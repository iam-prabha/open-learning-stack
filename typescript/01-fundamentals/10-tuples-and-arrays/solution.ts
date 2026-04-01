// solution.ts - Arrays and Tuples answers

// TODO 1
const prices: number[] = [10, 20, 30];

// TODO 2
const rgb: [number, number, number] = [255, 0, 128];

// TODO 3
function sumPair(pair: [number, number]): number {
    return pair[0] + pair[1];
}

// TODO 4
const days: readonly string[] = ["Mon", "Tue", "Wed"];
// days.push("Thu"); // Error: Property 'push' does not exist on type 'readonly string[]'

// TODO 5
const userStatus: [string, number] = ["online", 1];
const [statusText, statusCode] = userStatus;

// TODO 6
// Answer: Readability. In a tuple, you only know elements by index ([0], [1]). 
// In an object, you have keys (id, name, age) which describe the data's 
// meaning, making the code much easier for others to read and maintain.

// CHALLENGE ANSWER
type Pair<T> = [T, T];
const coordPair: Pair<number> = [10, 20];
const stringPair: Pair<string> = ["Hello", "World"];

console.log("\n--- Why it works ---");
console.log("1. Predictability: Tuples ensure that data follows a specific sequence, which is perfect for coordinate pairs or key-value pairs from Object.entries().");
console.log("2. Immutability: Readonly arrays/tuples help prevent unintentional changes to your data, leading to fewer state-related bugs.");
console.log("3. Destructuring: TS knows exactly what types are at each index of a tuple, providing safe destructuring with full IDE support.");
console.log("4. Type-safety: Unlike JS arrays, TS ensures you don't accidentally mix 'Apples' and 'Oranges' in the same list unless you explicitly allow it.");
