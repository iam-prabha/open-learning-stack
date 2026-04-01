// solution.js - Data types answers

// TODO 1
const s = "text";
const n = 123;
const b = true;
const nl = null;
let ud;

// TODO 2
const result2 = typeof 42n; // "bigint"

// TODO 3
const car = { make: "Toyota", model: "Corolla", year: 2020 };

// TODO 4
const colors = ["red", "green", "blue"];

// TODO 5
const sumResult = 0.1 + 0.2; // 0.30000000000000004
console.log(`0.1 + 0.2 = ${sumResult}`);

// TODO 6
const isArrayCheck = Array.isArray(colors); // true
// We use Array.isArray because 'typeof' returns "object" for arrays, 
// which doesn't distinguish them from regular objects.

// CHALLENGE ANSWER
const obj1 = {};
const obj2 = {};
const comparison = (obj1 === obj2); // false
// Even though both are empty objects, they are different objects in memory.
// JavaScript compares objects by reference (memory address), not by value.

// --- Verification ---
console.log("--- Verification ---");
console.log(`Type of 42n: ${result2}`);
console.log(`Is Array? ${isArrayCheck}`);
console.log(`Compare {} === {}: ${comparison}`);
console.log(`Car Year: ${car.year}`);

console.log("\n--- Why it works ---");
console.log("1. Primitives: Immutable and compared by value. 5 === 5 is always true.");
console.log("2. Objects: Mutable and compared by reference. Each {} creates a new unique address.");
console.log("3. Numbers: JS uses IEEE 754 floating point. 0.1 + 0.2 rounding error is a side effect of binary math.");
console.log("4. Null vs Undefined: undefined means 'not born yet'; null means 'intentionally gone'.");
