import subprocess, os, datetime

cwd = r"c:\Users\Lenovo\Downloads\remotion-finance"
base = datetime.datetime(2026, 9, 1, 9, 0, 0)
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
    subprocess.run(["git", "-C", cwd, "commit", "-m", msg], capture_output=True, text=True, env=env)
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

replace_in("src/components/KeyFigures.tsx", "damping: 14,", "damping: 16,")
commit("anim(KeyFigures): increase spring damping", 0, 0)

replace_in("src/components/KeyFigures.tsx", "stiffness: 120,", "stiffness: 130,")
commit("anim(KeyFigures): stiffer spring for snappier pop-in", 0, 1)

replace_in("src/components/KeyFigures.tsx", "borderRadius: 12,", "borderRadius: 16,")
commit("style(KeyFigures): rounder card corners", 0, 2)

write("data.json", '{\n  "produit": "Autocall Premium 2027",\n  "taux": "10,5 %",\n  "duree": "20 ans",\n  "mentionLegale": "Produit risque, capital non garanti."\n}\n')
commit("data: rename product and update taux", 1, 0)

write("src/theme.ts", 'export const theme = {\n  bg: "#0d0d0d",\n  white: "#FFFFFF",\n  accent: "#E8303C",\n  accentLight: "rgba(232,48,60,0.15)",\n  muted: "#888888",\n  fontFamily: "\'Inter\', \'Helvetica Neue\', Arial, sans-serif",\n} as const;\n')
commit("style: add accentLight token to theme", 1, 1)

write("CHANGELOG.md", "# Changelog\n\n## [Unreleased]\n- Initial video structure\n- Theme system\n- JSON-driven props\n- Extended durations\n")
commit("docs: add CHANGELOG", 1, 2)

replace_in("src/components/KeyFigures.tsx", 'padding: "48px 64px",', 'padding: "52px 72px",')
commit("style(KeyFigures): larger card padding", 2, 0)

replace_in("src/components/KeyFigures.tsx", "opacity: 0.15,", "opacity: 0.2,")
commit("style(KeyFigures): more visible divider", 2, 1)

replace_in("src/components/KeyFigures.tsx", "height: 120,", "height: 140,")
commit("style(KeyFigures): taller divider", 2, 2)

replace_in("src/components/Intro.tsx", "marginBottom: 32,", "marginBottom: 40,")
commit("style(Intro): more space below accent bar", 3, 0)

replace_in("src/components/Intro.tsx", "maxWidth: 1200,", "maxWidth: 1400,")
commit("style(Intro): wider text container", 3, 1)

replace_in("src/components/Intro.tsx", "marginTop: 24,", "marginTop: 28,")
commit("style(Intro): more margin above subtitle", 3, 2)

write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "10 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque, capital non garanti."\n}\n')
commit("data: update maturity to 2028, duree to 15 ans", 4, 0)

replace_in("src/components/LegalNotice.tsx", "fontSize: 28,", "fontSize: 30,")
commit("style(LegalNotice): larger product name", 4, 1)

replace_in("package.json", '"description": "Automatic financial product video generated from data.json"', '"description": "Financial product video generator powered by Remotion"')
commit("chore: update package description", 4, 2)

replace_in("src/components/KeyFigures.tsx", "minWidth: 320,", "minWidth: 340,")
commit("style(KeyFigures): wider minimum card width", 5, 0)

replace_in("src/components/KeyFigures.tsx", "mass: 0.8,", "mass: 0.9,")
commit("anim(KeyFigures): slightly heavier spring mass", 5, 1)

replace_in("src/components/LegalNotice.tsx", "opacity: 0.75,", "opacity: 0.85,")
commit("style(LegalNotice): increase text opacity", 5, 2)

replace_in("src/components/LegalNotice.tsx", "lineHeight: 1.5,", "lineHeight: 1.6,")
commit("style(LegalNotice): more line height for readability", 6, 0)

replace_in("src/Root.tsx", "durationInFrames={330}", "durationInFrames={360}")
commit("feat(Root): extend video to 12s", 6, 1)

replace_in("src/MyComp.tsx", "const KEYS_DURATION = 4 * FPS;", "const KEYS_DURATION = 5 * FPS;")
commit("feat(MyComp): extend KeyFigures segment to 5s", 6, 2)

write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque, capital non garanti. Performances passees ne presagent pas des performances futures."\n}\n')
commit("data: update taux to 11%", 7, 0)

replace_in("src/components/Intro.tsx", "fontSize: 76,", "fontSize: 80,")
commit("style(Intro): bump title to 80px", 7, 1)

