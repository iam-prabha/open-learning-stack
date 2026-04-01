// solution.ts - Conditional Types answers

// TODO 1
type IsString<T> = T extends string ? true : false;

// TODO 2
type Result = IsString<number>; // false

// TODO 3
type Flatten<T> = T extends Array<infer U> ? U : T;

// TODO 4
type F1 = Flatten<string[]>; // string
type F2 = Flatten<number>; // number

// TODO 5
type GetIdType<T> = T extends { id: infer I } ? I : never;

// TODO 6
// Answer: If the type is distributive (most are), the condition 
// check is run for EACH member of the union. The result is a 
// new union containing the individual results.

// CHALLENGE ANSWER
type MyReturnType<T> = T extends (...args: any[]) => infer R ? R : any;

console.log("\n--- Why it works ---");
console.log("1. Type-level Logic: Conditional types allow the type system to 'compute' types based on existing ones, just like JS code computes values.");
console.log("2. Distribution: The automatic 'looping' over unions makes these types incredibly powerful for transforming entire data models.");
console.log("3. Inference: The 'infer' keyword allows you to extract information that's otherwise hard to reach (like a function's return type).");
console.log("4. Robustness: You can eliminate impossible types (using 'never') or provide safe defaults, ensuring your APIs are 100% accurate.");
