// solution.js - Conditionals answers

// TODO 1
const temp = 32;
if (temp > 30) {
    console.log("It's hot!");
} else {
    console.log("It's fine.");
}

// TODO 2
const isAuthenticated = true;
const message = isAuthenticated ? "Allowed" : "Denied";

// TODO 3
let fruit = "banana";
switch (fruit) {
    case "apple":
        console.log("Red");
        break;
    case "banana":
        console.log("Yellow");
        break;
    case "orange":
        console.log("Orange");
        break;
    default:
        console.log("Unknown color");
}

// TODO 4
let myValue = "";
if (myValue) {
    console.log("Value exists");
} else {
    console.log("Value is falsy (empty/null/undef/0)");
}

// TODO 5
const age = 20, isCitizen = true;
if (age >= 18 && isCitizen) {
    console.log("Can vote");
}

// TODO 6 (Demo)
const test = 1;
console.log("Switch test (no break):");
switch(test) {
    case 1: console.log("one");
    case 2: console.log("two");
    default: console.log("default");
}

// CHALLENGE ANSWER
function fizzBuzz(n) {
    if (n % 3 === 0 && n % 5 === 0) return "FizzBuzz";
    if (n % 3 === 0) return "Fizz";
    if (n % 5 === 0) return "Buzz";
    return n;
}

// --- Verification ---
console.log("--- Verification ---");
console.log(`Ternary result: ${message}`);
console.log(`FizzBuzz(15): ${fizzBuzz(15)}`);
console.log(`FizzBuzz(9):  ${fizzBuzz(9)}`);

console.log("\n--- Why it works ---");
console.log("1. Multi-branch logic: switch/case is optimized for checking many exact values (strings/numbers).");
output: "2. The 'Ternary': Extremely efficient for simple binary decisions, especially inside template literals.";
console.log("3. Falsy values: JS treated 0, '', null, undef, and NaN as false. This makes 'if(val)' checks very common.");
console.log("4. Short-circuiting: 'a && b' only proceeds if 'a' is true. 'a || b' only proceeds if 'a' is false.");
