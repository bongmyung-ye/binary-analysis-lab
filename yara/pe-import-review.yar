rule LAB_PE_Import_Review
{
    meta:
        description = "Identifies the self-built PE Import Review lab sample"
        author = "binary-analysis-lab"
        scope = "lab-only"
        sample = "03-pe-import-review"

    strings:
        $mz = { 4D 5A }
        $banner = "Binary Analysis Lab - PE Import Review" ascii
        $message = "PE Import Review sample executed." ascii
        $user32 = "USER32.dll" ascii nocase

    condition:
        $mz at 0 and $banner and any of ($message, $user32)
}
