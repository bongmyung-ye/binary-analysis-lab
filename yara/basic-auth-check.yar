rule Basic_Auth_Check_SelfBuilt_Lab
{
    meta:
        description = "Detects the self-built Basic Auth Check sample from binary-analysis-lab"
        author = "bongmyung-ye"
        scope = "self-built lab sample"
        sample = "basic-auth-check.exe"
        sha256 = "edf54c2da41feb107a001a5b98e147de89cee9e05a973ce18ca486b38710a860"
        date = "2026-07-08"
        purpose = "educational and defensive analysis"

    strings:
        $title = "Binary Analysis Lab - Basic Auth Check" ascii
        $prompt = "Enter passphrase:" ascii
        $passphrase = "lab-pass-2026" ascii
        $success = "Access granted for lab sample." ascii
        $failure = "Access denied for lab sample." ascii
        $function_name = "verify_passphrase" ascii

    condition:
        uint16(0) == 0x5A4D and
        filesize < 300KB and
        4 of them
}
