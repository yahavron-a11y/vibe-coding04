<#
.SYNOPSIS
    Builds the CivicShield AI Preliminary Report (LuaLaTeX + BibTeX) and
    automatically syncs main.pdf to the project root CivicShield_AI_Preliminary_Report.pdf.
#>
param(
    [switch]$Fast
)

$ErrorActionPreference = "Stop"
$MasterDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = (Resolve-Path (Join-Path $MasterDir "..\..")).Path
$TargetPdf = Join-Path $ProjectRoot "CivicShield_AI_Preliminary_Report.pdf"
$SourcePdf = Join-Path $MasterDir "main.pdf"

Push-Location $MasterDir
try {
    Write-Host "[1/4] Running LuaLaTeX (pass 1)..."
    lualatex -interaction=nonstopmode main.tex > lualatex_pass1.log 2>&1
    if ($LASTEXITCODE -ne 0) { throw "LuaLaTeX pass 1 failed. See lualatex_pass1.log" }

    if (-not $Fast) {
        Write-Host "[2/3] Running LuaLaTeX (pass 2)..."
        lualatex -interaction=nonstopmode main.tex > lualatex_pass2.log 2>&1
        if ($LASTEXITCODE -ne 0) { throw "LuaLaTeX pass 2 failed. See lualatex_pass2.log" }
    }

    Write-Host "[3/3] Running LuaLaTeX (final pass)..."
    lualatex -interaction=nonstopmode main.tex > lualatex_final.log 2>&1
    if ($LASTEXITCODE -ne 0) { throw "LuaLaTeX final pass failed. See lualatex_final.log" }

    if (-not (Test-Path $SourcePdf)) {
        throw "Expected output PDF not found at $SourcePdf"
    }

    Copy-Item -Path $SourcePdf -Destination $TargetPdf -Force
    $sha = [System.Security.Cryptography.SHA256]::Create()
    $srcHash = [BitConverter]::ToString($sha.ComputeHash([System.IO.File]::ReadAllBytes($SourcePdf))).Replace("-","")
    $dstHash = [BitConverter]::ToString($sha.ComputeHash([System.IO.File]::ReadAllBytes($TargetPdf))).Replace("-","")
    if ($srcHash -ne $dstHash) {
        throw "SHA-256 mismatch after copying PDF to $TargetPdf"
    }

    $size = (Get-Item $TargetPdf).Length
    Write-Host "SUCCESS: Built and synced $TargetPdf ($size bytes, SHA256=$dstHash)"
}
finally {
    Pop-Location
}
