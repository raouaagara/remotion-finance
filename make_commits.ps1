$cwd = "c:\Users\Lenovo\Downloads\remotion-finance"
$baseDate = [DateTime]::new(2026, 8, 1, 9, 0, 0)
$commitCount = 0

function Commit($msg, $days, $hours = 0) {
    $date = $baseDate.AddDays($days).AddHours($hours).ToString("yyyy-MM-ddTHH:mm:ss")
    $env:GIT_AUTHOR_DATE = $date
    $env:GIT_COMMITTER_DATE = $date
    git -C $cwd add -A 2>$null
    git -C $cwd commit -m $msg 2>&1 | Out-Null
    $script:commitCount++
    Write-Host "[$($script:commitCount)] $msg"
}

# 2
Add-Content "$cwd\.gitignore" "`n*.log"
Commit "chore: ignore log files" 0 1

# 3
Set-Content "$cwd\README.md" "# remotion-finance`n`nGenerate financial product videos from JSON data using Remotion.`n`n## Setup`n`n``````bash`nnpm install`n```````"
Commit "docs: update README with setup instructions" 0 2

# 4
Add-Content "$cwd\README.md" "`n## Scripts`n`n- ``npm run studio`` — open Remotion Studio`n- ``npm run render`` — render to out/video.mp4"
Commit "docs: add scripts section to README" 1 0

# 5
Set-Content "$cwd\src\theme.ts" 'export const theme = {
  bg: "#0d0d0d",
  white: "#FFFFFF",
  accent: "#E8303C",
  fontFamily: "'"'"'Inter'"'"', '"'"'Helvetica Neue'"'"', Arial, sans-serif",
} as const;'
Commit "style: darken background color" 1 1

# 6
Set-Content "$cwd\src\theme.ts" 'export const theme = {
  bg: "#0d0d0d",
  white: "#FFFFFF",
  accent: "#E8303C",
  muted: "#888888",
  fontFamily: "'"'"'Inter'"'"', '"'"'Helvetica Neue'"'"', Arial, sans-serif",
} as const;'
Commit "style: add muted color to theme" 1 2

# 7
Set-Content "$cwd\data.json" '{
  "produit": "Autocall Euro 2027",
  "taux": "10 %",
  "duree": "20 ans",
  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."
}'
Commit "data: extend legal notice text" 2 0

# 8
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "fontSize: 72,","fontSize: 76," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): increase product name font size" 2 1

# 9
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace 'letterSpacing: "4px"','letterSpacing: "6px"' | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): increase subtitle letter spacing" 2 2

# 10
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "width: 80,","width: 100," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): widen accent bar" 3 0

# 11
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "height: 4,","height: 5," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): thicker accent bar" 3 1

# 12
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "fontSize: 80,","fontSize: 88," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): larger stat value font" 3 2

# 13
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace 'letterSpacing: "3px"','letterSpacing: "4px"' | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): increase label letter spacing" 4 0

# 14
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "gap: 56,","gap: 64," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): increase card gap" 4 1

# 15
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace 'letterSpacing: "5px"','letterSpacing: "6px"' | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): wider header tracking" 4 2

# 16
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace "fontSize: 15,","fontSize: 14," | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): reduce legal text size" 5 0

# 17
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'padding: "18px 60px"','padding: "20px 72px"' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): increase bottom bar padding" 5 1

# 18
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace "opacity: 0.75,","opacity: 0.8," | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): slightly more opaque legal text" 5 2

# 19
(Get-Content "$cwd\src\Root.tsx" -Raw) -replace "durationInFrames={300}","durationInFrames={330}" | Set-Content "$cwd\src\Root.tsx"
Commit "feat(Root): extend video duration to 11s" 6 0

# 20
(Get-Content "$cwd\src\MyComp.tsx" -Raw) -replace "const LEGAL_DURATION = 3 \* FPS;","const LEGAL_DURATION = 4 * FPS;" | Set-Content "$cwd\src\MyComp.tsx"
Commit "feat(MyComp): extend legal notice duration to 4s" 6 1

# 21
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "damping: 14,","damping: 16," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "anim(KeyFigures): increase spring damping" 6 2

# 22
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "stiffness: 120,","stiffness: 130," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "anim(KeyFigures): stiffer spring for snappier pop-in" 7 0

