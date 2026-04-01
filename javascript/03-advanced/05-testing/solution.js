// solution.js - Testing answers

// TODO 1
/*
test("multiply 2 * 3", () => {
    expect(multiply(2, 3)).toBe(6);
});
*/

// TODO 2
/*
test("greet returns correct message", () => {
    expect(greet("Alice")).toBe("Hello Alice");
});
*/

// TODO 3
/*
test("array contains item1", () => {
    expect(getArray()).toContain("item1");
});
*/

// TODO 4
// Answer: Use jest.mock() or jest.fn(). 
// e.g. apiCall.mockReturnValue({ success: true });

// TODO 5
// Answer: 'toBe' checks for reference equality (same object in memory). 
// 'toEqual' checks for deep equality (same values inside the object).

// TODO 6
// Answer: 'beforeEach' runs before every individual test, ensuring 
// a fresh state (like a new database connection or reset variables).

// CHALLENGE ANSWER
function assert(actual, expected, message) {
    if (actual !== expected) {
        throw new Error(`FAIL: ${message} (Expected ${expected}, got ${actual})`);
    }
    console.log(`PASS: ${message}`);
}

// --- Verification ---
console.log("--- Verification (Manual) ---");
assert(5, 5, "Sum test basic");
try {
    assert(5, 10, "Failure test");
} catch (err) {
    console.log(`Caught expected failure: ${err.message}`);
}

console.log("\n--- Why it works ---");
console.log("1. Assertions: These are the core of testing — a statement of truth that the code must satisfy.");
console.log("2. Mocking: Letting you test code in isolation from external services (Database, API, File System).");
console.log("3. Automation: Once written, tests can run every time you save a file, catching bugs within seconds.");
console.log("4. Shared Logic: describe/test structures provide a hierarchical view of your app's requirements.");
