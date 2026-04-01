// exercise.js - Practice with variables

// TODO 1: Declare a constant 'DAYS_IN_WEEK' and set it to 7.
// const DAYS_IN_WEEK = ...

// TODO 2: Declare a let variable 'currentAge' and set it to your age.
// Then increment it by 1 on the next line.
// let currentAge = ...
// currentAge = ...

// TODO 3: Create a block (curly braces { }) and declare a 'let' variable 
// inside it. Try to console.log it OUTSIDE the block and catch the error.
/*
{
  ...
}
console.log(...)
*/

// TODO 4: Compare 'var' and 'let' hoisting. 
// Try to log a 'var' before it is declared, and then do the same with a 'let'.
// Observe which one crashes the program.

// TODO 5: Create a 'const' object 'settings' with a property 'theme: "dark"'.
// Change the theme to "light" without re-assigning the whole object.
/*
const settings = ...
settings.theme = ...
*/

// TODO 6: Declare three variables on one line using commas.
// let x = 1, y = 2, ...

// CHALLENGE: Explain WHY 'const' is preferred over 'let' in most modern 
// JS style guides (like Airbnb or Google).

// --- Verification ---
console.log("--- Results ---");
try {
    console.log(`Days in week: ${DAYS_IN_WEEK}`);
    console.log(`Age: ${currentAge}`);
    console.log(`Theme: ${settings.theme}`);
} catch (e) {
    console.log("Error: fill in all TODOs to see results!");
}
