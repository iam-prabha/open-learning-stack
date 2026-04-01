// exercise.js - Practice with async/await

// TODO 1: Create an async function 'sayHello' that 
// waits for 500ms and then returns "Hello!".

// TODO 2: Call 'sayHello' and log the result to the console.
/*
async function run() {
  const result = ...
  console.log(result);
}
*/

// TODO 3: Create an async function 'fetchNumber' that 
// returns a random number after 200ms.

// TODO 4: Write another async function 'addNumbers' that 
// waits for two separate 'fetchNumber' calls and returns their sum.

// TODO 5: Rewrite this promise chain to use async/await and try/catch:
/*
fetchData()
  .then(data => console.log(data))
  .catch(err => console.error(err));
*/

// TODO 6: Use Promise.all inside an async function to wait for 
// three 'fetchNumber' calls at once and log the final array.

// CHALLENGE: Create a function 'retryFetch(func, retries)' 
// that attempts to run an async function 'retries' number 
// of times before finally throwing an error.

// --- Verification ---
console.log("--- Results ---");
try {
    // run();
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
