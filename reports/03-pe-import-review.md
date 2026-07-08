# Case Study 03 - PE Import Review

## Overview

This case study analyzes a small self-built Windows PE executable that calls harmless Windows APIs to create useful import table material.

The goal of this sample is to practice PE triage, import table review, behavior categorization, and safe analysis documentation.

## Sample Information

| Field | Value |
| --- | --- |
| Sample | pe-import-review.exe |
| Path | samples/03-pe-import-review/bin/pe-import-review.exe |
| MD5 | 46dfbfc86ea74011aaf6623edc6bde4c |
| SHA-1 | 926e13c710e7658eb0bd17b014ebecf25adfdcfe |
| SHA-256 | 3e0372f35523b4b7429535894b7060d22bcbfd71c5fbed43c8841730ab28c931 |
| Size | 136838 bytes |
| Format | Windows PE executable |
| Architecture | x64 |
| Build Toolchain | MSYS2 MinGW-w64 GCC |
| Analysis Date | 2026-07-09 |

## Runtime Behavior

The program prints a short banner, reads basic local environment information, prints the current Windows user name, and prints a tick count value.

Observed runtime output:

    Binary Analysis Lab - PE Import Review
    Current user: user2
    Tick count: 48838703

The tick count value changes on each run because it is generated at runtime.

## Source-Level Behavior

The sample is intentionally small and transparent.

High-level flow:

    main -> print banner -> Windows API calls -> print observed values -> exit

The Windows-specific routine uses a few harmless APIs:

| API | Purpose |
| --- | --- |
| GetUserNameA | Reads the current local user name |
| GetTickCount | Reads system uptime tick count |
| MessageBoxA | Displays a simple message box when available in the sample build |

These APIs are used only to create import table material for analysis practice.

## Import Review Notes

The source code is expected to produce imports related to:

| DLL | Expected reason |
| --- | --- |
| KERNEL32.dll | Runtime support and GetTickCount |
| ADVAPI32.dll | GetUserNameA |
| USER32.dll | MessageBoxA |
| api-ms-win-crt-* | C runtime support from the MinGW-w64/UCRT toolchain |

The presence of these imports does not indicate malicious behavior by itself. In real triage work, imports are reviewed together with strings, control flow, runtime behavior, persistence indicators, network behavior, file operations, and other context.

## PE Triage Notes

Important triage questions for this sample:

| Question | Observation |
| --- | --- |
| Is this a Windows executable? | Yes, it is a PE executable. |
| Does it use GUI-related APIs? | The sample is designed to include MessageBoxA when available. |
| Does it read local user information? | Yes, it calls GetUserNameA. |
| Does it perform network activity? | No network behavior is implemented. |
| Does it modify files or registry keys? | No file or registry modification is implemented. |
| Does it implement persistence? | No persistence behavior is implemented. |
| Does it execute external commands? | No external command execution is implemented. |

## Analysis Summary

This sample demonstrates a basic PE import review workflow:

1. Confirm the file type and architecture.
2. Review user-facing strings.
3. Inspect imported DLLs and functions.
4. Map imports back to source-level behavior.
5. Separate harmless runtime imports from sample-specific API usage.
6. Document behavior without over-interpreting imports.

## Defensive Context

Import table review is a common early triage step in Windows binary analysis. It can quickly suggest areas of interest, but imports alone are not enough to classify a binary as benign or malicious.

This sample is safe and self-built. It does not contain malware, persistence, credential theft, network communication, destructive behavior, evasion, or third-party software bypassing.

## YARA Rule

A lab-only YARA rule is available for this sample.

Rule path:

    yara/pe-import-review.yar

The rule matches the PE header and sample-specific strings such as:

    Binary Analysis Lab - PE Import Review
    Current user:
    Tick count:

Expected local usage:

    yara yara/pe-import-review.yar samples/03-pe-import-review/bin/pe-import-review.exe

Expected match:

    PE_Import_Review_SelfBuilt_Lab samples/03-pe-import-review/bin/pe-import-review.exe

## Next Steps

- Capture a Ghidra screenshot showing references to GetUserNameA, GetTickCount, and MessageBoxA.
- Capture an import table screenshot from a PE analysis tool.
- Add a short note comparing source-level API calls with observed imports.
