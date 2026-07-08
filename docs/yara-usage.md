# YARA Rule Usage

This repository includes small YARA rules for identifying self-built lab samples.

The rules are written for educational and defensive analysis purposes only. They are not designed to detect real malware or third-party software.

## Rule List

| Rule | Target |
| --- | --- |
| Basic_Auth_Check_SelfBuilt_Lab | samples/01-basic-auth-check/bin/basic-auth-check.exe |

## Example Usage

From the repository root:

    yara yara/basic-auth-check.yar samples/01-basic-auth-check/bin/basic-auth-check.exe

Expected match:

    Basic_Auth_Check_SelfBuilt_Lab samples/01-basic-auth-check/bin/basic-auth-check.exe

## Notes

The Basic Auth Check rule matches a safe, self-built Windows console binary using a combination of unique strings:

- Program title
- Prompt text
- Expected passphrase
- Success message
- Failure message
- Helper function name

The rule also checks for the Windows PE header using:

    uint16(0) == 0x5A4D

This confirms that the target begins with the standard MZ header used by Windows PE files.
