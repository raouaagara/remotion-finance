# remotion-finance

A data-driven financial product video generator built with [Remotion](https://www.remotion.dev/). Generate professional animated videos from a simple JSON file — no video editing required.

## Preview

The video is composed of three animated scenes:

| Scene | Duration | Description |
|-------|----------|-------------|
| Intro | 3.5s | Product name with fade-in and slide-up animation |
| Key Figures | 5s | Animated stat cards (yield rate, duration) |
| Legal Notice | 4s | Disclaimer bar with product CTA |

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) v18+
- npm

### Installation

```bash
npm install
```

## Usage

### Open Remotion Studio (live preview)

```bash
npm run studio
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

### Render the video

```bash
npm run render
```

The output video is saved to `out/video.mp4`.

## Customize

Edit `data.json` to change the video content:

```json
{
  "produit": "Autocall Premium 2028",
  "taux": "11 %",
  "duree": "15 ans",
  "mentionLegale": "Risk product. Capital not guaranteed."
}
```

| Field | Description |
|-------|-------------|
| `produit` | Product name displayed in the intro and legal scenes |
| `taux` | Annual yield rate shown in the key figures scene |
| `duree` | Product duration shown in the key figures scene |
| `mentionLegale` | Legal disclaimer text shown at the bottom |

After editing `data.json`, re-run `npm run render` to generate the updated video.

## Project Structure

```
remotion-finance/
├── src/
│   ├── components/
│   │   ├── Intro.tsx          # Opening scene
│   │   ├── KeyFigures.tsx     # Animated stat cards
│   │   └── LegalNotice.tsx    # Disclaimer scene
│   ├── MyComp.tsx             # Main composition with timing
│   ├── Root.tsx               # Remotion root (composition config)
│   ├── theme.ts               # Design tokens (colors, fonts)
│   └── types.ts               # TypeScript interfaces
├── data.json                  # Video content (edit this)
├── out/                       # Rendered video output (git-ignored)
└── package.json
```

## Tech Stack

- [Remotion 4](https://www.remotion.dev/) — React-based video framework
- [React 18](https://react.dev/)
- [TypeScript 5](https://www.typescriptlang.org/)

## License

MIT
