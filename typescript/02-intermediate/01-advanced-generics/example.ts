// example.ts - Constraints and Defaults in Generics

// 1. Generic Constraints (extends)
interface Lengthwise {
    length: number;
}

// T must be something that has a .length property
function logLength<T extends Lengthwise>(arg: T): void {
    console.log(`Length is: ${arg.length}`);
}

console.log("--- Constraints ---");
logLength("Hello"); // String has length
logLength([1, 2, 3]); // Array has length
// logLength(123); // Error: number doesn't have a length!

// 2. Using 'keyof' Constraint
function getProperty<T extends object, K extends keyof T>(obj: T, key: K) {
    return obj[key];
}

const user = { id: 1, name: "Alice" };
console.log("\n--- keyof Constraint ---");
console.log(getProperty(user, "name")); // OK
// getProperty(user, "age"); // Error: "age" is not a key of user

// 3. Generic Parameter Defaults
interface ApiResponse<T = any> {
    data: T;
    status: number;
}

// Defaults to 'any' data
const genericRes: ApiResponse = { data: "raw", status: 200 };

// Specifically a number array
const specificRes: ApiResponse<number[]> = { data: [1], status: 200 };

// 4. Multiple Parameters with Constraints
class Processor<T extends string, U = number> {
    constructor(public id: T, public value: U) {}
}

const p = new Processor("task-1", 100);
console.log("\n--- Defaults and Constraints ---");
console.log(`ID: ${p.id}, Value: ${p.value}`);
