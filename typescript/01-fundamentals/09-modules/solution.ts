// solution.ts - Modules answers

// TODO 1 & 2
/*
// config.ts
export const API_KEY = "123-abc";
export interface Settings { theme: string; }
*/

// TODO 3
// import { API_KEY, Settings } from "./config";

// TODO 4
// Answer: Use 'import type { Settings } from "./config";'

// TODO 5
// import * as MathTools from "./math";

// TODO 6
// Answer: They are completely removed (erased). The compiled 
// JavaScript will have no reference to them at all.

// CHALLENGE ANSWER
/*
// logger.ts
export const LOG_LEVEL = "DEBUG";
export default function log(m: string) { console.log(m); }

// main.ts
import log, { LOG_LEVEL } from "./logger";
*/

console.log("\n--- Why it works ---");
console.log("1. Organization: You can break massive projects into small, manageable units without cluttering the global scope.");
console.log("2. Type-safety: By exporting interfaces, you ensure that every part of your app 'speaks the same language.'");
console.log("3. Compilation: TS handles the complex logic of converting modern imports into whatever format your runtime needs (CommonJS, ESM, etc.).");
console.log("4. Clarity: 'import type' gives an explicit hint to both the developer and the compiler that this is a zero-runtime dependency.");
