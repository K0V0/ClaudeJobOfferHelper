# Windows without Git Bash. Runs the prebuilt save-offer, downloaded once and checked against save-offer.lock.
# Without a usable build it runs scripts/save_offer.py with whichever Python this system has.
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$tools = Join-Path $env:USERPROFILE 'JobOfferHelper\.tools'

function Get-Prebuilt {
    $lock = Join-Path $PSScriptRoot 'save-offer.lock'
    if (-not (Test-Path $lock)) { return $null }
    $line = Get-Content $lock | Where-Object { $_ -like 'save-offer-windows-x64.exe *' } | Select-Object -First 1
    if (-not $line) { return $null }
    $name, $sha, $url = $line -split '\s+'
    $target = Join-Path $tools "$sha-$name"
    if (Test-Path $target) { return $target }
    [Console]::Error.WriteLine('Downloading save-offer, only the first time ...')
    $partial = "$target.$PID.exe"
    try {
        New-Item -ItemType Directory -Force -Path $tools | Out-Null
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $partial
        if ((Get-FileHash -Algorithm SHA256 $partial).Hash.ToLower() -ne $sha) { throw 'checksum' }
        & $partial --help *> $null
        if ($LASTEXITCODE -ne 0) { throw 'broken' }
        Move-Item -Force $partial $target
        Get-ChildItem $tools -Filter "*-$name" | Where-Object { $_.FullName -ne $target } | Remove-Item -Force -ErrorAction SilentlyContinue
        return $target
    } catch {
        [Console]::Error.WriteLine('Prebuilt save-offer can not be used here, trying Python.')
        Remove-Item -Force -ErrorAction SilentlyContinue $partial
        return $null
    }
}

$executable = Get-Prebuilt
if ($executable) {
    & $executable @args
    exit $LASTEXITCODE
}

$script = Join-Path $PSScriptRoot '..\scripts\save_offer.py'
foreach ($python in 'python3', 'python', 'py') {
    if (-not (Get-Command $python -ErrorAction SilentlyContinue)) { continue }
    try { & $python -c 'import sys; sys.exit(sys.version_info < (3, 10))' *> $null } catch { continue }
    if ($LASTEXITCODE -eq 0) {
        & $python $script @args
        exit $LASTEXITCODE
    }
}
[Console]::Error.WriteLine('FAILED: no prebuilt save-offer and no Python 3.10 or newer. Nothing was written.')
exit 3
