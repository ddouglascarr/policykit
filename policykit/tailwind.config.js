/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-nunito)"],
      },
    },
    colors: {
      white: "#FFFFFF",
      background: {
        light: "#F8F9FA",
        focus: "#F1F4F6",
      },
      grey: {
        darkest: "#191F24",
        dark: "#52677A",
        DEFAULT: "#B2BBC3",
        light: "#D2D2D2",
      },
      primary: {
        darkest: "#2F387B",
        dark: "#4451B2",
        DEFAULT: "#7282F9",
        light: "#CDD3FF",
        lightest: "#F2F4FF",
      },
      success: {
        darkest: "#254125",
        dark: "#3B683B",
        DEFAULT: "#70AE6E",
        light: "#E7F6E7",
      },
      warning: {
        darkest: "#E09D00",
        dark: "#FFC233",
        DEFAULT: "#FFD470",
        light: "#FFEDC2",
      },
      error: {
        darkest: "#A72A11",
        dark: "#E03616",
        DEFAULT: "#ED6145",
        light: "#F2917D",
        background: "#FDF4F2",
      },
      burgundy: "#7F0055",
    },
    boxShadow: {
      light: "",
      focus: "0px 2px 4px 0px #CDD3FF",
      dark: "",
      disabled: "0px 0px 4px 0px rgba(39, 39, 39, 0.35)",
    },
  },
  plugins: [],
};
