rule LAB_XOR_Encoded_Strings
{
    meta:
        description = "Identifies the self-built XOR Encoded Strings lab sample"
        author = "binary-analysis-lab"
        scope = "lab-only"
        sample = "02-xor-encoded-strings"

    strings:
        $mz = { 4D 5A }
        $encoded_banner_start = { 75 5E 59 56 45 4E 17 76 59 56 5B 4E 44 5E 44 }
        $encoded_note_start = { 64 56 51 52 17 44 52 5B 51 1A 55 42 5E 5B 43 }
        $key_hint = { 37 }

    condition:
        $mz at 0 and $encoded_banner_start and $encoded_note_start and $key_hint
}
