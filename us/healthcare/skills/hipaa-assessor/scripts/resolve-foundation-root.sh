#!/usr/bin/env sh
set -eu

is_foundation_root() {
  candidate=$1
  [ -f "$candidate/core/index/domain-inventory.yaml" ] &&
    [ -f "$candidate/core/applicability/triage-output-template.yaml" ] &&
    [ -f "$candidate/skills/hipaa-assessor/SKILL.md" ]
}

print_resolved() {
  cd "$1"
  pwd -P
  exit 0
}

find_repo_root() {
  dir=$1
  while :; do
    [ -e "$dir/.git" ] && { echo "$dir"; return 0; }
    parent=$(dirname "$dir")
    [ "$parent" = "$dir" ] && break
    dir=$parent
  done
  return 1
}

# Priority 1: explicit override (fail closed if set but invalid)
if [ "${HIPAA_FOUNDATION_ROOT:-}" ]; then
  if is_foundation_root "$HIPAA_FOUNDATION_ROOT"; then
    print_resolved "$HIPAA_FOUNDATION_ROOT"
  else
    echo "HIPAA_FOUNDATION_ROOT is set to '$HIPAA_FOUNDATION_ROOT' but it is not a valid hipaa-foundation checkout." >&2
    exit 1
  fi
fi

# Priority 2: cross-tool config file
config_file="${XDG_CONFIG_HOME:-$HOME/.config}/hipaa-assessor/config"
if [ -f "$config_file" ]; then
  config_path=$(sed -n '1{s/\r$//;p;}' "$config_file")
  case "$config_path" in
    /*)
      if is_foundation_root "$config_path"; then
        print_resolved "$config_path"
      fi
      ;;
    "")
      ;;
    *)
      echo "Config file $config_file must contain a single-line absolute path to a hipaa-foundation checkout." >&2
      exit 1
      ;;
  esac
fi

# Priority 3: well-known path convention
well_known="$HOME/github/hipaa-foundation"
if [ -d "$well_known" ] && is_foundation_root "$well_known"; then
  print_resolved "$well_known"
fi

# Priority 4: current working directory
cwd=$(pwd -P)
if is_foundation_root "$cwd"; then
  print_resolved "$cwd"
fi

# Priority 5: sibling of the target repo root (walk up to .git, then check sibling)
if repo_root=$(find_repo_root "$cwd"); then
  sibling_dir="$(dirname "$repo_root")/hipaa-foundation"
  if [ -d "$sibling_dir" ] && is_foundation_root "$sibling_dir"; then
    print_resolved "$sibling_dir"
  fi
fi

# Priority 6: immediate sibling of cwd (fallback if not inside a git repo)
parent_dir=$(dirname "$cwd")
sibling_dir="$parent_dir/hipaa-foundation"
if [ -d "$sibling_dir" ] && is_foundation_root "$sibling_dir"; then
  print_resolved "$sibling_dir"
fi

echo "Could not resolve hipaa-foundation." >&2
echo "Options:" >&2
echo "  1. Set HIPAA_FOUNDATION_ROOT env var" >&2
echo "  2. Write the path to ${XDG_CONFIG_HOME:-$HOME/.config}/hipaa-assessor/config" >&2
echo "  3. Clone to $HOME/github/hipaa-foundation" >&2
echo "  4. Clone next to your target repo" >&2
exit 1
