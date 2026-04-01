// solution.ts - Type-Level Programming answers

// TODO 1 & 2
type DeepReadonly<T> = T extends object 
    ? { readonly [P in keyof T]: DeepReadonly<T[P]> } 
    : T;

// TODO 3
type Reverse<T extends any[]> = T extends [infer First, ...infer Rest] 
    ? [...Reverse<Rest>, First] 
    : [];

// TODO 4
type Join<T extends string[], D extends string> = 
    T extends [infer First extends string, ...infer Rest extends string[]]
        ? Rest extends [] 
            ? First 
            : `${First}${D}${Join<Rest, D>}`
        : "";

// TODO 5
type Trim<T extends string> = T extends ` ${infer R}` | `${infer R} ` 
    ? Trim<R> : T;

// TODO 6
// Answer: Performance and Stability. Deeply recursive types can 
// hit the recursion limit, causing build failures. They also 
// slow down your IDE because the compiler has to 're-calculate' 
// these types on every keystroke.

// CHALLENGE ANSWER
type Add<N1 extends any[], N2 extends any[]> = [...N1, ...N2];
// Result: A tuple whose .length is the sum!

console.log("\n--- Why it works ---");
console.log("1. Turing Completeness: TS can solve mathematical and logical problems by treating 'types' as data and 'conditionals/recursion' as instructions.");
console.log("2. Precision: You can define APIs that are so specific they are 'correct by construction' (e.g., path route params match the handler).");
console.log("3. Automation: Complex data transformations (like converting snake_case to camelCase) can be done entirely at the type level.");
console.log("4. Future-proofing: As the TS compiler gets faster, these techniques become more widely applicable for high-scale enterprise codebases.");

export {};
