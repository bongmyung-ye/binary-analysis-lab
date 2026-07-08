# 01 - Basic Auth Check

This sample is a small console program that asks for a passphrase and prints a success or failure message.

The goal is to practice basic static and dynamic analysis without modifying or bypassing third-party software.

## Analysis focus

- Locate the `main` function
- Review referenced strings
- Identify the input comparison logic
- Observe the success and failure branches
- Compare static observations with runtime behavior

## Build

```bash
gcc src/main.c -o bin/basic-auth-check.exe
```

From the repository root:

```bash
gcc samples/01-basic-auth-check/src/main.c -o samples/01-basic-auth-check/bin/basic-auth-check.exe
```
