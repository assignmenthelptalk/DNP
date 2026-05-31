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

$pagesPath = Join-Path (Join-Path (Get-ClientDataRoot) $ClientName) 'pages'
if (-not (Test-Path $pagesPath)) {
    throw "Pages directory not found: $pagesPath"
}
$pages = Get-ChildItem (Join-Path $pagesPath '*.html')
foreach ($p in $pages) {
    $c = Get-Content $p.FullName -Raw
    $hasInfographic = if ($c -match '<figure class="infographic">') { 'YES' } else { 'NO ' }
    $hasSchema      = if ($c -match 'application/ld\+json') { 'YES' } else { 'NO ' }
    $hasFAQ         = if ($c -match 'FAQPage') { 'YES' } else { 'NO ' }
    $leftover       = ([regex]::Matches($c, 'INFOGRAPHIC:')).Count
    Write-Host "$($p.Name) | Fig:$hasInfographic | Schema:$hasSchema | FAQ:$hasFAQ | Leftover:$leftover"
}
