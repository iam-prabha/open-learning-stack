// example.js - Mastering Promises in JavaScript

// 1. Creating a Promise
const myPromise = new Promise((resolve, reject) => {
    const success = true;
    setTimeout(() => {
        if (success) {
            resolve("Data received! ✅");
        } else {
            reject("Connection failed! ❌");
        }
    }, 1000);
});

console.log("--- Starting Promise ---");

// 2. Consuming a Promise (.then, .catch, .finally)
myPromise
    .then(data => {
        console.log(`Success: ${data}`);
        return "Next step..."; // Passing data to the next chain
    })
    .then(nextData => {
        console.log(`Chained: ${nextData}`);
    })
    .catch(error => {
        console.error(`Error: ${error}`);
    })
    .finally(() => {
        console.log("Done: Resources cleaned up.");
    });

// 3. Promise.all (Parallel execution)
const p1 = Promise.resolve("Result 1");
const p2 = new Promise(resolve => setTimeout(() => resolve("Result 2"), 500));
const p3 = Promise.resolve("Result 3");

console.log("\n--- Promise.all ---");
Promise.all([p1, p2, p3])
    .then(results => {
        console.log(`All Results:`, results);
    });

// 4. Promise.race (First one to finish wins)
const fast = new Promise(resolve => setTimeout(() => resolve("Winner!"), 100));
const slow = new Promise(resolve => setTimeout(() => resolve("Too slow"), 500));

console.log("\n--- Promise.race ---");
Promise.race([fast, slow])
    .then(winner => {
        console.log(`Race Result: ${winner}`);
    });
