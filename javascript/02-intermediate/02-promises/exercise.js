// exercise.js - Practice with Promises

// TODO 1: Create a promise 'wait(ms)' that resolves 
// after the given number of milliseconds.

// TODO 2: Use your 'wait' function to log "Hello" after 1 second.

// TODO 3: Create a promise that rejects with "Oops!" if a number 
// is less than 0.5 (simulate random failure).
/*
const checkRandom = new Promise((resolve, reject) => {
  const num = Math.random();
  ...
});
*/

// TODO 4: Use .catch() to handle the potential error from 'checkRandom'.

// TODO 5: Chain three promises together. Each step should return 
// a number multiplied by 2. (Start with 5 -> 10 -> 20 -> 40).
/*
Promise.resolve(5)
  .then(...)
  .then(...)
  ...
*/

// TODO 6: Use Promise.all to fetch these three names concurrently:
// const p1 = Promise.resolve("Alice");
// const p2 = Promise.resolve("Bob");
// const p3 = Promise.resolve("Charlie");

// CHALLENGE: Create a function 'delayedError' that returns a promise 
// which rejects with "Timed out" after 3 seconds.

// --- Verification ---
console.log("--- Results ---");
try {
    // Test your code here
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
