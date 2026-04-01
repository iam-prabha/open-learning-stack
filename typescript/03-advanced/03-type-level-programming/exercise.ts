// exercise.ts - Practice with Type-Level Programming

// TODO 1: Create a recursive type 'DeepReadonly<T>' 
// that makes every property at every level 'readonly'.

// TODO 2: Test 'DeepReadonly' on the 'ComplexUser' interface.

// TODO 3: Create a type 'Reverse<T>' that reverses 
// a tuple (e.g., [1, 2, 3] -> [3, 2, 1]).
// (Hint: T extends [infer First, ...infer Rest] ? [...Reverse<Rest>, First] : [])

// TODO 4: Create a type 'Join<T, D>' that joins a tuple 
// of strings with a delimiter (e.g., Join<['a', 'b'], '-'> -> 'a-b').

// TODO 5: Create a type 'Trim<T>' that removes leading 
// and trailing whitespace from a string.
// (Hint: T extends ` ${infer R}` | `${infer R} ` ? Trim<R> : T)

// TODO 6: What is the main risk of using deeply recursive 
// types in a large project?
// Answer: ...

// CHALLENGE: Create a type-level 'Add<N1, N2>' that increments 
// numbers represented as tuple lengths.
// (e.g., Add<[any, any], [any]> -> [any, any, any] (3))

// --- Verification ---
console.log("--- Results ---");
// Check your type-level magic vs the solution!

export {};
