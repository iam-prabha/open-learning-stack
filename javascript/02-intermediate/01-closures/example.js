// example.js - Understanding Closures and Lexical Scope

// 1. Basic Closure
function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
        console.log(`Outer: ${outerVariable}`);
        console.log(`Inner: ${innerVariable}`);
    };
}

const newFunction = outerFunction("outside");
newFunction("inside"); // Still remembers "outside"!

// 2. Private Variables (Data Encapsulation)
function createCounter() {
    let count = 0; // This variable is private!
    
    return {
        increment: () => ++count,
        decrement: () => --count,
        getCount: () => count
    };
}

const myCounter = createCounter();
console.log("\n--- Private Counter ---");
console.log(myCounter.increment()); // 1
console.log(myCounter.increment()); // 2
// count = 10; // Error: count is not accessible here
console.log(`Total count: ${myCounter.getCount()}`);

// 3. Function Factories
function makeAdder(x) {
    return function(y) {
        return x + y;
    };
}

const add5 = makeAdder(5);
const add10 = makeAdder(10);

console.log("\n--- Function Factory ---");
console.log(`Add 5 to 2:  ${add5(2)}`); // 7
console.log(`Add 10 to 2: ${add10(2)}`); // 12

// 4. Closures in a Loop (The 'let' vs 'var' difference)
console.log("\n--- Loop Closures ---");
for (let i = 1; i <= 3; i++) {
    // Each iteration of let creates a NEW binding for 'i'
    setTimeout(() => {
        console.log(`Iteration ${i}`);
    }, 100);
}
