#!/usr/bin/env python3
"""onboarding — show the first-use Companion orientation once, then never again.

Holds <root>/onboarding.json (default ~/.lq): UI state, not learning data — no
profile, no journey, no transcript, no identity. The learning store opens only
through the consent-gated store contract; this marker never gates it.

`offer` claims a five-minute token so two concurrent sessions cannot both show
the full intro; `shown --token` acknowledges with that token. `preview`
replays the introduction on request without reading or writing the marker.
Orientation content is never hardcoded here — the map comes from the live
catalog (see legalquants/SKILL.md). Corrupt state is preserved for repair and
the intro still shows. Stdlib only. --root overrides ~/.lq (tests).
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import secrets
import sys
import time

CLAIM_TTL_S = 300
STATE = "onboarding.json"


def root_of(args) -> pathlib.Path:
    return pathlib.Path(args.root) if args.root else pathlib.Path.home() / ".lq"


def atomic_write(path: pathlib.Path, text: str) -> None:
    # tmp+rename, same convention as the profile store: a crash never leaves
    # half a marker.
    tmp = path.with_suffix(path.suffix + f".tmp.{os.getpid()}")
    tmp.write_text(text)
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass
    # os.replace, not Path.rename: on Windows rename refuses an existing target,
    # so every second write of the store or marker failed there.
    os.replace(tmp, path)


class Lock:
    def __init__(self, root: pathlib.Path):
        self.path = root / ".onboarding.lock"

    def __enter__(self):
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
        except FileExistsError:
            sys.exit(
                "another onboarding operation is running (lockfile held). "
                f"If that is wrong, remove {self.path} and retry."
            )
        return self

    def __exit__(self, *_):
        self.path.unlink(missing_ok=True)


def cmd_offer(args):
    root = root_of(args)
    root.mkdir(parents=True, exist_ok=True)  # the lockfile needs the dir to exist
    try:
        os.chmod(root, 0o700)
    except OSError:
        pass
    with Lock(root):
        path = root / STATE
        try:
            state = json.loads(path.read_text()) if path.exists() else {}
        except ValueError:
            print(
                json.dumps(
                    {
                        "show": True,
                        "token": None,
                        "warning": "welcome state needs repair; nothing changed",
                    }
                )
            )
            return
        if state.get("shown"):
            print(json.dumps({"show": False, "reason": "already_shown"}))
            return
        if state.get("expires", 0) > time.time():
            print(
                json.dumps({"show": False, "reason": "another_session_is_showing_it"})
            )
            return
        token = secrets.token_hex(12)
        atomic_write(
            path,
            json.dumps(
                {"shown": False, "token": token, "expires": time.time() + CLAIM_TTL_S}
            ),
        )
        print(json.dumps({"show": True, "token": token}))


def cmd_preview(args):
    """Replay on request: show without reading or writing the marker."""
    print(json.dumps({"show": True, "preview": True, "marker_untouched": True}))


def cmd_shown(args):
    root = root_of(args)
    root.mkdir(parents=True, exist_ok=True)  # the lockfile needs the dir to exist
    try:
        os.chmod(root, 0o700)
    except OSError:
        pass
    with Lock(root):
        path = root / STATE
        try:
            state = json.loads(path.read_text())
        except (ValueError, OSError):
            sys.exit("no welcome claim to acknowledge; state unchanged.")
        if not args.token or state.get("token") != args.token:
            sys.exit("welcome token does not match; state unchanged.")
        atomic_write(path, json.dumps({"shown": True, "shown_at": time.time()}))
    print(json.dumps({"shown": True}))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", help="override ~/.lq (tests)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("offer")
    sub.add_parser("preview")
    sh = sub.add_parser("shown")
    sh.add_argument("--token")
    args = ap.parse_args()
    {"offer": cmd_offer, "preview": cmd_preview, "shown": cmd_shown}[args.cmd](args)


if __name__ == "__main__":
    main()
