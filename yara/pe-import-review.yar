rule PE_Import_Review_SelfBuilt_Lab
{
    meta:
        description = "Detects the self-built PE Import Review sample from binary-analysis-lab"
        author = "bongmyung-ye"
        scope = "self-built lab sample"
        sample = "pe-import-review.exe"
        sha256 = "3e0372f35523b4b7429535894b7060d22bcbfd71c5fbed43c8841730ab28c931"
        purpose = "educational and defensive PE import review"

    strings:
        $banner = "Binary Analysis Lab - PE Import Review" ascii
        $current_user = "Current user:" ascii
        $tick_count = "Tick count:" ascii
        $title = "Binary Analysis Lab" ascii
        $user32 = "USER32.dll" ascii nocase
        $advapi32 = "ADVAPI32.dll" ascii nocase
        $api_messagebox = "MessageBoxA" ascii
        $api_username = "GetUserNameA" ascii

    condition:
        uint16(0) == 0x5A4D and
        filesize < 300KB and
        $banner and
        2 of ($current_user, $tick_count, $title, $user32, $advapi32, $api_messagebox, $api_username)
}
