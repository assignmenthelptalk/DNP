param(
    [string]$ClientName = 'tupate.studio'
)

function Get-ClientDataRoot {
    $repoRoot = Split-Path -Parent $PSScriptRoot
    if ($env:CLIENT_DATA_ROOT) {
        return $env:CLIENT_DATA_ROOT
    }

    $configPath = Join-Path $repoRoot 'workspace.config.json'
    if (Test-Path $configPath) {
        $config = Get-Content $configPath -Raw | ConvertFrom-Json
        if ($config.client_data_root) {
            return $config.client_data_root
        }
    }

    return (Join-Path $repoRoot 'client_data')
}

$dir = Join-Path (Join-Path (Get-ClientDataRoot) $ClientName) 'page-briefs'
if (-not (Test-Path $dir)) {
    throw "Page briefs directory not found: $dir"
}
Get-ChildItem -Path $dir -Filter '*.md' | ForEach-Object {
    $content = Get-Content -Path $_.FullName -Raw
    $content = $content -replace 'Tupae Studio', 'Tupate Studio'
    $content = $content -replace 'tupae\.studio', 'tupate.studio'
    Set-Content -Path $_.FullName -Value $content -NoNewline
    Write-Host "Updated: $($_.Name)"
}
Write-Host "Done."
