// solution.js - Web APIs answers

// TODO 1 & 2
async function getUsers() {
    try {
        const res = await fetch("https://jsonplaceholder.typicode.com/users");
        if (!res.ok) throw new Error("Fetch failed");
        
        const users = await res.json();
        console.log(`First User: ${users[0].name}`);
    } catch (err) {
        console.error(err.message);
    }
}
getUsers();

// TODO 3 & 4
// Saving to LocalStorage
const key = "current_user";
const val = "LearnJS";
if (typeof localStorage !== "undefined") {
    localStorage.setItem(key, val);
    const retrieved = localStorage.getItem(key);
    if (retrieved) console.log(`Welcome, ${retrieved}`);
}

// TODO 5
const params = new URLSearchParams("?theme=dark&lang=en");
console.log(`Theme set to: ${params.get("theme")}`);

// TODO 6
// Answer: A race condition occurs when multiple async requests are in flight 
// and the "wrong" one finishes last, overwriting the "correct" data. 
// e.g. You search for "A", then "AB", but the results for "A" arrive 
// AFTER "AB", showing you the wrong results.

// CHALLENGE ANSWER
async function fetchWithTimeout(url, timeoutMs) {
    const controller = new AbortController();
    const id = setTimeout(() => controller.abort(), timeoutMs);

    try {
        const response = await fetch(url, { signal: controller.signal });
        clearTimeout(id);
        return await response.json();
    } catch (err) {
        if (err.name === "AbortError") {
            console.log("Request timed out and was cancelled.");
        }
        throw err;
    }
}

console.log("\n--- Why it works ---");
console.log("1. Environment: Web APIs like Fetch and Storage are provided by the browser (or specialized Node environments).");
console.log("2. AbortController: This is the standard way to cancel any asynchronous Web API task (like Fetch).");
console.log("3. Persistence: LocalStorage survives page reloads and browser restarts, making it perfect for UI state.");
console.log("4. Parsing: URLSearchParams handles all the complex logic of query strings (like encoding and multiple values) for you.");
