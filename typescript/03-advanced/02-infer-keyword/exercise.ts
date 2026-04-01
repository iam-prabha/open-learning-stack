// exercise.ts - Practice with 'infer'

// TODO 1: Create a type 'FirstElement<T>' that:
// - If T is an array, infers the first element's type.
// - Otherwise, returns 'never'.

// TODO 2: Use 'FirstElement' on '[string, number]' 
// and observe the result.

// TODO 3: Create a type 'UnwrapPromise<T>' that uses 
// 'infer' to recursively get the nested type of a Promise.
// (Hint: T extends Promise<infer U> ? UnwrapPromise<U> : T)

// TODO 4: Create a type 'GetParameters<T>' that extracts 
// the parameters of a function as a tuple.

// TODO 5: Create a type 'LastChar<T>' that extracts the 
// last character of a template literal string.
// (Hint: T extends `${infer Rest}${infer Last}` ? ...)
// Actually, let's keep it simpler: T extends `${string}${infer Last}` where Last is 1 char.

// TODO 6: Where can the 'infer' keyword be used in TypeScript?
// Answer: ...

// CHALLENGE: Create a type 'Pop<T>' that takes a tuple 
// [1, 2, 3] and returns [1, 2] using 'infer' and rest '...'.

// --- Verification ---
console.log("--- Results ---");
// Check your inference logic vs the solution!

export {}; // Prevent global scope collisions
