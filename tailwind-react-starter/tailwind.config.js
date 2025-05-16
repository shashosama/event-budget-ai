/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        cream: '#FFFDF5',
        ink: '#1A237E',
      },
      fontFamily: {
        body: ['"Times New Roman"', 'serif'],
      },
    },
  },
  plugins: [],
};
