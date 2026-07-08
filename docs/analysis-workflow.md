# Analysis Workflow

This workflow keeps each case study consistent and easy to review.

## 1. Identify the sample

Record the file name, file size, hashes, compiler notes, and analysis date.

```bash
python scripts/hash-files.py path/to/sample.exe
```

## 2. Collect quick triage data

Check basic PE metadata and strings before opening the binary in a debugger.

```bash
python scripts/pe-summary.py path/to/sample.exe
python scripts/extract-strings.py path/to/sample.exe
```

## 3. Static analysis

Open the sample in Ghidra or another static analysis tool.

Focus on:

- Entry point
- Main function
- Referenced strings
- Imported functions
- Branching logic
- Small helper functions

## 4. Dynamic analysis

Run the sample in a local test environment and observe behavior.

Focus on:

- Console output
- Input handling
- Breakpoints around interesting functions
- Runtime-decoded strings
- Branch decisions

## 5. Document findings

Use `reports/_template.md` and keep the writing factual. Include screenshots only when they make the analysis easier to verify.

## 6. Add detection notes

When useful, write a small YARA rule for the sample and explain what it detects.

Avoid overly broad rules that match unrelated files.
