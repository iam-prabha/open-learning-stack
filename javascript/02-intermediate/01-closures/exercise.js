// exercise.js - Practice with Closures

// TODO 1: Create a function 'greet(message)' that returns a function.
// The inner function should take a 'name' and log: "${message}, ${name}!".
/*
const sayHello = greet("Hello");
sayHello("Alice"); // Expected: "Hello, Alice!"
*/

// TODO 2: Create a function 'createSecret(secret)' that returns an object 
// with two methods: 'getSecret()' and 'setSecret(newSecret)'.
// Use a closure to keep the 'secret' variable private.

// TODO 3: Write a function factory 'makeMultiplier(x)' that returns 
// a function that multiplies its input by 'x'.
/*
const double = makeMultiplier(2);
console.log(double(10)); // Expected: 20
*/

// TODO 4: Fix the loop closure problem below so it logs 1, 2, 3 
// instead of 4, 4, 4. (Hint: change 'var' to 'let')
/*
for (var i = 1; i <= 3; i++) {
  setTimeout(() => console.log(i), 100);
}
*/

// TODO 5: Create a function 'bankAccount(initialBalance)' that returns 
// an object with 'deposit(amount)', 'withdraw(amount)', and 'getBalance()'.
// The balance should be impossible to modify directly from outside.

// TODO 6: Use a closure to create a 'once(func)' function.
// It should take a function and return a version of it that can 
// only be called ONCE. Subsequent calls should do nothing.

// CHALLENGE: Create a function 'memoize(func)' that takes a function 
// and returns a version that caches results for the same inputs.

// --- Verification ---
console.log("--- Results ---");
try {
    // Test your code here
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
