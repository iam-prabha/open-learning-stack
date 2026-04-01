// example.js - Modern Asynchronous JavaScript

// Simulating a delay
const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// 1. Basic async/await
async function fetchData() {
    console.log("Fetching...");
    await wait(1000); // Wait for 1s
    return { id: 1, name: "Alice" };
}

// 2. Handling errors with try/catch
async function runDemo() {
    try {
        const user = await fetchData();
        console.log(`User found: ${user.name}`);
    } catch (error) {
        console.error(`Error fetching: ${error}`);
    } finally {
        console.log("Fetch cycle complete.");
    }
}

console.log("--- Starting Async Demo ---");
runDemo();

// 3. Parallel execution with Promise.all
async function fetchConfig() {
    console.log("\nFetching config in parallel...");
    // These run at the SAME time
    const [theme, lang] = await Promise.all([
        wait(500).then(() => "dark"),
        wait(500).then(() => "en")
    ]);
    console.log(`Config: ${theme}, ${lang}`);
}
fetchConfig();

// 4. Sequential vs Parallel Trap
async function sequential() {
    const start = Date.now();
    await wait(500);
    await wait(500);
    console.log(`Sequential took: ${Date.now() - start}ms`); // ~1000ms
}
sequential();
