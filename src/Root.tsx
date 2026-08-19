import React from "react";
import { Composition } from "remotion";
import { MyComp } from "./MyComp";
import type { ProductData } from "./types";

// Default props — used in Remotion Studio only.
// At render time these are replaced by --props=data.json.
const defaultProps: ProductData = {
  produit: "Autocall Euro 2027",
  taux: "7,5 %",
  duree: "5 ans",
  mentionLegale: "Produit risqué, capital non garanti.",
};

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="MyComp"
      component={MyComp}
      durationInFrames={390} // 10 s × 30 fps
      fps={30}
      width={1920}
      height={1080}
      defaultProps={defaultProps}
    />
  );
};
