import React from "react";
import { Sequence, useVideoConfig } from "remotion";
import { Intro } from "./components/Intro";
import { KeyFigures } from "./components/KeyFigures";
import { LegalNotice } from "./components/LegalNotice";
import { theme } from "./theme";
import type { ProductData } from "./types";

// Timing constants (frames at 30 fps)
const FPS = 30;
const INTRO_START = 0;           //  0 s
const INTRO_DURATION = 3 * FPS;  //  3 s  → frames 0–89
const KEYS_START = 3 * FPS;      //  3 s
const KEYS_DURATION = 4 * FPS;   //  4 s  → frames 90–209
const LEGAL_START = 7 * FPS;     //  7 s
const LEGAL_DURATION = 4 * FPS;  //  3 s  → frames 210–299

export const MyComp: React.FC<ProductData> = ({
  produit,
  taux,
  duree,
  mentionLegale,
}) => {
  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        backgroundColor: theme.bg,
        fontFamily: theme.fontFamily,
        overflow: "hidden",
      }}
    >
      <Sequence from={INTRO_START} durationInFrames={INTRO_DURATION} name="Intro">
        <Intro produit={produit} />
      </Sequence>

      <Sequence from={KEYS_START} durationInFrames={KEYS_DURATION} name="KeyFigures">
        <KeyFigures taux={taux} duree={duree} />
      </Sequence>

      <Sequence from={LEGAL_START} durationInFrames={LEGAL_DURATION} name="LegalNotice">
        <LegalNotice mentionLegale={mentionLegale} produit={produit} />
      </Sequence>
    </div>
  );
};
