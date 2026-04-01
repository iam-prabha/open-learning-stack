// solution.js - Object answers

// TODO 1 & 2
const person = {
    firstName: "John",
    lastName: "Doe",
    age: 25,
    fullName() {
        return `${this.firstName} ${this.lastName}`;
    }
};

// TODO 3
const { age } = person;

// TODO 4
const updatedPerson = {
    ...person,
    age: person.age + 1
};

// TODO 5
const propName = "firstName";
const val = person[propName];

// TODO 6
const city = person.address?.city ?? "Unknown";

// CHALLENGE ANSWER
const calculator = {
    add: (a, b) => a + b,
    sub: (a, b) => a - b
};

// --- Verification ---
console.log("--- Verification ---");
console.log(`Full Name: ${person.fullName()}`);
console.log(`Extracted Age: ${age}`);
console.log(`Updated Age: ${updatedPerson.age}`);
console.log(`Bracket Access: ${val}`);
console.log(`Safe City: ${city}`);
console.log(`Calc Add: ${calculator.add(10, 5)}`);

console.log("\n--- Why it works ---");
console.log("1. Methods: Use the 'function' keyword or shorthand syntax to have access to 'this'.");
console.log("2. Spread (...): Essential for 'immutable' updates — creates a new object instead of changing the old one.");
console.log("3. Optional Chaining: Prevents the #1 error in JS (Cannot read property 'x' of undefined).");
console.log("4. Keys/Values: Converting objects to arrays makes it easy to use .map() or .filter() on them.");
