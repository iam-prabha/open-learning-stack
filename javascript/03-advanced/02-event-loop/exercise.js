// exercise.js - Practice with Event Loop order

// TODO 1: Predict the output order of this code:
/*
console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");
*/
// Your Answer: ...

// TODO 2: Write a snippet that uses 'setTimeout' to log "Step 2" 
// AFTER "Step 1" (Sync) and "Step 1.5" (Microtask).

// TODO 3: What is the main difference between a Microtask and a Macrotask?
// Answer: ...

// TODO 4: Create a Promise that resolves and then chains another .then(). 
// Observe where it lands in the sequence compared to a 0ms setTimeout.

// TODO 5: Use 'queueMicrotask(() => ...)' to manually add a task 
// to the microtask queue without using a Promise.

// TODO 6: Why does 'setTimeout(..., 1000)' NOT guarantee the code runs 
// at exactly 1000ms? 
// Answer: ...

// CHALLENGE: Write a function 'performChunked(n)' that loops n times, 
// but uses 'setTimeout' every 1000 iterations to avoid blocking 
// the event loop for too long.

// --- Verification ---
console.log("--- Results ---");
try {
    // Run your code here and check relative order!
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
