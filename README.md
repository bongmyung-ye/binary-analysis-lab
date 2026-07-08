# Binary Analysis Lab

A practical reverse engineering and binary analysis lab using safe, self-built samples.

This repository documents small case studies focused on static analysis, dynamic debugging, string analysis, PE triage, YARA rules, and lightweight automation scripts.

All samples are created for educational and defensive analysis purposes only. This repository does not contain malware, cracking tools, license bypasses, or third-party software patches.

## What this lab covers

- Static analysis workflow with tools such as Ghidra
- Dynamic debugging notes with Windows debuggers such as x64dbg
- Hashing, string extraction, and PE header triage
- Import table review for small Windows binaries
- YARA rules for identifying safe, self-built samples
- Clean report writing for repeatable analysis

## Case studies

| Case | Topic | Status |
|---|---|---|
| 01 | Basic Auth Check | Completed |
| 02 | XOR Encoded Strings | Planned |
| 03 | PE Import Review | Planned |

## Repository structure

```txt
binary-analysis-lab/
?쒋? docs/                 # workflow, tools, and safety notes
?쒋? reports/              # analysis reports and templates
?쒋? samples/              # self-built sample source code
?쒋? scripts/              # small analysis helpers
?쒋? screenshots/          # Ghidra / x64dbg screenshots
?붴? yara/                 # detection rules for the lab samples
```

## Quick start

Clone the repository and inspect the sample source code.

```bash
git clone https://github.com/bongmyung-ye/binary-analysis-lab.git
cd binary-analysis-lab
```

Run the helper scripts against a compiled sample binary.

```bash
python scripts/hash-files.py samples/01-basic-auth-check/bin/basic-auth-check.exe
python scripts/extract-strings.py samples/01-basic-auth-check/bin/basic-auth-check.exe
python scripts/pe-summary.py samples/01-basic-auth-check/bin/basic-auth-check.exe
```

The `bin/` folders are intentionally ignored by Git. Build outputs should be generated locally and not committed unless there is a clear reason to preserve a small, safe sample binary.

## Build notes

The samples are intentionally small C programs. On Windows, they can be compiled with MinGW, MSYS2, Visual Studio Developer Command Prompt, or Clang.

Example with GCC or MinGW:

```bash
gcc samples/01-basic-auth-check/src/main.c -o samples/01-basic-auth-check/bin/basic-auth-check.exe
gcc samples/02-xor-encoded-strings/src/main.c -o samples/02-xor-encoded-strings/bin/xor-encoded-strings.exe
gcc samples/03-pe-import-review/src/main.c -o samples/03-pe-import-review/bin/pe-import-review.exe
```

PowerShell helper:

```powershell
./build.ps1
```

## Safety statement

This lab is limited to self-built samples and defensive analysis. It is not intended for unauthorized access, software cracking, license bypassing, malware distribution, or modifying third-party software.

See [`docs/safety-policy.md`](docs/safety-policy.md) for the full policy.

## Roadmap

- Add screenshots from Ghidra and x64dbg
- Complete case study reports
- Add YARA rule test notes
- Add lightweight import categorization script
- Add Korean summary page for profile visitors

## License

MIT
