// solution.ts - Types and Annotations answers

// TODO 1
let planet: string = "Earth";

// TODO 2
let distance: number = 149.6;

// TODO 3
let colors: string[] = ["Red", "Green", "Blue"];

// TODO 4
function multiply(x: number, y: number): number {
    return x * y;
}

// TODO 5
let points = 10;
// points = "low"; // Error: Type 'string' is not assignable to type 'number'

// TODO 6
// Answer: 'any' disables type checking. If you use it, you lose the safety 
// of TypeScript, essentially going back to standard JavaScript, which 
// allows bugs to sneak into production.

// CHALLENGE ANSWER
let user: { id: number; email?: string } = {
    id: 1,
    // email is optional, so it's okay to omit it
};
user.email = "test@example.com";

console.log("\n--- Why it works ---");
console.log("1. Safety: By defining types, you get red squiggles (errors) in the IDE as you type, not after you refresh the browser.");
console.log("2. Documentation: Types serve as living documentation. A new developer knows exactly what 'multiply' expects without reading the whole function.");
console.log("3. Inference: TypeScript is smart. It doesn't force you to type everything — only the things it can't figure out on its own.");
console.log("4. Autocomplete: Because TS knows your object structure, it provides perfect code-completion (Intellisense).");
