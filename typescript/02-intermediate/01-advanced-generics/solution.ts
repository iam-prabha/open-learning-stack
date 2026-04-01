// solution.ts - Advanced Generics answers

// TODO 1
interface HasId {
    id: number;
}

// TODO 2
function findItem<T extends HasId>(items: T[], id: number): T | undefined {
    return items.find(item => item.id === id);
}

// TODO 3 & 4
interface Box<T = string> {
    value: T;
}
const myBox: Box = { value: "A string" }; // Defaults to string

// TODO 5
function pluck<T extends object, K extends keyof T>(obj: T, key: K) {
    return obj[key];
}

const data = { name: "Alice", age: 25 };
const userName = pluck(data, "name"); // Works!

// TODO 6
// Answer: 'T extends object' allows you to use methods and features 
// that only work on objects (like using 'keyof' or spread). It 
// prevents the function from being called with primitives like 
// strings or numbers when an object is required.

// CHALLENGE ANSWER
abstract class Container<T extends { value: any }> {
    constructor(protected data: T) {}
    getValue() { return this.data.value; }
}

class StringContainer extends Container<{ value: string }> {
    constructor(val: string) { super({ value: val }); }
}

const c = new StringContainer("Hello");
console.log(`Value: ${c.getValue()}`);

console.log("\n--- Why it works ---");
console.log("1. Safety with Constraints: Extending an interface (like HasId) ensures that the generic T *must* have specific properties, preventing runtime errors.");
console.log("2. Precision with keyof: By tying one generic parameter to the keys of another, you create a perfect link between an object and its properties.");
console.log("3. Ergonomics with Defaults: Standardizing on a default type (like = any or = string) makes your code easier to use for the common cases.");
console.log("4. Type preservation: Advanced generics allow for complex logic (like merging objects) while maintaining 100% type accuracy.");
