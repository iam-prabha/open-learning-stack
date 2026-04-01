// example.js - Reusable code in JavaScript

// 1. Function Declaration (Hoisted)
function greet(name = "Guest") { // "Guest" is a default parameter
    return `Hello, ${name}!`;
}

console.log("--- Declaration ---");
console.log(greet("Alice"));
console.log(greet()); // Uses default "Guest"

// 2. Function Expression (Not Hoisted)
const add = function(a, b) {
    return a + b;
};

console.log("\n--- Expression ---");
console.log(`5 + 3 = ${add(5, 3)}`);

// 3. Arrow Function (Concise)
// Short version (Implicit return)
const multiply = (a, b) => a * b;

// Long version (Explicit return with { })
const divide = (a, b) => {
    if (b === 0) return "Error";
    return a / b;
};

console.log("\n--- Arrow Functions ---");
console.log(`4 * 4 = ${multiply(4, 4)}`);
console.log(`10 / 2 = ${divide(10, 2)}`);

// 4. Anonymous Functions (Callback demo)
console.log("\n--- Callback Demo ---");
const numbers = [1, 2, 3];
const squares = numbers.map(n => n * n); // Arrow function passed as argument
console.log(`Squares: ${squares}`);

// 5. Scope in Functions
let outerVal = "Global";
function checkScope() {
    let innerVal = "Local";
    console.log(outerVal); // Accessible
    console.log(innerVal); // Accessible
}
checkScope();
// console.log(innerVal); // Error: ReferenceError (innerVal not defined here)
