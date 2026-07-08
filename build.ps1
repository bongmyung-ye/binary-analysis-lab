$ErrorActionPreference = "Stop"

$Samples = @(
    @{ Name = "basic-auth-check"; Source = "samples/01-basic-auth-check/src/main.c"; Output = "samples/01-basic-auth-check/bin/basic-auth-check.exe" },
    @{ Name = "xor-encoded-strings"; Source = "samples/02-xor-encoded-strings/src/main.c"; Output = "samples/02-xor-encoded-strings/bin/xor-encoded-strings.exe" },
    @{ Name = "pe-import-review"; Source = "samples/03-pe-import-review/src/main.c"; Output = "samples/03-pe-import-review/bin/pe-import-review.exe" }
)

foreach ($Sample in $Samples) {
    $OutputDir = Split-Path $Sample.Output -Parent
    New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

    Write-Host "Building $($Sample.Name)..."
    gcc $Sample.Source -o $Sample.Output
}

Write-Host "Build complete."
