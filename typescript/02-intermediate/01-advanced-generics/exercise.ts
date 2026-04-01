// exercise.ts - Practice with Advanced Generics

// TODO 1: Create an interface 'HasId' that requires an 'id' (number).

// TODO 2: Write a generic function 'findItem<T>' that takes an 
// array of T (where T extends HasId) and a number id. 
// It should return the found item or undefined.

// TODO 3: Create a generic interface 'Box<T>' where T 
// defaults to 'string'.

// TODO 4: Create a variable 'myBox' that uses the 
// default type from TODO 3.

// TODO 5: Write a function 'pluck<T, K extends keyof T>' 
// that takes an object and a key and returns the value.

// TODO 6: Why is 'T extends object' safer than just using 'T'?
// Answer: ...

// CHALLENGE: Create a generic class 'Container<T extends { value: any }>' 
// that has a method 'getValue()' returning the internal value.

// --- Verification ---
console.log("--- Results ---");
// After filling in, check your code logic!
