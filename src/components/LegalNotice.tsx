import React from "react";
import { useCurrentFrame, interpolate, Easing } from "remotion";
import { theme } from "../theme";

interface LegalNoticeProps {
  mentionLegale: string;
  produit: string;
}

export const LegalNotice: React.FC<LegalNoticeProps> = ({ mentionLegale, produit }) => {
  const frame = useCurrentFrame();

  // Main content fades in
  const contentOpacity = interpolate(frame, [0, 18], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });

  // Legal bar slides up from the bottom
  const legalY = interpolate(frame, [8, 28], [60, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const legalOpacity = interpolate(frame, [8, 28], [0, 1], {
    extrapolateLeft: "clamp",
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
        position: "relative",
      }}
    >
      {/* Central content */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 20,
          opacity: contentOpacity,
        }}
      >
        <div
          style={{
            width: 60,
            height: 3,
            backgroundColor: theme.accent,
          }}
        />
        <p
          style={{
            color: theme.white,
            fontSize: 28,
            fontWeight: 300,
            letterSpacing: "1px",
            margin: 0,
          }}
        >
          {produit}
        </p>
        <p
          style={{
            color: theme.accent,
            fontSize: 18,
            fontWeight: 600,
            letterSpacing: "4px",
            textTransform: "uppercase",
            margin: 0,
          }}
        >
          Disponible dès maintenant
        </p>
      </div>

      {/* Legal notice bar — anchored at the bottom */}
      <div
        style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          right: 0,
          backgroundColor: theme.accentLight,
          borderTop: `1px solid ${theme.accent}`,
          padding: "20px 72px",
          opacity: legalOpacity,
          transform: `translateY(${legalY}px)`,
        }}
      >
        <p
          style={{
            color: theme.white,
            fontSize: 14,
            fontWeight: 400,
            margin: 0,
            opacity: 0.8,
            lineHeight: 1.5,
          }}
        >
          ⚠️ {mentionLegale}
        </p>
      </div>
    </div>
  );
};
