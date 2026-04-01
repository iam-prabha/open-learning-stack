// exercise.js - Practice with Prototypes

// TODO 1: Create a 'parent' object with a property 'role' set to "user".

// TODO 2: Create a 'child' object and set its prototype to 'parent'.

// TODO 3: Log 'child.role'. Then change 'child.role' to "admin" and log it again.
// Verify if 'parent.role' changed or stayed the same.

// TODO 4: Use 'Object.create()' to create a 'square' object that 
// inherits from a 'shape' object (which has a 'type' property).

// TODO 5: Create a constructor function 'Person(name)'. 
// Add a 'greet()' method to 'Person.prototype'.

// TODO 6: Create two instances of 'Person'. 
// Use '=== ' to check if their 'greet' methods are the same exact function.
/*
const p1 = new Person("A");
const p2 = new Person("B");
console.log(p1.greet === p2.greet); // Should be true if using prototype!
*/

// CHALLENGE: Create a custom method 'last()' on 'Array.prototype' 
// that returns the last element of any array.
// [1, 2, 3].last(); // Expected: 3

// --- Verification ---
console.log("--- Results ---");
try {
    // console.log(`Method shared: ${p1.greet === p2.greet}`);
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
