// example.js - Exploring JavaScript's 8 data types

// 1. Primitive Types
const myString = "Hello JS";        // String
const myNumber = 42.5;              // Number (always 64-bit float)
const myBool = true;                 // Boolean
const myNull = null;                 // Null (intentional nothing)
let myUndefined;                     // Undefined (automatic nothing)
const mySymbol = Symbol("id");       // Symbol (unique identifier)
const myBigInt = 9007199254740991n;  // BigInt (ends with 'n')

console.log("--- Primitive Types ---");
console.log(`typeof myString: ${typeof myString}`);
console.log(`typeof myNumber: ${typeof myNumber}`);
console.log(`typeof myBool:   ${typeof myBool}`);
console.log(`typeof myNull:   ${typeof myNull}`); // Note: "object" (legacy bug)
console.log(`typeof myUndef:  ${typeof myUndefined}`);
console.log(`typeof mySymbol: ${typeof mySymbol}`);
console.log(`typeof myBigInt: ${typeof myBigInt}`);

// 2. Objects (Reference Types)
const myObject = { name: "Alice", age: 30 };
const myArray = [1, 2, 3];
const myFunction = function() { return "I am a function"; };

console.log("\n--- Reference Types ---");
console.log(`typeof myObject:   ${typeof myObject}`);
console.log(`typeof myArray:    ${typeof myArray}`);    // Note: "object"
console.log(`typeof myFunction: ${typeof myFunction}`); // Note: "function"

// 3. Immutability of Primitives
let val = "Original";
val.toUpperCase(); // returns "ORIGINAL" but doesn't change 'val'
console.log(`\nPrimitive: ${val}`); // Still "Original"

// 4. Mutability of Objects
const user = { name: "Alice" };
user.name = "Bob";
console.log(`Object:    ${user.name}`); // Changed to "Bob"
