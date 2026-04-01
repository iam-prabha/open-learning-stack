// exercise.ts - Practice with Narrowing

// TODO 1: Wrap this function in a 'typeof' check to fix the error:
/*
function getLength(input: string | number) {
    return input.length;
}
*/

// TODO 2: Use 'instanceof' to check if 'error' is an instance 
// of the built-in 'Error' class.

// TODO 3: Use the 'in' operator to check if 'pet' (Bird | Fish) 
// has a 'swim' method.

// TODO 4: Write a type predicate function 'isString' that 
// takes 'any' and returns 'val is string'.

// TODO 5: Use your 'isString' function to safely call 
// '.toLowerCase()' on a 'unknown' variable.

// TODO 6: Why can't you use 'instanceof' to check if an 
// object implements an 'interface'?
// Answer: ...

// CHALLENGE: Create a union of { type: 'success', data: string } | { type: 'failure', message: string }.
// Write a function that narrows the union using the 'type' property.

// --- Verification ---
console.log("--- Results ---");
// Fill in the guards and test your logic!
