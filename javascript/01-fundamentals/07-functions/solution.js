// solution.js - Function answers

// TODO 1
function isEven(num) {
    return num % 2 === 0;
}

// TODO 2
const subtract = function(a, b) {
    return a - b;
};

// TODO 3
const powerOfTwo = n => n * n;

// TODO 4
function calculateTotal(price, tax = 0.1) {
    return price + (price * tax);
}

// TODO 5
const numbers = [10, 20, 30];
const doubled = numbers.map(n => n * 2);

// TODO 6
const describePerson = (name, age) => `${name} is ${age} years old.`;

// CHALLENGE ANSWER
function findMax(nums) {
    if (nums.length === 0) return null;
    return Math.max(...nums); // spread operator expands the array
}

// --- Verification ---
console.log("--- Verification ---");
console.log(`isEven(10): ${isEven(10)}`);
console.log(`subtract(20, 5): ${subtract(20, 5)}`);
console.log(`powerOfTwo(8): ${powerOfTwo(8)}`);
console.log(`Total: ${calculateTotal(100)}`);
console.log(`Doubled: ${doubled}`);
console.log(describePerson("Bob", 40));
console.log(`Max: ${findMax([1, 5, 2, 9, 3])}`);

console.log("\n--- Why it works ---");
console.log("1. Declaration: Benefits from 'hoisting', allowing you to call it anywhere in the file.");
console.log("2. Expression: Treats functions like variables, useful for callbacks and keeping global scope clean.");
console.log("3. Arrow Function: If there is only one parameter, you can omit ( ). If it's one line, you omit { return }.");
console.log("4. Default Params: Ensure your code doesn't break (e.g. NaN) if an expected value is missing.");
