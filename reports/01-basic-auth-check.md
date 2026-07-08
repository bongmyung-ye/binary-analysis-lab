# Case Study 01 - Basic Auth Check

## Summary

This case study analyzes a small self-built console program that asks for a passphrase and prints either a success or failure message.

The purpose of this sample is to document a basic static and dynamic analysis workflow without modifying third-party software.

## Sample information

| Field | Value |
|---|---|
| File name | basic-auth-check.exe |
| File type | Windows PE executable |
| Architecture | To be confirmed after build |
| Size | To be recorded |
| MD5 | To be recorded |
| SHA1 | To be recorded |
| SHA256 | To be recorded |
| Build date | To be recorded |
| Analysis date | To be recorded |

## Analysis goals

- Locate the user input handling logic
- Identify the string comparison function
- Observe the success and failure branches
- Confirm runtime behavior with a debugger

## Static analysis notes

### Strings

Expected strings include:

- `Binary Analysis Lab - Basic Auth Check`
- `Enter passphrase:`
- `Access granted for lab sample.`
- `Access denied for lab sample.`
- `lab-pass-2026`

These strings provide useful anchors for locating the main control flow in a disassembler.

### Imports

Expected imports depend on the compiler and runtime, but the sample should include standard C runtime functions related to console input, output, and string comparison.

### Function flow

The source contains a small helper named `verify_passphrase`. In a stripped binary, the function name may not be preserved, but the comparison behavior can still be identified through string references and call flow.

## Dynamic analysis notes

Suggested observations:

- Run the program with an incorrect input and confirm the failure branch.
- Run the program with the expected passphrase and confirm the success branch.
- Set a breakpoint near the comparison call to observe both branch outcomes.

## YARA notes

A simple rule can identify this lab sample using stable strings and the PE magic header. The rule should not be treated as a generic detection rule.

## Conclusion

This sample is useful for practicing entry-level binary triage, string reference review, and branch-flow documentation in a controlled environment.
