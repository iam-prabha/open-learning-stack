// exercise.js - Practice with Iterators

// TODO 1: Extract the iterator from this array using Symbol.iterator:
// const names = ["Alice", "Bob", "Charlie"];
// const it = ...

// TODO 2: Manually call it.next() twice and log the results.

// TODO 3: Use a 'for...of' loop to iterate over the string "JavaScript".

// TODO 4: Create a custom iterable 'counter' that yields 3, 2, 1 
// and then stops. (Implement [Symbol.iterator])
/*
const countdown = {
  [Symbol.iterator]() { ... }
};
*/

// TODO 5: Use the spread operator (...) to convert your 'countdown' 
// object into an array.
// const countArr = ...

// TODO 6: What property must an object have to be considered "Iterable"?
// Answer: ...

// CHALLENGE: Create an object 'namesGroup' that has a 'members' array 
// and allows direct iteration over the 'members' using 'for...of' on the object itself.

// --- Verification ---
console.log("--- Results ---");
try {
    // console.log(`Names Iterator:`, it.next());
    // for (const val of countdown) console.log(val);
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
