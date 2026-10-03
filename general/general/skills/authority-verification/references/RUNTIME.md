# Runtime

## Requirements

- `CASEDEV_API_KEY` in the environment
- `casedev` CLI for the shell script
- `jq` for the shell script follow-on steps
- Python 3.9+ and the `casedev` package for the Python script
- Node.js 18+ and the `casedev` package for the TypeScript script

## Install

CLI:

```bash
brew tap CaseMark/casedev && brew install casedev
```

Python:

```bash
python3 -m pip install casedev
```

TypeScript:

```bash
npm install casedev
npm install -D tsx typescript @types/node
```

Shell helper:

```bash
brew install jq
```

## Environment

```bash
export CASEDEV_API_KEY="sk_case_YOUR_API_KEY"
```

## Preflight Checks

CLI workflow:

```bash
command -v casedev
command -v jq
casedev --version
```

Python workflow:

```bash
python3 -c "import casedev; print('ok')"
```

TypeScript workflow:

```bash
npx tsx --version
node -e "console.log(process.version)"
```

## Run Commands

CLI:

```bash
bash scripts/verify_authority.sh "531 U.S. 98" "equal protection"
```

Python:

```bash
python3 scripts/verify_authority.py --citation "531 U.S. 98" --highlight-query "equal protection"
```

TypeScript:

```bash
npx tsx scripts/verify_authority.ts --citation "531 U.S. 98" --highlight-query "equal protection"
```
