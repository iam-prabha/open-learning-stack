// solution.js - Modules answers

// TODO 1
// export const PI = 3.14159;

// TODO 2
// export default function square(n) { return n * n; }

// TODO 3
// import square, { PI } from "./math.js";

// TODO 4
// import { PI as circleConstant } from "./math.js";

// TODO 5
/*
export const info = (msg) => console.log(`[INFO] ${msg}`);
export const warn = (msg) => console.log(`[WARN] ${msg}`);
export const error = (msg) => console.log(`[ERROR] ${msg}`);
*/

// TODO 6
// Answer: You will get a SyntaxError. A file can only have ONE default export.

// CHALLENGE ANSWER
/*
// database.mjs
export const VERSION = "1.0.0";
const db = {
    connect: () => "Connected",
    query: (q) => `Result for ${q}`
};
export default db;
*/

console.log("--- Why it works ---");
console.log("1. Named vs Default: Defaults are for 'the main point' of a file; Named are for 'bags of tools'.");
console.log("2. Scope: Variables in a module are NOT global. They can only be accessed if explicitly exported.");
console.log("3. Tree Shaking: Modern tools (Webpack/Vite) can 'shake off' named exports you don't use, making your app smaller.");
console.log("4. Read-only bindings: Imported variables are live-read-only. You can see updates inside the module, but you can't change the value of the imported variable yourself.");
