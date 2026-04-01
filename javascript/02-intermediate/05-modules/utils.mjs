// utils.mjs - The Utility Module

// 1. Named Exports (multiple per file)
export const API_URL = "https://api.example.com";

export function add(a, b) {
    return a + b;
}

export function subtract(a, b) {
    return a - b;
}

// 2. Default Export (one per file)
const config = {
    theme: "dark",
    retries: 3
};

export default config;