# 23
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "borderRadius: 12,","borderRadius: 16," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): rounder card corners" 7 1

# 24
Set-Content "$cwd\data.json" '{
  "produit": "Autocall Premium 2027",
  "taux": "10,5 %",
  "duree": "20 ans",
  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."
}'
Commit "data: rename product and update taux" 7 2

# 25
Set-Content "$cwd\src\theme.ts" 'export const theme = {
  bg: "#0d0d0d",
  white: "#FFFFFF",
  accent: "#E8303C",
  accentLight: "rgba(232,48,60,0.15)",
  muted: "#888888",
  fontFamily: "'"'"'Inter'"'"', '"'"'Helvetica Neue'"'"', Arial, sans-serif",
} as const;'
Commit "style: add accentLight token to theme" 8 0

# 26
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'backgroundColor: "rgba\(232, 48, 60, 0\.12\)"','backgroundColor: theme.accentLight' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "refactor(LegalNotice): use theme.accentLight" 8 1

# 27
Set-Content "$cwd\CHANGELOG.md" "# Changelog`n`n## [Unreleased]`n- Initial video structure`n- Theme system`n- JSON-driven props`n- Extended durations"
Commit "docs: add CHANGELOG" 8 2

# 28
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace 'padding: "48px 64px"','padding: "52px 72px"' | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): larger card padding" 9 0

# 29
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "opacity: 0.15,","opacity: 0.2," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): more visible divider" 9 1

# 30
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "height: 120,","height: 140," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): taller divider" 9 2

# 31
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "marginBottom: 32,","marginBottom: 40," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): more space below accent bar" 10 0

# 32
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "maxWidth: 1200,","maxWidth: 1400," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): wider text container" 10 1

# 33
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "marginTop: 24,","marginTop: 28," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): more margin above subtitle" 10 2

# 34
Set-Content "$cwd\data.json" '{
  "produit": "Autocall Premium 2028",
  "taux": "10 %",
  "duree": "15 ans",
  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."
}'
Commit "data: update maturity to 2028, duree to 15 ans" 11 0

# 35
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace "fontSize: 28,","fontSize: 30," | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): larger product name" 11 1

# 36
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace "Disponible des maintenant","Souscription ouverte" | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "content(LegalNotice): update CTA text" 11 2

# 37
$pkg = Get-Content "$cwd\package.json" -Raw
$pkg = $pkg -replace '"description": "Automatic financial product video generated from data.json"','"description": "Financial product video generator powered by Remotion"'
Set-Content "$cwd\package.json" $pkg
Commit "chore: update package description" 12 0

# 38
(Get-Content "$cwd\src\Root.tsx" -Raw) -replace "width={1920}","width={1920} {/* Full HD 16:9 */}" | Set-Content "$cwd\src\Root.tsx"
Commit "chore(Root): document resolution comment" 12 1

# 39
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "minWidth: 320,","minWidth: 340," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): wider minimum card width" 12 2

# 40
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "mass: 0.8,","mass: 0.9," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "anim(KeyFigures): slightly heavier spring mass" 13 0

# 41
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace "opacity: 0.8,","opacity: 0.85," | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): increase text opacity" 13 1

# 42
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'lineHeight: 1.5,','lineHeight: 1.6,' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): more line height for readability" 13 2

# 43
(Get-Content "$cwd\src\Root.tsx" -Raw) -replace "durationInFrames={330}","durationInFrames={360}" | Set-Content "$cwd\src\Root.tsx"
Commit "feat(Root): extend video to 12s" 14 0

# 44
(Get-Content "$cwd\src\MyComp.tsx" -Raw) -replace "const KEYS_DURATION = 4 \* FPS;","const KEYS_DURATION = 5 * FPS;" | Set-Content "$cwd\src\MyComp.tsx"
Commit "feat(MyComp): extend KeyFigures segment to 5s" 14 1

# 45
Set-Content "$cwd\data.json" '{
  "produit": "Autocall Premium 2028",
  "taux": "11 %",
  "duree": "15 ans",
  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."
}'
Commit "data: update taux to 11%" 14 2

# 46
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "fontSize: 76,","fontSize: 80," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): bump title to 80px" 15 0

# 47
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace 'fontWeight: 700,','fontWeight: 800,' | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): bolder product name" 15 1

# 48
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace 'fontWeight: 800,','fontWeight: 900,' | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): maximum font weight on stat value" 15 2

