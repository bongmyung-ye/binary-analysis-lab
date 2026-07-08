# 03 - PE Import Review

This sample calls a few harmless Windows APIs so the import table has more useful analysis material.

The goal is to practice PE triage and import table review. The sample does not perform destructive actions.

## Analysis focus

- Confirm PE header metadata
- Review imported DLLs and functions
- Categorize imports by behavior
- Compare import table observations with source code

## Build

```bash
gcc src/main.c -o bin/pe-import-review.exe
```

From the repository root:

```bash
gcc samples/03-pe-import-review/src/main.c -o samples/03-pe-import-review/bin/pe-import-review.exe
```
