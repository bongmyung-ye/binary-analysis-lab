#!/usr/bin/env python3
import argparse
import datetime as dt
import struct
from dataclasses import dataclass
from pathlib import Path

MACHINE_TYPES = {
    0x014C: "Intel 386",
    0x8664: "x64",
    0x01C0: "ARM",
    0x01C4: "ARMv7",
    0xAA64: "ARM64",
}

SUBSYSTEMS = {
    1: "Native",
    2: "Windows GUI",
    3: "Windows CUI",
    9: "Windows CE GUI",
    10: "EFI Application",
}

@dataclass
class Section:
    name: str
    virtual_address: int
    virtual_size: int
    raw_pointer: int
    raw_size: int


def read_u16(data: bytes, offset: int) -> int:
    return struct.unpack_from("<H", data, offset)[0]


def read_u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def read_c_string(data: bytes, offset: int) -> str:
    end = data.find(b"\x00", offset)
    if end == -1:
        end = min(len(data), offset + 256)
    return data[offset:end].decode("ascii", errors="replace")


def rva_to_offset(rva: int, sections: list[Section]) -> int | None:
    for section in sections:
        start = section.virtual_address
        size = max(section.virtual_size, section.raw_size)
        end = start + size
        if start <= rva < end:
            return section.raw_pointer + (rva - start)
    return None


def parse_sections(data: bytes, section_table_offset: int, count: int) -> list[Section]:
    sections: list[Section] = []
    for index in range(count):
        offset = section_table_offset + index * 40
        raw_name = data[offset:offset + 8].split(b"\x00", 1)[0]
        name = raw_name.decode("ascii", errors="replace")
        virtual_size = read_u32(data, offset + 8)
        virtual_address = read_u32(data, offset + 12)
        raw_size = read_u32(data, offset + 16)
        raw_pointer = read_u32(data, offset + 20)
        sections.append(Section(name, virtual_address, virtual_size, raw_pointer, raw_size))
    return sections


def parse_imports(data: bytes, optional_header_offset: int, magic: int, sections: list[Section]) -> list[str]:
    data_directory_offset = optional_header_offset + (112 if magic == 0x20B else 96)
    import_table_rva = read_u32(data, data_directory_offset + 8)
    import_table_size = read_u32(data, data_directory_offset + 12)

    if import_table_rva == 0 or import_table_size == 0:
        return []

    import_offset = rva_to_offset(import_table_rva, sections)
    if import_offset is None:
        return []

    imports: list[str] = []
    descriptor_size = 20
    cursor = import_offset

    while cursor + descriptor_size <= len(data):
        original_first_thunk = read_u32(data, cursor)
        time_date_stamp = read_u32(data, cursor + 4)
        forwarder_chain = read_u32(data, cursor + 8)
        name_rva = read_u32(data, cursor + 12)
        first_thunk = read_u32(data, cursor + 16)

        if not any([original_first_thunk, time_date_stamp, forwarder_chain, name_rva, first_thunk]):
            break

        name_offset = rva_to_offset(name_rva, sections)
        if name_offset is not None and 0 <= name_offset < len(data):
            imports.append(read_c_string(data, name_offset))

        cursor += descriptor_size

    return imports


def summarize_pe(path: Path) -> None:
    data = path.read_bytes()

    if len(data) < 0x40 or data[:2] != b"MZ":
        raise SystemExit("Not a PE file: missing MZ header")

    pe_offset = read_u32(data, 0x3C)
    if data[pe_offset:pe_offset + 4] != b"PE\x00\x00":
        raise SystemExit("Not a PE file: missing PE signature")

    coff_offset = pe_offset + 4
    machine = read_u16(data, coff_offset)
    section_count = read_u16(data, coff_offset + 2)
    timestamp = read_u32(data, coff_offset + 4)
    optional_header_size = read_u16(data, coff_offset + 16)
    characteristics = read_u16(data, coff_offset + 18)

    optional_header_offset = coff_offset + 20
    magic = read_u16(data, optional_header_offset)
    is_pe32_plus = magic == 0x20B
    entry_point_rva = read_u32(data, optional_header_offset + 16)
    image_base = struct.unpack_from("<Q" if is_pe32_plus else "<I", data, optional_header_offset + 24)[0]
    subsystem = read_u16(data, optional_header_offset + (92 if is_pe32_plus else 68))

    section_table_offset = optional_header_offset + optional_header_size
    sections = parse_sections(data, section_table_offset, section_count)
    imports = parse_imports(data, optional_header_offset, magic, sections)

    build_time = dt.datetime.fromtimestamp(timestamp, tz=dt.timezone.utc).isoformat()

    print(f"File: {path}")
    print(f"Size: {path.stat().st_size} bytes")
    print(f"Format: {'PE32+' if is_pe32_plus else 'PE32'}")
    print(f"Machine: {MACHINE_TYPES.get(machine, hex(machine))}")
    print(f"Sections: {section_count}")
    print(f"Timestamp: {build_time}")
    print(f"Entry point RVA: 0x{entry_point_rva:08x}")
    print(f"Image base: 0x{image_base:x}")
    print(f"Subsystem: {SUBSYSTEMS.get(subsystem, str(subsystem))}")
    print(f"Characteristics: 0x{characteristics:04x}")
    print()
    print("Sections")
    for section in sections:
        print(
            f"- {section.name:<8} VA=0x{section.virtual_address:08x} "
            f"VSZ=0x{section.virtual_size:08x} RAW=0x{section.raw_pointer:08x} RSZ=0x{section.raw_size:08x}"
        )

    print()
    print("Imported DLLs")
    if imports:
        for name in imports:
            print(f"- {name}")
    else:
        print("- none found or import table could not be parsed")


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a small PE header and import summary.")
    parser.add_argument("file", type=Path, help="PE file to inspect")
    args = parser.parse_args()

    if not args.file.is_file():
        raise SystemExit(f"File not found: {args.file}")

    summarize_pe(args.file)


if __name__ == "__main__":
    main()
