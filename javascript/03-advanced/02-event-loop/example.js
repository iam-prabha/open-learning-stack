// example.js - Visualizing the Event Loop

console.log("1: Start (Synchronous)");

// 1. Macrotask (Timeout)
setTimeout(() => {
    console.log("5: Timeout (Macrotask)");
}, 0);

// 2. Microtask (Promise)
Promise.resolve().then(() => {
    console.log("3: Promise 1 (Microtask)");
}).then(() => {
    console.log("4: Promise 2 (Microtask)");
});

console.log("2: End (Synchronous)");

/* 
EXPECTED ORDER:
1: Start (Sync)
2: End (Sync)
--- Stack is clear, checking Microtasks ---
3: Promise 1 (Micro)
4: Promise 2 (Micro)
--- Microtask queue is clear, checking Macrotasks ---
5: Timeout (Macro)
*/

// 3. Blocking the Loop Demo (Don't do this in production!)
function block(ms) {
    const start = Date.now();
    while (Date.now() - start < ms) { }
    console.log(`Block finished after ${ms}ms`);
}

// console.log("\n--- Blocking Demo ---");
// block(1000); // This would prevent 'Timeout' from running for an extra second!
