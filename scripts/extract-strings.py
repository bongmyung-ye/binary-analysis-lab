#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

ASCII_PATTERN = re.compile(rb"[ -~]{4,}")
UTF16LE_PATTERN = re.compile(rb"(?:[ -~]\x00){4,}")


def decode_ascii(value: bytes) -> str:
    return value.decode("ascii", errors="replace")


def decode_utf16le(value: bytes) -> str:
    return value.decode("utf-16le", errors="replace")


def iter_strings(data: bytes, include_utf16: bool) -> list[tuple[int, str, str]]:
    results: list[tuple[int, str, str]] = []

    for match in ASCII_PATTERN.finditer(data):
        results.append((match.start(), "ascii", decode_ascii(match.group())))

    if include_utf16:
        for match in UTF16LE_PATTERN.finditer(data):
            results.append((match.start(), "utf16le", decode_utf16le(match.group())))

    return sorted(results, key=lambda item: item[0])


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract simple ASCII and UTF-16LE strings from a binary file.")
    parser.add_argument("file", type=Path, help="Binary file to inspect")
    parser.add_argument("--no-utf16", action="store_true", help="Disable UTF-16LE string extraction")
    parser.add_argument("--min-length", type=int, default=4, help="Minimum string length for display filtering")
    args = parser.parse_args()

    if not args.file.is_file():
        raise SystemExit(f"File not found: {args.file}")

    data = args.file.read_bytes()
    for offset, encoding, value in iter_strings(data, include_utf16=not args.no_utf16):
        if len(value) < args.min_length:
            continue
        print(f"0x{offset:08x} {encoding:<7} {value}")


if __name__ == "__main__":
    main()
