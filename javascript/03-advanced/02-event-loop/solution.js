// solution.js - Event Loop answers

// TODO 1
// Answer: A, D, C, B

// TODO 2
console.log("Step 1");
Promise.resolve().then(() => console.log("Step 1.5"));
setTimeout(() => console.log("Step 2"), 0);

// TODO 3
// Answer: Microtasks (Promises, queueMicrotask) are processed immediately after 
// the call stack is clear, BEFORE the next event loop tick. 
// Macrotasks (setTimeout, setInterval) are processed in the next tick.

// TODO 4
Promise.resolve("One").then(res => {
    console.log(res);
    return "Two";
}).then(res => console.log(res));

// TODO 5
queueMicrotask(() => console.log("Manual Microtask"));

// TODO 6
// Answer: It only guarantees that the task is added to the queue AFTER 1000ms. 
// If the call stack is busy (blocking), the task will wait until the stack is clear.

// CHALLENGE ANSWER
function performChunked(n) {
    let i = 0;
    function nextChunk() {
        const start = i;
        // Process 1000 items at a time
        while (i < start + 1000 && i < n) {
            // Do work...
            i++;
        }
        if (i < n) {
            console.log(`Chunked at ${i}...`);
            setTimeout(nextChunk, 0); // Give the event loop a "breath"
        } else {
            console.log("Done!");
        }
    }
    nextChunk();
}

// performChunked(5000);

console.log("\n--- Why it works ---");
console.log("1. Single Thread: The Chef (JS) can't cook two things at once, so the order is strict.");
console.log("2. Microtask Priority: Promises are handled as soon as the current script finishes, allowing for 'near-instant' async updates.");
console.log("3. Non-blocking: This architecture is why JS is so good for I/O heavy tasks like web servers and UI interactions.");
console.log("4. Fairness: The event loop ensures that UI rendering and user inputs aren't ignored forever even if multiple tasks are queued.");
