// solution.js - Error Handling answers

// TODO 1
try {
    const data = JSON.parse("{ invalid json }");
} catch (err) {
    console.log("Caught JSON error:", err.message);
}

// TODO 2 & 3 & 4
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

try {
    console.log(`10 / 2 = ${divide(10, 2)}`);
    console.log(`10 / 0 = ${divide(10, 0)}`);
} catch (err) {
    console.error(`Division Error: ${err.message}`);
} finally {
    console.log("Division Operation attempted.");
}

// TODO 5
class ValidationError extends Error {
    constructor(message, field) {
        super(message);
        this.name = "ValidationError";
        this.field = field;
    }
}

// TODO 6
async function fetchSafe() {
    try {
        // await fetchData(); // Simulated call
        throw new Error("Network Down");
    } catch (err) {
        console.error(`Fetch failed safely: ${err.message}`);
    }
}
fetchSafe();

// CHALLENGE ANSWER
function validateEmail(email) {
    if (!email.includes("@")) {
        throw new ValidationError("Invalid email format", "email");
    }
    return true;
}

try {
    validateEmail("bad-email.com");
} catch (err) {
    if (err instanceof ValidationError) {
        console.log(`Validation Failed on [${err.field}]: ${err.message}`);
    }
}

console.log("\n--- Why it works ---");
console.log("1. Control Flow: try/catch changes the execution path, meaning the rest of the 'try' block is skipped as soon as an error occurs.");
console.log("2. Throwing Objects: Using 'new Error()' provides the file name and line number (stack trace), making it much easier to debug.");
console.log("3. Finally: This is the perfect place to hide loading spinners or close database connections, as it's guaranteed to run.");
console.log("4. instanceof: This lets you distinguish between different kinds of errors, allowing you to handle 'NetworkErrors' differently than 'UserErrors'.");
