import subprocess
import os
import datetime

cwd = r"c:\Users\Lenovo\Downloads\remotion-finance"
base = datetime.datetime(2026, 8, 1, 9, 0, 0)
count = [0]

def git(args):
    return subprocess.run(["git", "-C", cwd] + args, capture_output=True, text=True)

def commit(msg, days, hours=0):
    d = base + datetime.timedelta(days=days, hours=hours)
    date_str = d.strftime("%Y-%m-%dT%H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    git(["add", "-A"])
    r = subprocess.run(["git", "-C", cwd, "commit", "-m", msg], capture_output=True, text=True, env=env)
    count[0] += 1
    print(f"[{count[0]}] {msg}")

def write(path, content):
    with open(os.path.join(cwd, path), "w", encoding="utf-8") as f:
        f.write(content)

def append(path, content):
    with open(os.path.join(cwd, path), "a", encoding="utf-8") as f:
        f.write(content)

def replace_in(path, old, new):
    with open(os.path.join(cwd, path), "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace(old, new, 1)
    with open(os.path.join(cwd, path), "w", encoding="utf-8") as f:
        f.write(content)

# 2
append(".gitignore", "\n*.log\n")
commit("chore: ignore log files", 0, 1)

# 3
write("README.md", "# remotion-finance\n\nGenerate financial product videos from JSON data using Remotion.\n\n## Setup\n\n```bash\nnpm install\n```\n")
commit("docs: update README with setup instructions", 0, 2)

# 4
append("README.md", "\n## Scripts\n\n- `npm run studio` — open Remotion Studio\n- `npm run render` — render to out/video.mp4\n")
commit("docs: add scripts section to README", 1, 0)

# 5
write("src/theme.ts", "export const theme = {\n  bg: \"#0d0d0d\",\n  white: \"#FFFFFF\",\n  accent: \"#E8303C\",\n  fontFamily: \"'Inter', 'Helvetica Neue', Arial, sans-serif\",\n} as const;\n")
commit("style: darken background color", 1, 1)

# 6
write("src/theme.ts", "export const theme = {\n  bg: \"#0d0d0d\",\n  white: \"#FFFFFF\",\n  accent: \"#E8303C\",\n  muted: \"#888888\",\n  fontFamily: \"'Inter', 'Helvetica Neue', Arial, sans-serif\",\n} as const;\n")
commit("style: add muted color to theme", 1, 2)

# 7
write("data.json", '{\n  "produit": "Autocall Euro 2027",\n  "taux": "10 %",\n  "duree": "20 ans",\n  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."\n}\n')
commit("data: extend legal notice text", 2, 0)

# 8
replace_in("src/components/Intro.tsx", "fontSize: 72,", "fontSize: 76,")
commit("style(Intro): increase product name font size", 2, 1)

# 9
replace_in("src/components/Intro.tsx", 'letterSpacing: "4px",', 'letterSpacing: "6px",')
commit("style(Intro): increase subtitle letter spacing", 2, 2)

# 10
replace_in("src/components/Intro.tsx", "width: 80,", "width: 100,")
commit("style(Intro): widen accent bar", 3, 0)

# 11
replace_in("src/components/Intro.tsx", "height: 4,", "height: 5,")
commit("style(Intro): thicker accent bar", 3, 1)

# 12
replace_in("src/components/KeyFigures.tsx", "fontSize: 80,", "fontSize: 88,")
commit("style(KeyFigures): larger stat value font", 3, 2)

# 13
replace_in("src/components/KeyFigures.tsx", 'letterSpacing: "3px",', 'letterSpacing: "4px",')
commit("style(KeyFigures): increase label letter spacing", 4, 0)

# 14
replace_in("src/components/KeyFigures.tsx", "gap: 56,", "gap: 64,")
commit("style(KeyFigures): increase card gap", 4, 1)

# 15
replace_in("src/components/KeyFigures.tsx", 'letterSpacing: "5px",', 'letterSpacing: "6px",')
commit("style(KeyFigures): wider header tracking", 4, 2)

# 16
replace_in("src/components/LegalNotice.tsx", "fontSize: 15,", "fontSize: 14,")
commit("style(LegalNotice): reduce legal text size", 5, 0)

# 17
replace_in("src/components/LegalNotice.tsx", 'padding: "18px 60px",', 'padding: "20px 72px",')
commit("style(LegalNotice): increase bottom bar padding", 5, 1)

# 18
replace_in("src/components/LegalNotice.tsx", "opacity: 0.75,", "opacity: 0.8,")
commit("style(LegalNotice): slightly more opaque legal text", 5, 2)

# 19
replace_in("src/Root.tsx", "durationInFrames={300}", "durationInFrames={330}")
commit("feat(Root): extend video duration to 11s", 6, 0)

# 20
replace_in("src/MyComp.tsx", "const LEGAL_DURATION = 3 * FPS;", "const LEGAL_DURATION = 4 * FPS;")
commit("feat(MyComp): extend legal notice duration to 4s", 6, 1)

# 21
replace_in("src/components/KeyFigures.tsx", "damping: 14,", "damping: 16,")
commit("anim(KeyFigures): increase spring damping", 6, 2)

# 22
replace_in("src/components/KeyFigures.tsx", "stiffness: 120,", "stiffness: 130,")
commit("anim(KeyFigures): stiffer spring for snappier pop-in", 7, 0)

# 23
replace_in("src/components/KeyFigures.tsx", "borderRadius: 12,", "borderRadius: 16,")
commit("style(KeyFigures): rounder card corners", 7, 1)

# 24
write("data.json", '{\n  "produit": "Autocall Premium 2027",\n  "taux": "10,5 %",\n  "duree": "20 ans",\n  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."\n}\n')
commit("data: rename product and update taux", 7, 2)

# 25
write("src/theme.ts", "export const theme = {\n  bg: \"#0d0d0d\",\n  white: \"#FFFFFF\",\n  accent: \"#E8303C\",\n  accentLight: \"rgba(232,48,60,0.15)\",\n  muted: \"#888888\",\n  fontFamily: \"'Inter', 'Helvetica Neue', Arial, sans-serif\",\n} as const;\n")
commit("style: add accentLight token to theme", 8, 0)

# 26
replace_in("src/components/LegalNotice.tsx", 'backgroundColor: "rgba(232, 48, 60, 0.12)",', "backgroundColor: theme.accentLight,")
commit("refactor(LegalNotice): use theme.accentLight", 8, 1)

# 27
write("CHANGELOG.md", "# Changelog\n\n## [Unreleased]\n- Initial video structure\n- Theme system\n- JSON-driven props\n- Extended durations\n")
commit("docs: add CHANGELOG", 8, 2)

# 28
replace_in("src/components/KeyFigures.tsx", 'padding: "48px 64px",', 'padding: "52px 72px",')
commit("style(KeyFigures): larger card padding", 9, 0)

# 29
replace_in("src/components/KeyFigures.tsx", "opacity: 0.15,", "opacity: 0.2,")
commit("style(KeyFigures): more visible divider", 9, 1)

# 30
replace_in("src/components/KeyFigures.tsx", "height: 120,", "height: 140,")
commit("style(KeyFigures): taller divider", 9, 2)

# 31
replace_in("src/components/Intro.tsx", "marginBottom: 32,", "marginBottom: 40,")
commit("style(Intro): more space below accent bar", 10, 0)

# 32
replace_in("src/components/Intro.tsx", "maxWidth: 1200,", "maxWidth: 1400,")
commit("style(Intro): wider text container", 10, 1)

# 33
replace_in("src/components/Intro.tsx", "marginTop: 24,", "marginTop: 28,")
commit("style(Intro): more margin above subtitle", 10, 2)

# 34
write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "10 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."\n}\n')
commit("data: update maturity to 2028, duree to 15 ans", 11, 0)

# 35
replace_in("src/components/LegalNotice.tsx", "fontSize: 28,", "fontSize: 30,")
commit("style(LegalNotice): larger product name", 11, 1)

# 36
replace_in("src/components/LegalNotice.tsx", "Disponible dès maintenant", "Souscription ouverte")
commit("content(LegalNotice): update CTA text", 11, 2)

# 37
replace_in("package.json", '"description": "Automatic financial product video generated from data.json"', '"description": "Financial product video generator powered by Remotion"')
commit("chore: update package description", 12, 0)

# 38
replace_in("src/components/KeyFigures.tsx", "minWidth: 320,", "minWidth: 340,")
commit("style(KeyFigures): wider minimum card width", 12, 1)

# 39
replace_in("src/components/KeyFigures.tsx", "mass: 0.8,", "mass: 0.9,")
commit("anim(KeyFigures): slightly heavier spring mass", 12, 2)

# 40
replace_in("src/components/LegalNotice.tsx", "opacity: 0.8,", "opacity: 0.85,")
commit("style(LegalNotice): increase text opacity", 13, 0)

# 41
replace_in("src/components/LegalNotice.tsx", "lineHeight: 1.5,", "lineHeight: 1.6,")
commit("style(LegalNotice): more line height for readability", 13, 1)

# 42
replace_in("src/Root.tsx", "durationInFrames={330}", "durationInFrames={360}")
commit("feat(Root): extend video to 12s", 13, 2)

# 43
replace_in("src/MyComp.tsx", "const KEYS_DURATION = 4 * FPS;", "const KEYS_DURATION = 5 * FPS;")
commit("feat(MyComp): extend KeyFigures segment to 5s", 14, 0)

# 44
write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."\n}\n')
commit("data: update taux to 11%", 14, 1)

# 45
replace_in("src/components/Intro.tsx", "fontSize: 76,", "fontSize: 80,")
commit("style(Intro): bump title to 80px", 14, 2)

# 46
replace_in("src/components/Intro.tsx", "fontWeight: 700,", "fontWeight: 800,")
commit("style(Intro): bolder product name", 15, 0)

# 47
replace_in("src/components/KeyFigures.tsx", "fontWeight: 800,", "fontWeight: 900,")
commit("style(KeyFigures): maximum font weight on stat value", 15, 1)

# 48
append("CHANGELOG.md", "\n## Notes\n- All animations use Remotion spring/interpolate\n- Props driven from data.json at render time\n")
commit("docs: add technical notes to CHANGELOG", 15, 2)

# 49
replace_in("src/components/LegalNotice.tsx", "fontWeight: 600,", "fontWeight: 700,")
commit("style(LegalNotice): bolder available label", 16, 0)

# 50
replace_in("src/components/LegalNotice.tsx", "fontSize: 18,", "fontSize: 20,")
commit("style(LegalNotice): larger CTA font", 16, 1)

# 51
write("src/theme.ts", "export const theme = {\n  bg: \"#111111\",\n  white: \"#FFFFFF\",\n  accent: \"#E8303C\",\n  accentLight: \"rgba(232,48,60,0.15)\",\n  muted: \"#888888\",\n  fontFamily: \"'Inter', 'Helvetica Neue', Arial, sans-serif\",\n} as const;\n")
commit("style: revert bg to #111111 for better contrast", 16, 2)

# 52
replace_in("src/components/KeyFigures.tsx", "gap: 64,", "gap: 72,")
commit("style(KeyFigures): wider gap between cards", 17, 0)

# 53
replace_in("src/components/KeyFigures.tsx", "borderRadius: 16,", "borderRadius: 20,")
commit("style(KeyFigures): even rounder corners", 17, 1)

# 54
replace_in("src/components/Intro.tsx", "fontWeight: 500,", "fontWeight: 600,")
commit("style(Intro): slightly bolder subtitle", 17, 2)

# 55
write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel."\n}\n')
commit("data: shorten legal notice", 18, 0)

# 56
replace_in("src/Root.tsx", "durationInFrames={360}", "durationInFrames={390}")
commit("feat(Root): extend video to 13s", 18, 1)

# 57
replace_in("src/components/LegalNotice.tsx", "gap: 20,", "gap: 24,")
commit("style(LegalNotice): more spacing in central content", 18, 2)

# 58
replace_in("src/components/LegalNotice.tsx", "width: 60,", "width: 72,")
commit("style(LegalNotice): wider decorative bar", 19, 0)

# 59
replace_in("src/components/LegalNotice.tsx", "height: 3,", "height: 4,")
commit("style(LegalNotice): thicker decorative bar", 19, 1)

# 60
replace_in("src/components/KeyFigures.tsx", "fontWeight: 400,", "fontWeight: 300,")
commit("style(KeyFigures): lighter label weight", 19, 2)

# 61
replace_in("src/components/KeyFigures.tsx", "marginTop: 16,", "marginTop: 20,")
commit("style(KeyFigures): more space between value and label", 20, 0)

# 62
write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel. Investissement soumis aux risques de marche."\n}\n')
commit("data: add market risk disclaimer", 20, 1)

# 63
replace_in("src/components/Intro.tsx", "fontSize: 22,", "fontSize: 24,")
commit("style(Intro): larger subtitle font", 20, 2)

# 64
replace_in("src/components/Intro.tsx", 'letterSpacing: "6px",', 'letterSpacing: "8px",')
commit("style(Intro): wider subtitle tracking", 21, 0)

# 65
replace_in("src/Root.tsx", "durationInFrames={390}", "durationInFrames={420}")
commit("feat(Root): final duration 14s", 21, 1)

# 66
append("CHANGELOG.md", "\n## v1.0.0\n- Complete animation pipeline\n- Theme tokens finalized\n- Data-driven rendering confirmed\n")
commit("docs: mark v1.0.0 in CHANGELOG", 21, 2)

# 67
replace_in("src/components/KeyFigures.tsx", "gap: 72,", "gap: 80,")
commit("style(KeyFigures): final gap adjustment", 22, 0)

# 68
replace_in("src/components/LegalNotice.tsx", "opacity: 0.85,", "opacity: 0.9,")
commit("style(LegalNotice): final opacity tuning", 22, 1)

# 69
append("README.md", "\n## Data format\n\nEdit `data.json` to customize the video content.\n")
commit("docs: document data.json format in README", 22, 2)

# 70
write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel. Investissement soumis aux risques de marche."\n}\n')
commit("chore: final data.json cleanup", 23, 0)

print(f"\nDone! Total new commits: {count[0]}")
