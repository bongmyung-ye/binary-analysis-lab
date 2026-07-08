rule LAB_Basic_Auth_Check
{
    meta:
        description = "Identifies the self-built Basic Auth Check lab sample"
        author = "binary-analysis-lab"
        scope = "lab-only"
        sample = "01-basic-auth-check"

    strings:
        $mz = { 4D 5A }
        $banner = "Binary Analysis Lab - Basic Auth Check" ascii
        $success = "Access granted for lab sample." ascii
        $failure = "Access denied for lab sample." ascii

    condition:
        $mz at 0 and 2 of ($banner, $success, $failure)
}
