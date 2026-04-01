// example.js - Meta-programming with Proxy and Reflect

// 1. Basic Interception (The 'get' trap)
const user = { name: "Alice", age: 25 };

const proxyUser = new Proxy(user, {
    get(target, prop, receiver) {
        console.log(`Reading property: ${prop}`);
        // Using Reflect to perform the default operation
        return Reflect.get(target, prop, receiver) || "N/A";
    }
});

console.log("--- Get Trap ---");
console.log(proxyUser.name); // Alicia (Logged: Reading property: name)
console.log(proxyUser.job);  // N/A (Logged: Reading property: job)

// 2. Data Validation (The 'set' trap)
const validator = {
    set(target, prop, value) {
        if (prop === "age") {
            if (typeof value !== "number" || value < 0) {
                throw new Error("Age must be a positive number.");
            }
        }
        console.log(`Updating ${prop} to ${value}...`);
        return Reflect.set(target, prop, value);
    }
};

const secureUser = new Proxy(user, validator);
console.log("\n--- Set Trap ---");
secureUser.age = 30; // Works
// secureUser.age = -5; // Throws Error

// 3. Deletion and 'in' Interception
const secretObj = { _id: 123, publicData: "Hello" };
const guardedObj = new Proxy(secretObj, {
    deleteProperty(target, prop) {
        if (prop.startsWith("_")) {
            console.log(`Permission denied: Cannot delete ${prop}`);
            return false;
        }
        return Reflect.deleteProperty(target, prop);
    },
    has(target, prop) {
        if (prop.startsWith("_")) return false; // Hide private fields
        return Reflect.has(target, prop);
    }
});

console.log("\n--- 'delete' and 'in' ---");
console.log(`Is _id in object? ${"_id" in guardedObj}`); // false
delete guardedObj._id; // Denied
console.log(`_id still exists:`, secretObj._id);
