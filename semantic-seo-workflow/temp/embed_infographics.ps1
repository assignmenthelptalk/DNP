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

$clientDataRoot = Get-ClientDataRoot
$pagesDir = Join-Path (Join-Path $clientDataRoot $ClientName) 'pages'
$infographicsPath = '../infographics'

if (-not (Test-Path $pagesDir)) {
    throw "Pages directory not found: $pagesDir"
}

# Helper: replace an infographic comment with a <figure> tag
function Replace-Infographic {
    param($content, $commentPattern, $svgFile, $altText, $caption)
    $figure = @"
<figure class="infographic">
  <img src="$infographicsPath/$svgFile" alt="$altText" width="100%" loading="lazy">
  <figcaption>$caption</figcaption>
</figure>
"@
    return $content -replace [regex]::Escape("<!-- INFOGRAPHIC: $commentPattern -->"), $figure
}

# Helper: remove an unmapped infographic comment
function Remove-Infographic {
    param($content, $commentPattern)
    return $content -replace [regex]::Escape("<!-- INFOGRAPHIC: $commentPattern -->"), ''
}

# ---------- Page 01: website-design-kenya.html ----------
$file = "$pagesDir\website-design-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'professional-vs-template-website-kenya' 'website-design-anatomy.svg' 'Anatomy of a high-converting Kenyan business website showing key design elements' 'Key elements of a high-converting Kenyan business website — from M-Pesa button to mobile-first layout.'
$c = Remove-Infographic $c 'website-cost-tiers-kenya'
Set-Content $file $c -NoNewline
Write-Host "Done: website-design-kenya.html"

# ---------- Page 02: seo-services-kenya.html ----------
$file = "$pagesDir\seo-services-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'google-ranking-factors-kenya' 'seo-3-pillars.svg' 'How Google ranks Kenyan business websites — Technical SEO, On-Page SEO, and Local SEO pillars' 'The three pillars Google uses to rank Kenyan business websites — and how Tupate Studio addresses each.'
Set-Content $file $c -NoNewline
Write-Host "Done: seo-services-kenya.html"

# ---------- Page 03: ecommerce-website-development-kenya.html ----------
$file = "$pagesDir\ecommerce-website-development-kenya.html"
$c = Get-Content $file -Raw
$c = Remove-Infographic $c 'Kenyan Online Shopper Expectations'
$c = Replace-Infographic $c 'Kenya E-commerce Platform Performance Comparison' 'mpesa-payment-flow.svg' 'M-Pesa STK Push payment flow for Kenyan e-commerce websites — 6 steps from cart to confirmed order' 'How M-Pesa STK Push works on a Kenyan e-commerce website — from cart to confirmed payment in under 10 seconds.'
Set-Content $file $c -NoNewline
Write-Host "Done: ecommerce-website-development-kenya.html"

# ---------- Page 04: local-seo-kenya.html ----------
$file = "$pagesDir\local-seo-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'Google Business Profile Optimization Checklist for Kenya' 'local-seo-google-pack.svg' 'Google 3-Pack local SEO pyramid for Kenyan businesses — how to get into the top 3 local results' 'How the Google Local 3-Pack works in Kenya — and the layers of optimization that put your business there.'
$c = Remove-Infographic $c 'Kenyan Local Search Behavior Patterns'
Set-Content $file $c -NoNewline
Write-Host "Done: local-seo-kenya.html"

# ---------- Page 05: website-redesign-kenya.html ----------
$file = "$pagesDir\website-redesign-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'Signs Your Business Website Needs a Redesign Kenya' 'website-redesign-signs.svg' '9 warning signs your Kenyan business website needs a redesign — from mobile failure to WordPress plugin chaos' '9 signs your Kenyan business website is losing you customers and needs a professional redesign.'
$c = Remove-Infographic $c 'Pre-Redesign Audit Checklist for Kenyan Businesses'
Set-Content $file $c -NoNewline
Write-Host "Done: website-redesign-kenya.html"

# ---------- Page 06: corporate-website-design-kenya.html ----------
$file = "$pagesDir\corporate-website-design-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'Corporate Website vs Business Website Comparison Kenya' 'corporate-vs-business-website.svg' 'Corporate website vs business website comparison for Kenyan companies — pages, audiences, features, and compliance differences' 'What separates a corporate website from a standard business website for Kenyan companies.'
$c = Remove-Infographic $c 'KDPA 2019 Corporate Website Compliance Checklist'
Set-Content $file $c -NoNewline
Write-Host "Done: corporate-website-design-kenya.html"

# ---------- Page 07: custom-website-vs-wordpress-kenya.html ----------
$file = "$pagesDir\custom-website-vs-wordpress-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'WordPress vs Custom Speed Comparison Kenya' 'custom-vs-wordpress-comparison.svg' 'Custom-built website vs WordPress performance comparison for Kenya — speed, security, Core Web Vitals, and 3-year cost' 'Custom-built vs WordPress: the performance, security, and cost reality for Kenyan businesses.'
Set-Content $file $c -NoNewline
Write-Host "Done: custom-website-vs-wordpress-kenya.html"

# ---------- Page 08: custom-ecommerce-development-kenya.html ----------
$file = "$pagesDir\custom-ecommerce-development-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'M-Pesa Daraja API Checkout Flow Kenya' 'daraja-api-architecture.svg' 'M-Pesa Daraja API architecture diagram showing how STK Push, C2B, and B2C connect to a custom Kenyan e-commerce store' 'How the Daraja API connects M-Pesa to a custom-built Kenyan e-commerce store — direct integration, no plugins.'
Set-Content $file $c -NoNewline
Write-Host "Done: custom-ecommerce-development-kenya.html"

# ---------- Page 09: mobile-first-website-design-kenya.html ----------
$file = "$pagesDir\mobile-first-website-design-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'kenya-mobile-internet-stats' 'kenya-mobile-internet-stats.svg' 'Kenya mobile internet statistics — 80 percent mobile users, 93 percent Safaricom 4G coverage, 90 percent Android market share' 'Kenya mobile internet by the numbers — why every Kenyan business website must be built mobile-first.'
Set-Content $file $c -NoNewline
Write-Host "Done: mobile-first-website-design-kenya.html"

# ---------- Page 10: technical-seo-audit-kenya.html ----------
$file = "$pagesDir\technical-seo-audit-kenya.html"
$c = Get-Content $file -Raw
$c = Replace-Infographic $c 'technical-seo-audit-8-dimensions' 'technical-seo-audit-8-dimensions.svg' 'Technical SEO audit 8 dimensions — crawlability, indexation, Core Web Vitals, mobile usability, HTTPS, schema markup, internal linking, and page speed for Kenyan websites' 'The 8 dimensions of a Tupate Studio technical SEO audit — what we check on every Kenyan business website.'
Set-Content $file $c -NoNewline
Write-Host "Done: technical-seo-audit-kenya.html"

Write-Host "`nAll infographics embedded successfully."