# 49
Add-Content "$cwd\CHANGELOG.md" "`n## Notes`n- All animations use Remotion spring/interpolate`n- Props driven from data.json at render time"
Commit "docs: add technical notes to CHANGELOG" 16 0

# 50
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'fontWeight: 600,','fontWeight: 700,' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): bolder available label" 16 1

# 51
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'fontSize: 18,','fontSize: 20,' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): larger CTA font" 16 2

# 52
Set-Content "$cwd\src\theme.ts" 'export const theme = {
  bg: "#111111",
  white: "#FFFFFF",
  accent: "#E8303C",
  accentLight: "rgba(232,48,60,0.15)",
  muted: "#888888",
  fontFamily: "'"'"'Inter'"'"', '"'"'Helvetica Neue'"'"', Arial, sans-serif",
} as const;'
Commit "style: revert bg to #111111 for better contrast" 17 0

# 53
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "gap: 64,","gap: 72," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): wider gap between cards" 17 1

# 54
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "borderRadius: 16,","borderRadius: 20," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): even rounder corners" 17 2

# 55
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace 'border: `\$\{2\}px solid \$\{theme\.accent\}`','border: `3px solid ${theme.accent}`' | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): thicker card border" 18 0

# 56
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "fontWeight: 500,","fontWeight: 600," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): slightly bolder subtitle" 18 1

# 57
Set-Content "$cwd\data.json" '{
  "produit": "Autocall Premium 2028",
  "taux": "11 %",
  "duree": "15 ans",
  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel."
}'
Commit "data: shorten legal notice" 18 2

# 58
(Get-Content "$cwd\src\Root.tsx" -Raw) -replace "durationInFrames={360}","durationInFrames={390}" | Set-Content "$cwd\src\Root.tsx"
Commit "feat(Root): extend video to 13s" 19 0

# 59
(Get-Content "$cwd\src\MyComp.tsx" -Raw) -replace "const INTRO_START = 0;","const INTRO_START = 0; // frame 0" | Set-Content "$cwd\src\MyComp.tsx"
Commit "chore(MyComp): add frame comment to timing constants" 19 1

# 60
Add-Content "$cwd\README.md" "`n## Data format`n`nEdit \`data.json\` to customize the video content."
Commit "docs: document data.json format in README" 19 2

# 61
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'gap: 20,','gap: 24,' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): more spacing in central content" 20 0

# 62
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'width: 60,','width: 72,' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): wider decorative bar" 20 1

# 63
(Get-Content "$cwd\src\components\LegalNotice.tsx" -Raw) -replace 'height: 3,','height: 4,' | Set-Content "$cwd\src\components\LegalNotice.tsx"
Commit "style(LegalNotice): thicker decorative bar" 20 2

# 64
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "fontWeight: 400,","fontWeight: 300," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): lighter label weight" 21 0

# 65
(Get-Content "$cwd\src\components\KeyFigures.tsx" -Raw) -replace "marginTop: 16,","marginTop: 20," | Set-Content "$cwd\src\components\KeyFigures.tsx"
Commit "style(KeyFigures): more space between value and label" 21 1

# 66
Set-Content "$cwd\data.json" '{
  "produit": "Autocall Premium 2028",
  "taux": "11 %",
  "duree": "15 ans",
  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel. Investissement soumis aux risques de marche."
}'
Commit "data: add market risk disclaimer" 21 2

# 67
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace "fontSize: 22,","fontSize: 24," | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): larger subtitle font" 22 0

# 68
(Get-Content "$cwd\src\components\Intro.tsx" -Raw) -replace 'letterSpacing: "6px"','letterSpacing: "8px"' | Set-Content "$cwd\src\components\Intro.tsx"
Commit "style(Intro): wider subtitle tracking" 22 1

# 69
(Get-Content "$cwd\src\Root.tsx" -Raw) -replace "durationInFrames={390}","durationInFrames={420}" | Set-Content "$cwd\src\Root.tsx"
Commit "feat(Root): final duration 14s" 22 2

# 70
Add-Content "$cwd\CHANGELOG.md" "`n## v1.0.0`n- Complete animation pipeline`n- Theme tokens finalized`n- Data-driven rendering confirmed"
Commit "docs: mark v1.0.0 in CHANGELOG" 23 0

Write-Host "`nTotal commits created: $commitCount"
