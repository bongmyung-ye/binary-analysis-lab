#!/usr/bin/env python3
import argparse
import hashlib
from pathlib import Path


def digest_file(path: Path) -> dict[str, str]:
    hashes = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256(),
    }

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            for hasher in hashes.values():
                hasher.update(chunk)

    return {name: hasher.hexdigest() for name, hasher in hashes.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate MD5, SHA1, and SHA256 for files.")
    parser.add_argument("files", nargs="+", type=Path, help="Files to hash")
    args = parser.parse_args()

    for path in args.files:
        if not path.is_file():
            print(f"[skip] {path} is not a file")
            continue

        result = digest_file(path)
        print(f"File: {path}")
        print(f"Size: {path.stat().st_size} bytes")
        print(f"MD5: {result['md5']}")
        print(f"SHA1: {result['sha1']}")
        print(f"SHA256: {result['sha256']}")
        print()


if __name__ == "__main__":
    main()
