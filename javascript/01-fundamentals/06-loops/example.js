// example.js - Iteration in JavaScript

// 1. Classic for loop
console.log("--- for loop ---");
for (let i = 1; i <= 3; i++) {
    console.log(`Lap ${i}`);
}

// 2. while loop
console.log("\n--- while loop ---");
let count = 3;
while (count > 0) {
    console.log(`Blastoff in ${count}...`);
    count--;
}

// 3. for...of (Best for Arrays/Strings)
console.log("\n--- for...of (Values) ---");
const fruits = ["apple", "banana", "cherry"];
for (const fruit of fruits) {
    console.log(`Eating ${fruit}`);
}

// 4. for...in (Best for Objects)
console.log("\n--- for...in (Keys) ---");
const user = { name: "Alice", Role: "Admin", id: 501 };
for (const key in user) {
    console.log(`${key}: ${user[key]}`);
}

// 5. break and continue
console.log("\n--- break/continue ---");
for (let j = 1; j <= 5; j++) {
    if (j === 2) continue; // Skip 2
    if (j === 4) break;    // Stop at 4
    console.log(`Number ${j}`);
}
// Outputs: 1, 3
