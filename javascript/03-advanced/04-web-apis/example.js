// example.js - Interacting with Web APIs

// 1. Fetch API (Network Requests)
async function getRandomJoke() {
    console.log("--- Fetch API ---");
    try {
        const response = await fetch("https://official-joke-api.appspot.com/random_joke");
        if (!response.ok) throw new Error("Network error!");
        
        const joke = await response.json();
        console.log(`Joke: ${joke.setup} ... ${joke.punchline}`);
    } catch (err) {
        console.error(`Fetch failed: ${err.message}`);
    }
}
// getRandomJoke(); // Only works in browser or Node 18+

// 2. Storage API (Persistence)
function persistenceDemo() {
    console.log("\n--- Storage API ---");
    const name = "Alice";
    
    // Save to LocalStorage
    // localStorage.setItem("username", name);
    // console.log("Saved to storage:", localStorage.getItem("username"));
    console.log("Note: Storage requires a browser context.");
}
persistenceDemo();

// 3. Web Worker (Multi-threading)
function workerCheck() {
    console.log("\n--- Workers Check ---");
    if (typeof Worker !== "undefined") {
        console.log("Web Workers are supported! 🚀");
        // const myWorker = new Worker("worker.js");
    } else {
        console.log("Workers not supported in this environment (likely Node).");
    }
}
workerCheck();

// 4. URL API (Formatting)
const currentUrl = new URL("https://example.com/search?q=javascript");
console.log("\n--- URL API ---");
console.log(`Host: ${currentUrl.hostname}`);
console.log(`Path: ${currentUrl.pathname}`);
console.log(`Query: ${currentUrl.searchParams.get("q")}`);
