// example.js - Standard and unique operators in JavaScript

// 1. Arithmetic
console.log("--- Arithmetic ---");
console.log(`5 + 2 = ${5 + 2}`);
console.log(`5 - 2 = ${5 - 2}`);
console.log(`5 * 2 = ${5 * 2}`);
console.log(`5 / 2 = ${5 / 2}`);
console.log(`5 ** 2 = ${5 ** 2}`); // Exponentiation
console.log(`10 % 3 = ${10 % 3}`);  // Remainder

// 2. Comparison (The Strict Equality Rule)
console.log("\n--- Comparison ---");
console.log(`5 == "5"  : ${5 == "5"}`);  // true (Loose - avoid!)
console.log(`5 === "5" : ${5 === "5"}`); // false (Strict - use this!)
console.log(`0 === false: ${0 === false}`); // false

// 3. Logical Operators
console.log("\n--- Logical ---");
const isAdult = true;
const hasTicket = false;
console.log(`AND (&&): ${isAdult && hasTicket}`); // false
console.log(`OR  (||): ${isAdult || hasTicket}`); // true
console.log(`NOT (! ): ${!isAdult}`);            // false

// 4. Nullish Coalescing (??)
// Returns the right side ONLY if the left side is null or undefined
console.log("\n--- Nullish Coalescing ---");
const score = 0;
const defaultScore = score ?? 10; // score is 0 (not null/undef), so 0 is kept
const altScore = score || 10;     // score is 0 (falsy), so 10 is used
console.log(`score ?? 10: ${defaultScore}`);
console.log(`score || 10: ${altScore}`);

// 5. Compound Assignment
let count = 10;
count += 5; // 15
count *= 2; // 30
console.log(`\nFinal count: ${count}`);
