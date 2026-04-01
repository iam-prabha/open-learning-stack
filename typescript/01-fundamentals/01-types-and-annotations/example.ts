// example.ts - Basic Type Annotations in TypeScript

// 1. Primitives
let username: string = "Alice";
let age: number = 30;
let isLearner: boolean = true;

console.log("--- Primitive Types ---");
console.log(`${username} is ${age} years old.`);

// 2. Type Inference (TS guesses the type)
let score = 100; // TS knows this is a 'number'
// score = "high"; // Error: Type 'string' is not assignable to type 'number'

// 3. Arrays
let hobbies: string[] = ["Coding", "Reading", "Hiking"];
let luckyNumbers: Array<number> = [7, 13, 21]; // Alternative syntax

// 4. Any (The escape hatch - use sparingly!)
let dynamicData: any = "I can be anything";
dynamicData = 42;
dynamicData = { message: "still works" };

// 5. Functions (Parameters and Return Types)
function greet(name: string): string {
    return `Hello, ${name}!`;
}

console.log("\n--- Function Types ---");
console.log(greet("TypeScript Developer"));

// 6. Object Literals
let car: { make: string; year: number } = {
    make: "Tesla",
    year: 2023
};
