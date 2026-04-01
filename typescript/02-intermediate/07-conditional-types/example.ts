// example.ts - Type-level Logic with Conditionals

// 1. Basic Conditional Type
// If T is a string, return "TEXT", otherwise return "DATA"
type CheckType<T> = T extends string ? "TEXT" : "DATA";

type R1 = CheckType<string>; // "TEXT"
type R2 = CheckType<number>; // "DATA"

// 2. Distributive Conditional Types
// When T is a union, it runs for each member
type ToArray<T> = T extends any ? T[] : never;

type StringOrNumberArray = ToArray<string | number>; 
// Result: string[] | number[]

// 3. Using 'infer' to pluck types
type GetResult<T> = T extends (...args: any[]) => infer R ? R : never;

function save() { return { id: 1 }; }
type SaveResult = GetResult<typeof save>; // { id: number }

// 4. Practical Implementation: NonNullable (simplified)
type MyNonNullable<T> = T extends null | undefined ? never : T;

type ValidString = MyNonNullable<string | null>; // string

// 5. Constraining the Input
type MessageOf<T extends { message: unknown }> = T["message"];

interface Email { message: string; }
type EmailMsg = MessageOf<Email>; // string
