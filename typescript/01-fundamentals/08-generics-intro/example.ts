// example.ts - Reusable, Type-safe Components with Generics

// 1. Generic Function
// The <T> is a placeholder for the type
function identity<T>(arg: T): T {
    return arg;
}

console.log("--- Generic Functions ---");
let output1 = identity<string>("Hello");
let output2 = identity<number>(100);
console.log(`Identity string: ${output1}`);
console.log(`Identity number: ${output2}`);

// 2. Generic Interfaces
interface Box<T> {
    content: T;
}

const stringBox: Box<string> = { content: "Present" };
const numBox: Box<number> = { content: 5 };

console.log("\n--- Generic Interfaces ---");
console.log(`Box has: ${stringBox.content}`);

// 3. Generic Classes
class DataStorage<T> {
    private data: T[] = [];

    addItem(item: T) {
        this.data.push(item);
    }

    getItems(): T[] {
        return this.data;
    }
}

const textStore = new DataStorage<string>();
textStore.addItem("A");
textStore.addItem("B");
console.log("\n--- Generic Classes ---");
console.log(textStore.getItems());

// 4. Multiple Type Parameters
function pair<T, U>(first: T, second: U): [T, U] {
    return [first, second];
}

const myPair = pair<number, string>(1, "Apple");
console.log("\n--- Multiple Params ---");
console.log(myPair);
