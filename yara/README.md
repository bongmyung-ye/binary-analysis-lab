# YARA Rules

These rules are written only for the safe, self-built samples in this repository.

They are not generic malware detection rules. Each rule should be documented in the matching case study report before being used in a wider context.

Example:

```bash
yara yara/basic-auth-check.yar samples/01-basic-auth-check/bin/basic-auth-check.exe
```
