// example.ts - Fixed-length and Typed Collections

// 1. Basic Arrays
let scores: number[] = [90, 85, 100];
let names: string[] = ["Alice", "Bob"];

console.log("--- Arrays ---");
scores.push(95); // Allowed
// scores.push("A"); // Error

// 2. Tuples (Fixed length, fixed types)
let coord: [number, number] = [10.5, 20.3];
let userEntry: [number, string, boolean] = [1, "alice_92", true];

console.log("\n--- Tuples ---");
console.log(`Coords: ${coord[0]}, ${coord[1]}`);
console.log(`User ID: ${userEntry[0]} is Active: ${userEntry[2]}`);

// 3. Readonly Arrays/Tuples
const fixedPoint: readonly [number, number] = [0, 0];
// fixedPoint[0] = 5; // Error: Index signature in type 'readonly [0, 0]' only permits reading

// 4. Tuples with Optional Elements
let graphPoint: [number, number, number?] = [10, 20]; // 3rd is optional

// 5. Destructuring Tuples
const [x, y] = coord;
console.log(`\nDestructured: ${x}, ${y}`);

// 6. Practical Use: API Responses
type APIResult = [boolean, string | null];

function checkApi(): APIResult {
    return [true, "Data loaded"];
}
const [success, msg] = checkApi();
