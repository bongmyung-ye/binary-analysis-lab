# Case Study 02 - XOR Encoded Strings

## Summary

This case study analyzes a small self-built program that stores several strings in XOR-encoded form and decodes them at runtime.

The purpose of this sample is to practice identifying simple string encoding logic and comparing static observations with runtime output.

## Sample information

| Field | Value |
|---|---|
| File name | xor-encoded-strings.exe |
| File type | Windows PE executable |
| Architecture | To be confirmed after build |
| Size | To be recorded |
| MD5 | To be recorded |
| SHA1 | To be recorded |
| SHA256 | To be recorded |
| Build date | To be recorded |
| Analysis date | To be recorded |

## Analysis goals

- Compare visible strings before and after execution
- Locate the decode routine
- Identify the XOR key
- Observe decoded strings at runtime
- Recreate the decoding behavior with a small helper script if needed

## Static analysis notes

### Strings

Plaintext strings should be less visible before runtime because the sample stores selected messages in encoded byte arrays.

### Decode routine

The decode routine loops over a null-terminated byte buffer and applies the same XOR key to each byte.

### Function flow

The program decodes each buffer, then prints the decoded messages. This provides a small but practical example of runtime string recovery.

## Dynamic analysis notes

Suggested observations:

- Run string extraction before executing the program.
- Run the program and record the decoded output.
- Break on the decode routine or `puts` to inspect memory after decoding.

## YARA notes

A YARA rule for this sample should use a mix of encoded byte patterns and stable lab-specific strings. Avoid writing a broad rule that could match unrelated binaries.

## Conclusion

This sample demonstrates how a simple encoding technique can hide strings from quick triage while still being easy to recover through static and dynamic analysis.
