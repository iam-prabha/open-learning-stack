// solution.js - Iterators answers

// TODO 1 & 2
const names = ["Alice", "Bob", "Charlie"];
const it = names[Symbol.iterator]();
console.log("Manually dealing cards:");
console.log(it.next()); // { value: 'Alice', done: false }
console.log(it.next()); // { value: 'Bob', done: false }

// TODO 3
console.log("\nString iteration:");
for (const char of "JavaScript") {
    console.log(char.toUpperCase());
}

// TODO 4 & 5
const countdown = {
    [Symbol.iterator]() {
        let count = 3;
        return {
            next() {
                if (count >= 1) {
                    return { value: count--, done: false };
                } else {
                    return { value: undefined, done: true };
                }
            }
        };
    }
};

const countArr = [...countdown];
console.log(`Countdown Array:`, countArr); // [3, 2, 1]

// TODO 6
// Answer: Must have a method with the key [Symbol.iterator] that returns an iterator.

// CHALLENGE ANSWER
const namesGroup = {
    members: ["Apple", "Banana", "Cherry"],
    [Symbol.iterator]() {
        // We can just reuse the built-in array iterator!
        return this.members[Symbol.iterator]();
    }
};

console.log("\n--- Challenge Iteration ---");
for (const member of namesGroup) {
    console.log(`Member: ${member}`);
}

console.log("\n--- Why it works ---");
console.log("1. Consistency: Symbol.iterator provides a single uniform way for any object to plug into JS features like for...of, spread, and destructuring.");
console.log("2. Laziness: Iterators only compute the 'next' value when asked, which saves memory for large datasets.");
console.log("3. Separation of Concerns: The data (Iterable) and the point-in-time state of looping (Iterator) are separate objects.");
console.log("4. Under the hood: Almost all modern JS APIs (Set, Map, NodeLists) are built using these exact same protocols.");
