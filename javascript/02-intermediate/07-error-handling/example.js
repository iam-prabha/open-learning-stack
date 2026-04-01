// example.js - Managing Errors in JavaScript

// 1. Basic try/catch/finally
function parseJSON(json) {
    console.log("--- JSON Parsing ---");
    try {
        const data = JSON.parse(json);
        console.log("Parsed result:", data);
        return data;
    } catch (err) {
        console.error(`Catch: Invalid JSON format! (${err.message})`);
        return null;
    } finally {
        console.log("Finally: Cleanup complete.");
    }
}

parseJSON('{"name": "Alice"}'); // Success
parseJSON('Invalid JSON');      // Failure

// 2. Using 'throw' for Validation
function registerUser(age) {
    console.log("\n--- Validation ---");
    if (age < 18) {
        throw new Error("User must be at least 18 years old.");
    }
    console.log("Registration successful!");
}

try {
    registerUser(15);
} catch (error) {
    console.log(`Error detected: ${error.message}`);
}

// 3. Custom Error Classes
class APIError extends Error {
    constructor(message, status) {
        super(message);
        this.name = "APIError";
        this.status = status;
    }
}

function callAPI() {
    console.log("\n--- Custom Errors ---");
    throw new APIError("Unauthorized Access", 401);
}

try {
    callAPI();
} catch (err) {
    if (err instanceof APIError) {
        console.log(`API Error [${err.status}]: ${err.message}`);
    } else {
        console.log("Generic Error:", err.message);
    }
}
