// solution.js - Closures answers

// TODO 1
function greet(message) {
    return function(name) {
        console.log(`${message}, ${name}!`);
    };
}

// TODO 2
function createSecret(initialSecret) {
    let secret = initialSecret;
    return {
        getSecret: () => secret,
        setSecret: (newSecret) => { secret = newSecret; }
    };
}

// TODO 3
function makeMultiplier(x) {
    return (y) => x * y;
}

// TODO 4
// Fix: change 'var' to 'let'
for (let i = 1; i <= 3; i++) {
    setTimeout(() => console.log(`Fixed Loop: ${i}`), 100);
}

// TODO 5
function bankAccount(initialBalance) {
    let balance = initialBalance;
    return {
        deposit: (amount) => { balance += amount; },
        withdraw: (amount) => {
            if (amount > balance) return "Insufficient funds";
            balance -= amount;
        },
        getBalance: () => balance
    };
}

// TODO 6
function once(func) {
    let called = false;
    return function(...args) {
        if (!called) {
            called = true;
            return func(...args);
        }
    };
}

// CHALLENGE ANSWER
function memoize(func) {
    const cache = {};
    return function(...args) {
        const key = JSON.stringify(args);
        if (key in cache) {
            console.log("Fetching from cache...");
            return cache[key];
        }
        const result = func(...args);
        cache[key] = result;
        return result;
    };
}

// --- Verification ---
console.log("--- Verification ---");
const sayHello = greet("Hello");
sayHello("Alice");

const myAcc = bankAccount(100);
myAcc.deposit(50);
console.log(`Balance: ${myAcc.getBalance()}`);

const logOnce = once(msg => console.log(`Called with: ${msg}`));
logOnce("first");
logOnce("second"); // Does nothing

const slowAdd = (a, b) => a + b;
const memoAdd = memoize(slowAdd);
console.log(`MemoAdd(2, 3): ${memoAdd(2, 3)}`);
console.log(`MemoAdd(2, 3): ${memoAdd(2, 3)}`); // Cache hit

console.log("\n--- Why it works ---");
console.log("1. Data Privacy: Closures are the only way in JS (pre-ES2022) to truly keep data 'private'.");
console.log("2. Memory: The 'inner' function keeps a link to the 'outer' variables, preventing them from being deleted.");
console.log("3. Function Scope: 'let' creates a new scope for every loop iteration, which is why it fixes the loop trap.");
console.log("4. Factories: Closures allow you to 'pre-configure' functions with specific state.");
