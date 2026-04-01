// example.js - let, const, and scope in JavaScript

// 1. const vs let
const pi = 3.14159;
let score = 0;

console.log("--- Initial Values ---");
console.log(`Pi: ${pi}`);
console.log(`Score: ${score}`);

// pi = 3.14; // Error: Assignment to constant variable.
score = 10;   // OK: let can be re-assigned
console.log(`New Score: ${score}`);

// 2. Block Scope
console.log("\n--- Block Scope ---");
if (true) {
    const blockScoped = "I only live in this IF block";
    var functionScoped = "I leak out of the block!";
    console.log(blockScoped);
}

// console.log(blockScoped); // ReferenceError
console.log(`var leaked: ${functionScoped}`);

// 3. Hoisting (The 'var' quirk)
console.log("\n--- Hoisting ---");
console.log(`hoistedVar before decl: ${hoistedVar}`); // prints undefined (doesn't crash)
var hoistedVar = "I was hoisted";

// console.log(notHoisted); // ReferenceError: Cannot access before initialization
let notHoisted = "I am safe";

// 4. Constants and Objects
console.log("\n--- const and Objects ---");
const user = { name: "Alice" };
// user = { name: "Bob" }; // Error: Re-assigning the label
user.name = "Bob";         // OK: Mutating the internal data
console.log(`User name: ${user.name}`);
