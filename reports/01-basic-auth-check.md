# Case Study 01 - Basic Auth Check

## Overview

This case study analyzes a small self-built Windows console binary that validates a user-provided passphrase and prints a success or failure message.

The goal of this sample is to document a basic binary analysis workflow using a safe program created only for defensive learning and analysis practice.

## Sample Information

| Field | Value |
| --- | --- |
| Sample | basic-auth-check.exe |
| Path | samples/01-basic-auth-check/bin/basic-auth-check.exe |
| SHA-256 | edf54c2da41feb107a001a5b98e147de89cee9e05a973ce18ca486b38710a860 |
| Size | 135,594 bytes |
| Format | PE32+ |
| Architecture | x64 |
| Sections | 19 |
| Entry Point RVA | 0x00001460 |
| Image Base | 0x140000000 |
| Build Toolchain | MSYS2 MinGW-w64 GCC |

## Runtime Behavior

The program displays a title, asks the user for a passphrase, and then prints one of two messages depending on the input.

### Failed input

    Binary Analysis Lab - Basic Auth Check
    Enter passphrase: test
    Access denied for lab sample.

### Valid input

    Binary Analysis Lab - Basic Auth Check
    Enter passphrase: lab-pass-2026
    Access granted for lab sample.

## Static Analysis Notes

The source and extracted strings show a simple authentication-style control flow.

    input -> newline cleanup -> passphrase comparison -> success/failure branch

The binary contains the expected passphrase as a readable string.

    lab-pass-2026

Relevant user-facing strings include:

    Binary Analysis Lab - Basic Auth Check
    Enter passphrase:
    Access granted for lab sample.
    Access denied for lab sample.

The main comparison logic is implemented through a small helper routine named verify_passphrase.

At source level, the function compares the user input against the expected passphrase using strcmp.

    static int verify_passphrase(const char *input) {
        const char *expected = "lab-pass-2026";
        return strcmp(input, expected) == 0;
    }

## String and Function Observations

| Category | Observed value |
| --- | --- |
| Passphrase | lab-pass-2026 |
| Success message | Access granted for lab sample. |
| Failure message | Access denied for lab sample. |
| Input function | fgets |
| Newline cleanup | strcspn |
| Comparison function | strcmp |
| Helper routine | verify_passphrase |

The output also contains many MinGW and UCRT runtime symbols. These are expected for a Windows console binary built with MSYS2 MinGW-w64 GCC and are not part of the sample-specific authentication logic.

## PE Summary

The sample is a 64-bit Windows PE file.

| Field | Value |
| --- | --- |
| Format | PE32+ |
| Machine | x64 |
| Sections | 19 |
| Entry Point RVA | 0x00001460 |
| Image Base | 0x140000000 |

Observed sections include:

    .text
    .data
    .rdata
    .pdata
    .xdata
    .bss
    .idata
    .tls
    .rsrc
    .reloc

Imported DLLs include:

    KERNEL32.dll
    api-ms-win-crt-environment-l1-1-0.dll
    api-ms-win-crt-heap-l1-1-0.dll
    api-ms-win-crt-locale-l1-1-0.dll
    api-ms-win-crt-math-l1-1-0.dll
    api-ms-win-crt-private-l1-1-0.dll
    api-ms-win-crt-runtime-l1-1-0.dll
    api-ms-win-crt-stdio-l1-1-0.dll
    api-ms-win-crt-string-l1-1-0.dll

These imports are consistent with a small C console program using standard input, output, and string comparison routines.

## Analysis Summary

This sample demonstrates a basic static and behavioral analysis workflow:

1. Identify user-facing strings.
2. Locate the expected passphrase.
3. Review the input handling path.
4. Identify the comparison routine.
5. Confirm success and failure branches through runtime testing.
6. Review PE metadata and imported runtime libraries.

The sample does not implement destructive behavior, persistence, network communication, credential theft, evasion, or third-party software bypassing. It is intentionally limited to a safe self-built binary for analysis practice.

## Next Steps

- Capture a Ghidra screenshot showing the verify_passphrase routine.
- Capture an x64dbg screenshot showing the branch after the string comparison.
- Add a small YARA rule that matches this self-built sample by its unique strings.
