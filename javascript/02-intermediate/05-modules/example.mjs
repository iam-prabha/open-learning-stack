// example.mjs - The Main Entry Point
// Run this with: node example.mjs

// 1. Importing Named Exports
import { add, subtract, API_URL } from "./utils.mjs";

// 2. Importing Default Export (no curly braces!)
import appConfig from "./utils.mjs";

// 3. Importing everything as an alias
import * as MathTools from "./utils.mjs";

console.log("--- Named Imports ---");
console.log(`URL: ${API_URL}`);
console.log(`10 + 5 = ${add(10, 5)}`);

console.log("\n--- Default Import ---");
console.log(`Retries: ${appConfig.retries}`);

console.log("\n--- Aliased Library ---");
console.log(`Sub from tools: ${MathTools.subtract(20, 8)}`);
