/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#1a202c',
        secondary: '#2d3748',
        tertiary: '#4a5568',
        quaternary: '#718096',
        quinary: '#a0aec0',
        senary: '#cbd5e0',
        septenary: '#e2e8f0',
        octonary: '#edf2f7',
        white: '#ffffff',
        black: '#000000',
        red: '#f56565',
        green: '#48bb78',
        yellow: '#ecc94b',
        blue: '#4299e1',
        indigo: '#667eea',
        purple: '#9f7aea',
        pink: '#ed64a6',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        serif: ['Merriweather', 'serif'],
        mono: ['Fira Code', 'monospace'],
      },
      fontSize: {
        'xs': '.75rem',
        'sm': '.875rem',
        'base': '1rem',
        'lg': '1.125rem',
        'xl': '1.25rem',
        '2xl': '1.5rem',
        '3xl': '1.875rem',
        '4xl': '2.25rem',
        '5xl': '3rem',
        '6xl': '4rem',
      },
      spacing: {
        '0': '0',
        '1': '0.25rem',
        '2': '0.5rem',
        '3': '0.75rem',
        '4': '1rem',
        '5': '1.25rem',
        '6': '1.5rem',
        '8': '2rem',
        '10': '2.5rem',
        '12': '3rem',
        '16': '4rem',
        '20': '5rem',
        '24': '6rem',
        '32': '8rem',
        '40': '10rem',
        '48': '12rem',
        '56': '14rem',
        '64': '16rem',
      },
      borderRadius: {
        'none': '0',
        'sm': '0.125rem',
        DEFAULT: '0.25rem', // 4px
        'md': '0.375rem',
        'lg': '0.5rem',
        'xl': '0.75rem',
        '2xl': '1rem',
      },
    },
  },
  plugins: [],
  corePlugins: {
    preflight: false,
  },
  variants: {
    // ... your variants
  },
  content: [
    './src/**/*.{html,js,jsx}',
  ],
  purge: {
    layers: ['components', 'utilities'],
    content: [
      './src/**/*.{html,js,jsx}',
    ],
  },
};