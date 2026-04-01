// solution.js - Promises answers

// TODO 1
function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// TODO 2
wait(1000).then(() => console.log("Hello after 1s"));

// TODO 3 & 4
const checkRandom = new Promise((resolve, reject) => {
    const num = Math.random();
    if (num >= 0.5) {
        resolve(`Success: ${num}`);
    } else {
        reject(`Oops! ${num} was too low`);
    }
});

checkRandom
    .then(msg => console.log(msg))
    .catch(err => console.error(err));

// TODO 5
Promise.resolve(5)
    .then(n => n * 2) // 10
    .then(n => n * 2) // 20
    .then(n => n * 2) // 40
    .then(res => console.log(`Chain Result: ${res}`));

// TODO 6
const p1 = Promise.resolve("Alice");
const p2 = Promise.resolve("Bob");
const p3 = Promise.resolve("Charlie");

Promise.all([p1, p2, p3]).then(names => {
    console.log(`Fetched names: ${names}`);
});

// CHALLENGE ANSWER
function delayedError() {
    return new Promise((_, reject) => {
        setTimeout(() => reject("Timed out"), 3000);
    });
}

// --- Verification ---
console.log("--- Verification ---");
console.log("Running async tests...");

console.log("\n--- Why it works ---");
console.log("1. State Machine: A promise is ALWAYS in one of three states: pending, fulfilled, or rejected.");
console.log("2. Immutability: Once a promise resolves or rejects, its value CANNOT change.");
console.log("3. Chaining: Returning a value from .then() wraps it in a new promise automatically.");
console.log("4. Promise.all: Useful for speed — it starts all tasks at once rather than waiting for each one.");
