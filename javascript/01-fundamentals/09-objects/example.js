// example.js - Mastering Objects in JavaScript

// 1. Literal Notation and Methods
const laptop = {
    brand: "Apple",
    model: "MacBook Pro",
    ram: 16,
    describe() {
        // 'this' refers to the object itself
        return `${this.brand} ${this.model} with ${this.ram}GB RAM`;
    }
};

console.log("--- Methods ---");
console.log(laptop.describe());

// 2. Shorthand and Computed Properties
const username = "iamprabha";
const status = "online";
const key = "dynamic_id";

const user = {
    username, // same as username: username
    status,
    [key]: 12345 // Computed property name
};

console.log("\n--- Modern Syntax ---");
console.dir(user);

// 3. Destructuring and Spread
const { username: nameOnly, status: s } = user; // Extract and rename
const updatedUser = { ...user, status: "away" }; // Update without mutating original

console.log("\n--- Destructuring & Spread ---");
console.log(`Name: ${nameOnly}, Status: ${s}`);
console.dir(updatedUser);

// 4. Nested Objects and Optional Chaining
const company = {
    name: "TechCorp",
    // address is missing
};

console.log("\n--- Optional Chaining ---");
// This won't crash even if 'address' is undefined
const zip = company.address?.zipCode; 
console.log(`Zip Code: ${zip ?? "Not Found"}`);

// 5. Object.keys / Object.values
console.log("\n--- Iteration Helpers ---");
console.log(`Keys:`, Object.keys(laptop));
console.log(`Values:`, Object.values(laptop));