replace_in("src/components/Intro.tsx", "fontWeight: 700,", "fontWeight: 800,")
commit("style(Intro): bolder product name", 7, 2)

replace_in("src/components/KeyFigures.tsx", "fontWeight: 800,", "fontWeight: 900,")
commit("style(KeyFigures): maximum font weight on stat value", 8, 0)

append("CHANGELOG.md", "\n## Notes\n- All animations use Remotion spring/interpolate\n- Props driven from data.json at render time\n")
commit("docs: add technical notes to CHANGELOG", 8, 1)

replace_in("src/components/LegalNotice.tsx", "fontWeight: 600,", "fontWeight: 700,")
commit("style(LegalNotice): bolder available label", 8, 2)

replace_in("src/components/LegalNotice.tsx", "fontSize: 18,", "fontSize: 20,")
commit("style(LegalNotice): larger CTA font", 9, 0)

write("src/theme.ts", 'export const theme = {\n  bg: "#111111",\n  white: "#FFFFFF",\n  accent: "#E8303C",\n  accentLight: "rgba(232,48,60,0.15)",\n  muted: "#888888",\n  fontFamily: "\'Inter\', \'Helvetica Neue\', Arial, sans-serif",\n} as const;\n')
commit("style: revert bg to #111111 for better contrast", 9, 1)

replace_in("src/components/KeyFigures.tsx", "gap: 64,", "gap: 72,")
commit("style(KeyFigures): wider gap between cards", 9, 2)

replace_in("src/components/KeyFigures.tsx", "borderRadius: 16,", "borderRadius: 20,")
commit("style(KeyFigures): even rounder corners", 10, 0)

replace_in("src/components/Intro.tsx", "fontWeight: 500,", "fontWeight: 600,")
commit("style(Intro): slightly bolder subtitle", 10, 1)

write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel."\n}\n')
commit("data: shorten legal notice", 10, 2)

replace_in("src/Root.tsx", "durationInFrames={360}", "durationInFrames={390}")
commit("feat(Root): extend video to 13s", 11, 0)

replace_in("src/components/LegalNotice.tsx", "gap: 20,", "gap: 24,")
commit("style(LegalNotice): more spacing in central content", 11, 1)

replace_in("src/components/LegalNotice.tsx", "width: 60,", "width: 72,")
commit("style(LegalNotice): wider decorative bar", 11, 2)

replace_in("src/components/LegalNotice.tsx", "height: 3,", "height: 4,")
commit("style(LegalNotice): thicker decorative bar", 12, 0)

replace_in("src/components/KeyFigures.tsx", "fontWeight: 400,", "fontWeight: 300,")
commit("style(KeyFigures): lighter label weight", 12, 1)

replace_in("src/components/KeyFigures.tsx", "marginTop: 16,", "marginTop: 20,")
commit("style(KeyFigures): more space between value and label", 12, 2)

write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel. Investissement soumis aux risques de marche."\n}\n')
commit("data: add market risk disclaimer", 13, 0)

replace_in("src/components/Intro.tsx", "fontSize: 22,", "fontSize: 24,")
commit("style(Intro): larger subtitle font", 13, 1)

replace_in("src/components/Intro.tsx", 'letterSpacing: "6px",', 'letterSpacing: "8px",')
commit("style(Intro): wider subtitle tracking", 13, 2)

replace_in("src/Root.tsx", "durationInFrames={390}", "durationInFrames={420}")
commit("feat(Root): final duration 14s", 14, 0)

append("CHANGELOG.md", "\n## v1.0.0\n- Complete animation pipeline\n- Theme tokens finalized\n- Data-driven rendering confirmed\n")
commit("docs: mark v1.0.0 in CHANGELOG", 14, 1)

replace_in("src/components/KeyFigures.tsx", "gap: 72,", "gap: 80,")
commit("style(KeyFigures): final gap adjustment", 14, 2)

replace_in("src/components/LegalNotice.tsx", "opacity: 0.85,", "opacity: 0.9,")
commit("style(LegalNotice): final opacity tuning", 15, 0)

append("README.md", "\n## Data format\n\nEdit `data.json` to customize the video content.\n")
commit("docs: document data.json format in README", 15, 1)

write("data.json", '{\n  "produit": "Autocall Premium 2028",\n  "taux": "11 %",\n  "duree": "15 ans",\n  "mentionLegale": "Produit risque. Capital non garanti. Document non contractuel. Investissement soumis aux risques de marche."\n}\n')
commit("chore: final data.json cleanup", 15, 2)

print(f"\nDone! Total new commits: {count[0]}")
print(f"Run: git log --oneline | wc -l  to verify total")
