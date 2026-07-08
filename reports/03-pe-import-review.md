# Case Study 03 - PE Import Review

## Summary

This case study analyzes a small self-built Windows program that calls harmless Windows APIs to create useful import table material.

The purpose of this sample is to practice PE triage and import review without using malicious behavior.

## Sample information

| Field | Value |
|---|---|
| File name | pe-import-review.exe |
| File type | Windows PE executable |
| Architecture | To be confirmed after build |
| Size | To be recorded |
| MD5 | To be recorded |
| SHA1 | To be recorded |
| SHA256 | To be recorded |
| Build date | To be recorded |
| Analysis date | To be recorded |

## Analysis goals

- Confirm PE header metadata
- Identify imported DLLs and functions
- Categorize imports by behavior
- Compare import table results with source code

## Static analysis notes

### Imports

Expected Windows API imports may include:

- `KERNEL32.dll`
- `ADVAPI32.dll`
- `USER32.dll`

Exact imports depend on the compiler and linker.

### Behavior categories

The sample may include imports related to:

- Console output
- Username lookup
- Tick count retrieval
- Message box display

These imports are used for analysis practice only and do not indicate malicious behavior on their own.

## Dynamic analysis notes

Suggested observations:

- Run the sample in a local Windows test environment.
- Confirm that it prints a short message and displays a message box.
- Compare observed behavior with imported functions.

## YARA notes

A sample-specific YARA rule can combine lab strings with selected imports. The rule should be documented as a lab-only identification rule.

## Conclusion

This sample helps practice import table review and basic PE triage while keeping behavior transparent and safe.
