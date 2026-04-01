// solution.js - Operator answers

// TODO 1
const radius = 5;
const area = Math.PI * (radius ** 2);

// TODO 2
const isEven = (17 % 2 === 0);

// TODO 3
console.log(`10 == "10" : ${10 == "10"}`);   // true
console.log(`10 === "10": ${10 === "10"}`);  // false

// TODO 4
const age = 25;
const isWorkingAge = (age >= 18 && age <= 65);

// TODO 5
let username = null;
const displayName = username ?? "Guest";

// TODO 6
let points = 100;
points += 10;

// CHALLENGE ANSWER
let x = 5;
console.log(`Post-increment: ${x++}`); // Log 5, then x becomes 6
console.log(`Pre-increment:  ${++x}`); // x becomes 7, then log 7
// x++ returns the value BEFORE incrementing.
// ++x increments the value FIRST, then returns it.

// --- Verification ---
console.log("--- Verification ---");
console.log(`Area: ${area.toFixed(2)}`);
console.log(`Is 17 even? ${isEven}`);
console.log(`Display Name: ${displayName}`);
console.log(`Final points: ${points}`);

console.log("\n--- Why it works ---");
console.log("1. Strict Equality (===): Checks both value and type. Never uses weird coercion rules.");
console.log("2. Nullish Coalescing (??): Safer than || for providing defaults because it doesn't treat 0 or '' as null.");
console.log("3. Short-circuiting: In 'a && b', if 'a' is false, 'b' is never even evaluated.");
console.log("4. Compound Assignment: Saves time. points = points + 10 is identical to points += 10.");
