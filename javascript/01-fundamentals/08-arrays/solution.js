// solution.js - Array answers

// TODO 1 & 2
const hobbies = ["reading", "hiking", "gaming"];
hobbies.push("coding");
hobbies.shift(); // removes "reading"

// TODO 3
const ages = [12, 18, 25, 40, 15, 30];
const adults = ages.filter(a => a >= 18);

// TODO 4
const fruits = ["Apple", "Orange", "Banana"];
const labeledFruits = fruits.map(f => `Fresh ${f}`);

// TODO 5
const set1 = [1, 2], set2 = [3, 4];
const allNums = [...set1, ...set2];

// TODO 6
const colors = ["gold", "silver", "bronze"];
const [top1, top2] = colors;

// CHALLENGE ANSWER
const animals = ["cat", "elephant", "dog", "giraffe"];
const longest = animals.reduce((prev, curr) => {
    return curr.length > prev.length ? curr : prev;
}, "");

// --- Verification ---
console.log("--- Verification ---");
console.log(`Hobbies:`, hobbies);
console.log(`Adults:  `, adults);
console.log(`Labeled: `, labeledFruits);
console.log(`All Nums:`, allNums);
console.log(`Top 2:   ${top1}, ${top2}`);
console.log(`Longest animal: ${longest}`);

console.log("\n--- Why it works ---");
console.log("1. Mutation (.push, .shift): These change the original array. Useful for local state.");
console.log("2. Immutability (.map, .filter): These return new arrays, keeping your data 'pipelined' and safer.");
console.log("3. Spread (...): Creates a shallow copy. Modifying the copy doesn't affect the original array.");
console.log("4. Destructuring: A concise way to 'unpack' values. Improves code readability significantly.");
