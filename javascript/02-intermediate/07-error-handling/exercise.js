// exercise.js - Practice with Error Handling

// TODO 1: Wrap this JSON.parse call in a try/catch block:
// const data = JSON.parse("{ invalid json }");

// TODO 2: Write a function 'divide(a, b)' that throws an Error 
// with the message "Cannot divide by zero" if b is 0.

// TODO 3: Call your 'divide' function inside a try/catch block 
// and log the error message if it fails.

// TODO 4: Use a 'finally' block to log "Operation attempted" 
// whether the division succeeded or failed.

// TODO 5: Create a custom error class 'ValidationError' that 
// extends Error and includes a 'field' property in the constructor.

// TODO 6: Write an async function 'fetchSafe()' that calls 
// an imaginary 'fetchData()' function and catches any errors.
/*
async function fetchSafe() {
  try {
    await fetchData();
  } catch (err) { ... }
}
*/

// CHALLENGE: Create a function 'validateEmail(email)' that throws 
// a ValidationError if the email doesn't contain an "@" symbol.

// --- Verification ---
console.log("--- Results ---");
try {
    // Test your code here
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
