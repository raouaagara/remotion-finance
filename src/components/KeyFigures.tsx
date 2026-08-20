import React from "react";
import { useCurrentFrame, useVideoConfig, spring, interpolate, Easing } from "remotion";
import { theme } from "../theme";

interface KeyFiguresProps {
  taux: string;
  duree: string;
}

interface StatCardProps {
  label: string;
  value: string;
  delay: number; // frame delay before animation starts
}

const StatCard: React.FC<StatCardProps> = ({ label, value, delay }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const localFrame = Math.max(0, frame - delay);

  const scale = spring({
    frame: localFrame,
    fps,
    config: {
      damping: 16,
      stiffness: 130,
      mass: 0.9,
    },
  });

  const opacity = interpolate(localFrame, [0, 10], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "52px 72px",
        border: `2px solid ${theme.accent}`,
        borderRadius: 20,
        minWidth: 340,
        opacity,
        transform: `scale(${scale})`,
      }}
    >
      <span
        style={{
          color: theme.accent,
          fontSize: 88,
          fontWeight: 900,
          lineHeight: 1,
          letterSpacing: "-2px",
        }}
      >
        {value}
      </span>
      <span
        style={{
          color: theme.white,
          fontSize: 20,
          fontWeight: 300,
          letterSpacing: "4px",
          textTransform: "uppercase",
          marginTop: 16,
          opacity: 0.7,
        }}
      >
        {label}
      </span>
    </div>
  );
};

export const KeyFigures: React.FC<KeyFiguresProps> = ({ taux, duree }) => {
  const frame = useCurrentFrame();

  // Header fades in immediately (frame 0 of this sequence)
  const headerOpacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: "clamp",
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
        gap: 72,
      }}
    >
      <p
        style={{
          color: theme.white,
          fontSize: 20,
          fontWeight: 500,
          letterSpacing: "6px",
          textTransform: "uppercase",
          margin: 0,
          opacity: headerOpacity,
        }}
      >
        Chiffres Clés
      </p>

      <div style={{ display: "flex", gap: 72, alignItems: "center" }}>
        {/* Taux card appears at frame 10, durée at frame 25 */}
        <StatCard label="Rendement annuel" value={taux} delay={10} />
        <div
          style={{
            width: 1,
            height: 140,
            backgroundColor: theme.white,
            opacity: 0.2,
          }}
        />
        <StatCard label="Durée" value={duree} delay={25} />
      </div>
    </div>
  );
};
