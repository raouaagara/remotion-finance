import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, Easing } from "remotion";
import { theme } from "../theme";

interface IntroProps {
  produit: string;
}

export const Intro: React.FC<IntroProps> = ({ produit }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Fade in over the first 20 frames (~0.67 s)
  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  // Slide up slightly as it fades in
  const translateY = interpolate(frame, [0, 20], [30, 0], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        backgroundColor: theme.bg,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: theme.fontFamily,
      }}
    >
      {/* Accent bar */}
      <div
        style={{
          width: 80,
          height: 4,
          backgroundColor: theme.accent,
          marginBottom: 32,
          opacity,
          transform: `translateY(${translateY}px)`,
        }}
      />

      {/* Product name */}
      <h1
        style={{
          color: theme.white,
          fontSize: 76,
          fontWeight: 700,
          letterSpacing: "-1px",
          margin: 0,
          textAlign: "center",
          maxWidth: 1200,
          opacity,
          transform: `translateY(${translateY}px)`,
        }}
      >
        {produit}
      </h1>

      {/* Subtitle tag */}
      <p
        style={{
          color: theme.accent,
          fontSize: 22,
          fontWeight: 500,
          letterSpacing: "6px",
          textTransform: "uppercase",
          marginTop: 24,
          opacity,
          transform: `translateY(${translateY}px)`,
        }}
      >
        Produit Structuré
      </p>
    </div>
  );
};
