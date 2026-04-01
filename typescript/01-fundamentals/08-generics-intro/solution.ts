// solution.ts - Generics Intro answers

// TODO 1 & 2
function getFirst<T>(arr: T[]): T {
    return arr[0];
}
const num = getFirst<number>([10, 20]);

// TODO 3 & 4
interface Wrapper<T> {
    value: T;
}
const myNum: Wrapper<number> = { value: 42 };

// TODO 5
class Stack<T> {
    private items: T[] = [];
    push(item: T) { this.items.push(item); }
}

// TODO 6
// Answer: 'any' turns off type-checking entirely. Generics preserve 
// the type information, so if you pass a string in, TS knows for 
// sure you get a string back out.

// CHALLENGE ANSWER
function merge<T extends object, U extends object>(obj1: T, obj2: U): T & U {
    return { ...obj1, ...obj2 };
}

console.log("\n--- Why it works ---");
console.log("1. Flexibility: Generics allow a single piece of code to work with multiple data types without sacrificing safety.");
console.log("2. Type Preservation: Unlike 'any', generics maintain the relationship between input and output types.");
console.log("3. Reusability: You can build a single 'Storage' or 'Queue' class that works for strings, numbers, or complex users.");
console.log("4. Autocomplete: Because TS knows what T is at runtime, it provides full IntelliSense for the returned generic data.");
