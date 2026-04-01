// exercise.ts - Practice with Unions and Intersections

// TODO 1: Create a variable 'result' that can be 
// either a boolean or the number 0.

// TODO 2: Write a function 'printLength' that takes 
// a parameter that is either a string or string[].
// (Hint: use Array.isArray() to check if it's an array)

// TODO 3: Create a literal union 'Status' with 
// "Online", "Offline", and "Away".

// TODO 4: Create two interfaces: 'Logger' (with a log method) 
// and 'Writer' (with a write method).

// TODO 5: Create a type 'LogWriter' that is an 
// INTERSECTION of 'Logger' and 'Writer'. Implement an 
// object that fits the 'LogWriter' type.

// TODO 6: Why can you only access common properties of 
// a union type without narrowing?
// Answer: ...

// CHALLENGE: Create a function 'processData' that accepts 
// a union of { type: "user"; info: string } | { type: "admin"; level: number }.
// Use the 'type' property to handle both cases.

// --- Verification ---
console.log("--- Results ---");
// Check your code logic vs solution!
