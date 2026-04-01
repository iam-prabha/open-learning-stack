// solution.js - Async / Await answers

const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// TODO 1
async function sayHello() {
    await wait(500);
    return "Hello!";
}

// TODO 2
async function run() {
    const result = await sayHello();
    console.log(result);
}
run();

// TODO 3
async function fetchNumber() {
    await wait(200);
    return Math.floor(Math.random() * 100);
}

// TODO 4
async function addNumbers() {
    const n1 = await fetchNumber();
    const n2 = await fetchNumber();
    return n1 + n2;
}

// TODO 5
async function handleFetch() {
    try {
        const data = await fetchData(); // Assuming fetchData exists
        console.log(data);
    } catch (err) {
        console.error(`Error: ${err}`);
    }
}

// TODO 6
async function fetchInParallel() {
    const results = await Promise.all([
        fetchNumber(),
        fetchNumber(),
        fetchNumber()
    ]);
    console.log(`Parallel numbers: ${results}`);
}
fetchInParallel();

// CHALLENGE ANSWER
async function retryFetch(func, retries) {
    for (let i = 0; i < retries; i++) {
        try {
            return await func();
        } catch (err) {
            if (i === retries - 1) throw err;
            console.log(`Retry ${i + 1} failed, trying again...`);
        }
    }
}

// --- Verification ---
console.log("--- Verification ---");
console.log("Async tests are non-blocking...");

console.log("\n--- Why it works ---");
console.log("1. Readable Flow: It mimics synchronous code, which avoids the 'pyramid of doom' found in deep nesting.");
console.log("2. Unified Errors: You can use the same try/catch block for both synchronous and asynchronous errors.");
console.log("3. Return Type: Async functions ALWAYS return a Promise, even if you return a plain value.");
console.log("4. Context: 'await' only works inside an 'async' function (except for top-level await in modern modules).");
