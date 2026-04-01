// example.ts - Mastering Function Types

// 1. Basic Type Annotations
function add(a: number, b: number): number {
    return a + b;
}

console.log("--- Basic Typed Functions ---");
console.log(`10 + 20 = ${add(10, 20)}`);

// 2. Optional and Default Parameters
function greet(name: string, greeting: string = "Hello", title?: string): string {
    const prefix = title ? `${title} ` : "";
    return `${greeting}, ${prefix}${name}!`;
}

console.log("\n--- Optional/Default Params ---");
console.log(greet("Alice")); // "Hello, Alice!"
console.log(greet("Bob", "Hi", "Dr.")); // "Hi, Dr. Bob!"

// 3. Void (No return value)
function logError(message: string): void {
    console.error(`[ERROR]: ${message}`);
}
logError("Something went wrong!");

// 4. Rest Parameters (The '...' operator)
function sumAll(...numbers: number[]): number {
    return numbers.reduce((acc, curr) => acc + curr, 0);
}

console.log("\n--- Rest Parameters ---");
console.log(`Sum of 1,2,3,4: ${sumAll(1, 2, 3, 4)}`);

// 5. Arrow Functions with types
const multiply = (x: number, y: number): number => x * y;
console.log(`5 * 5 = ${multiply(5, 5)}`);
