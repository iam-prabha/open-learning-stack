// solution.js - Proxy and Reflect answers

// TODO 1 & 2 & 4
const data = { id: 1, text: "hello", _secret: "don't look!" };
const proxyData = new Proxy(data, {
    get(target, prop, receiver) {
        if (typeof prop === "string" && prop.startsWith("_")) {
            return "Secret";
        }
        console.log(`Accessing ${prop}`);
        return Reflect.get(target, prop, receiver);
    }
});

// TODO 3
const product = { name: "Pen", price: 15 };
const proxyProduct = new Proxy(product, {
    set(target, prop, value, receiver) {
        if (prop === "price" && (typeof value !== "number" || value <= 10)) {
            throw new Error("Price must be a number > 10");
        }
        return Reflect.set(target, prop, value, receiver);
    },
    // TODO 5
    has(target, prop) {
        return prop in target; // Simple form
    }
});

// TODO 6
// Answer: 'receiver' refers to the object where the operation was 
// originally performed. This is important for handling inherited 
// properites and ensuring 'this' binds correctly during Reflect calls.

// CHALLENGE ANSWER
const arr = [10, 20, 30];
const proxyArr = new Proxy(arr, {
    get(target, prop, receiver) {
        let index = Number(prop);
        if (index < 0) {
            index = target.length + index; // e.g. 3 + (-1) = 2
        }
        return Reflect.get(target, index, receiver);
    }
});

// --- Verification ---
console.log("--- Verification ---");
console.log(`Names: ${proxyData.text}, ${proxyData._secret}`);
proxyProduct.price = 20; 
console.log(`Price set: ${proxyProduct.price}`);
console.log(`Array[-1]: ${proxyArr[-1]}`); // 30

console.log("\n--- Why it works ---");
console.log("1. Interception: Proxy traps let you 'jump in' before an action happens, allowing for logic like validation without changing the target object.");
console.log("2. Consistency: Reflect provides the default original behavior. It returns a boolean for set/delete, making it easier to follow the Proxy protocols.");
console.log("3. Meta-programming: Proxies allow building abstractions like observable data (Vue 3) or smart mocking in tests.");
console.log("4. Encapsulation: You can make any property 'appear' private or even hidden entirely using the 'has' and 'get' traps.");
