// solution.ts - Template Literal Types answers

// TODO 1 & 2
type Protocol = "http" | "https";
type MyURL = `${Protocol}://localhost`;

// TODO 3 & 4
type Size = "small" | "large";
type Fruit = "apple" | "banana";
type Order = `${Size}-${Fruit}`;

// TODO 5
type Input = "fatal";
type ERROR_CODE = Uppercase<Input>;

// TODO 6
// Answer: It refers to the way TypeScript automatically generates 
// every possible combination when two or more unions are 
// interpolated into a template literal type.

// CHALLENGE ANSWER
type PropEvent<T extends string> = `on_${Capitalize<T>}`;
type Events = PropEvent<"click" | "scroll">; // "on_Click" | "on_Scroll"

console.log("\n--- Why it works ---");
console.log("1. String Precision: Template types allow you to enforce strict patterns (like Protocols or API paths) that plain strings cannot.");
console.log("2. Automation: Instead of manually typing out 50 combinations of CSS classes or events, you generate them in one line.");
console.log("3. API Design: They are the foundation of 'Type-safe pathing' in frameworks, ensuring you can't navigate to a nonexistent route.");
console.log("4. Readability: Combined with Mapped Types, they make complex key transformations transparent and easy to follow.");
