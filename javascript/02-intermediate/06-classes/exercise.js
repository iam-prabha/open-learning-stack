// exercise.js - Practice with Classes

// TODO 1: Create a class 'Book' with a constructor that 
// takes 'title', 'author', and 'pages'.

// TODO 2: Add a method 'read()' to 'Book' that logs 
// "Reading ${title} by ${author}...".

// TODO 3: Create an instance of 'Book' and call the 'read' method.

// TODO 4: Create a class 'EBook' that extends 'Book' and 
// takes an additional 'fileSize' property in the constructor.
// (Don't forget to call super!)

// TODO 5: Override the 'read()' method in 'EBook' to log 
// "Downloading ${title} and reading...".

// TODO 6: Create a static method 'isEBook(obj)' on the 'EBook' class 
// that returns true if the object is an instance of EBook.

// CHALLENGE: Create a 'BankAccount' class with a private property '#balance'.
// Add 'deposit(amount)' and 'withdraw(amount)' methods.
// Note: Private fields (#) require modern Node.js or browsers!

// --- Verification ---
console.log("--- Results ---");
try {
    // console.log(`Is EBook? ${EBook.isEBook(new EBook("X", "Y", 1, 5))}`);
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
