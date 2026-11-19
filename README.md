# remotion-finance

Génération automatique d'une vidéo de présentation d'un produit financier à partir d'un fichier JSON, avec [Remotion](https://www.remotion.dev/).

## Prérequis

- Node.js ≥ 16
- npm ≥ 7

## Installation

```bash
npm install
```

## Personnaliser la vidéo

Éditez uniquement **`data.json`** à la racine du projet :

```json
{
  "produit": "Autocall Euro 2027",
  "taux": "7,5 %",
  "duree": "5 ans",
  "mentionLegale": "Produit risqué, capital non garanti."
}
```

Aucune modification du code n'est nécessaire.

## Lancer le Studio (prévisualisation interactive)

```bash
npm run studio
```

Ouvre le Remotion Studio sur `http://localhost:3000`. Vous pouvez scrubber la timeline et voir les animations en temps réel.

## Générer la vidéo

```bash
npm run render
```

Équivalent à :

```bash
npx remotion render MyComp out/video.mp4 --props=data.json
```

Le fichier `out/video.mp4` est créé (1920 × 1080, 30 fps, 10 secondes).

## Structure du projet

```
remotion-finance/
├── data.json              ← seul fichier à modifier pour changer la vidéo
├── src/
│   ├── index.ts           ← point d'entrée Remotion (registerRoot)
│   ├── Root.tsx           ← déclare la Composition (id, fps, taille)
│   ├── MyComp.tsx         ← orchestre les 3 séquences via <Sequence>
│   ├── types.ts           ← interface ProductData
│   ├── theme.ts           ← couleurs et police
│   └── components/
│       ├── Intro.tsx      ← 0–3 s : nom du produit, fondu
│       ├── KeyFigures.tsx ← 3–7 s : taux & durée, animation spring
│       └── LegalNotice.tsx← 7–10 s : mention légale en bas d'écran
├── out/                   ← vidéo rendue (générée, non versionnée)
└── tsconfig.json
```

## Séquences animées

| Séquence | Durée | Animation |
|---|---|---|
| **Intro** | 0 → 3 s | Fondu + glissement vertical du nom produit |
| **Chiffres clés** | 3 → 7 s | Spring scale sur chaque carte (taux puis durée) |
| **Mention légale** | 7 → 10 s | Slide-up de la barre légale depuis le bas |

## Design

- Fond : `#111111`
- Texte : `#FFFFFF`
- Accent : `#E8303C` (rouge)
- Police : Inter / Helvetica Neue / Arial
