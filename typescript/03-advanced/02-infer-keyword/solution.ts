// solution.ts - infer keyword answers

// TODO 1
type FirstElement<T> = T extends [infer TFirst, ...any[]] ? TFirst : never;

// TODO 2
type T1 = FirstElement<[string, number]>; // string

// TODO 3
type UnwrapPromise<T> = T extends Promise<infer U> ? UnwrapPromise<U> : T;
type P1 = UnwrapPromise<Promise<Promise<number>>>; // number

// TODO 4
type GetParameters<T> = T extends (...args: infer P) => any ? P : never;

// TODO 5
type LastChar<T extends string> = T extends `${infer _Prev}${infer Last}` 
    ? (Last extends "" ? T : LastChar<Last>) 
    : T;
// Note: recursive string inference is advanced!

// TODO 6
// Answer: Only within the 'extends' clause of a conditional type.

// CHALLENGE ANSWER
type Pop<T extends any[]> = T extends [...infer Rest, any] ? Rest : never;
type P2 = Pop<[1, 2, 3]>; // [1, 2]

console.log("\n--- Why it works ---");
console.log("1. Structural Matching: 'infer' allows TS to 'zoom in' on a specific part of a structure (like a function return or array element).");
console.log("2. Recursion: Combined with conditional types, 'infer' allows for deep unwrapping of types (like nested Promises).");
console.log("3. Template Literals: You can even infer parts of strings, enabling powerful pattern matching for string-based APIs.");
console.log("4. Utility Power: Most of TypeScript's built-in advanced utilities (like Awaited or ReturnType) are built using this exact syntax.");

export {}; // Prevent global scope collisions
