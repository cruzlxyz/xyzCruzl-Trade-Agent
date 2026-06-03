if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 "$PSScriptRoot\src\main.py" @args
    exit $LASTEXITCODE
}

if (Get-Command python -ErrorAction SilentlyContinue) {
    & python "$PSScriptRoot\src\main.py" @args
    exit $LASTEXITCODE
}

Write-Host "Python not found. Install Python 3.10+ from https://www.python.org/downloads/"
exit 1
