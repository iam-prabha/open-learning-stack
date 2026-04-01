// exercise.ts - Practice with Conditional Types

// TODO 1: Create a conditional type 'IsString<T>' 
// that returns true if T is a string, false otherwise.

// TODO 2: Create a type 'Result' by passing 'number' 
// to your 'IsString' type.

// TODO 3: Create a type 'Flatten<T>' that:
// - If T is an array 'Array<infer U>', returns U.
// - Otherwise, returns T.

// TODO 4: Use 'Flatten' on 'string[]' and 'number'.

// TODO 5: Create a type 'GetIdType<T>' that:
// - If T has an 'id' property, returns the type of 'id'.
// - Otherwise, returns 'never'.

// TODO 6: What happens when you pass a Union 
// (e.g. string | number) to a conditional type?
// Answer: ...

// CHALLENGE: Create a type 'MyReturnType<T>' that 
// uses 'infer' to extract the return type of any function T.

// --- Verification ---
console.log("--- Results ---");
// Check your type logic vs the solution!
