// exercise.js - Practice with Proxy and Reflect

// TODO 1: Create a proxy for this 'data' object that logs 
// "Accessing [prop]" every time a property is read.
// const data = { id: 1, text: "hello" };

// TODO 2: Improve the proxy to return "Secret" if the user 
// tries to access any property starting with an underscore (_).

// TODO 3: Create a 'set' trap that validates that 'price' 
// must be a number greater than 10.
/*
const product = { name: "Pen", price: 15 };
const proxyProduct = new Proxy(product, {
  set(...) { ... }
});
*/

// TODO 4: Use Reflect.get() inside your proxy instead of target[prop].

// TODO 5: Implement the 'has' trap to return false for 
// any property that doesn't exist on the original object 
// (even if you'd normally get undefined).

// TODO 6: What is the third argument 'receiver' in the get trap for?
// Answer: ...

// CHALLENGE: Create a "Negative Index" array proxy that allows 
// accessing elements from the end using negative numbers.
// e.g. proxyArr[-1] returns the last item.

// --- Verification ---
console.log("--- Results ---");
try {
    // console.log(`-1 index: ${proxyArr[-1]}`);
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
