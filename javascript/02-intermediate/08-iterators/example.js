// example.js - Mastering Iteration in JavaScript

// 1. Built-in Iterables (Arrays, Strings)
const list = ["A", "B", "C"];
console.log("--- for...of loop ---");
for (const item of list) {
    console.log(item);
}

// 2. Manual Iteration (The under-the-hood mechanism)
const iterator = list[Symbol.iterator]();
console.log("\n--- Manual next() ---");
console.log(iterator.next()); // { value: 'A', done: false }
console.log(iterator.next()); // { value: 'B', done: false }
console.log(iterator.next()); // { value: 'C', done: false }
console.log(iterator.next()); // { value: undefined, done: true }

// 3. Custom Iterators (Making your object loopable)
const range = {
    from: 1,
    to: 3,
    [Symbol.iterator]() {
        // Return an iterator object
        let current = this.from;
        const last = this.to;
        return {
            next() {
                if (current <= last) {
                    return { value: current++, done: false };
                } else {
                    return { value: undefined, done: true };
                }
            }
        };
    }
};

console.log("\n--- Custom range object iteration ---");
for (const num of range) {
    console.log(num); // 1, 2, 3
}

// 4. Spread and Array.from (Works on any iterable)
const rangeArray = [...range];
console.log("\n--- Spread to Array ---");
console.log(rangeArray);
