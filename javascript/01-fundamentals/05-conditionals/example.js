// example.js - Decision making in JavaScript

// 1. if / else if / else
const hour = 14;

console.log("--- if/else ---");
if (hour < 12) {
    console.log("Good morning!");
} else if (hour < 18) {
    console.log("Good afternoon!");
} else {
    console.log("Good evening!");
}

// 2. The Ternary Operator (condition ? valIfTrue : valIfFalse)
const age = 20;
const status = age >= 18 ? "Adult" : "Minor";

console.log("\n--- Ternary ---");
console.log(`User age is ${age}, Status: ${status}`);

// 3. Switch statement
const day = "Monday";

console.log("\n--- Switch ---");
switch (day) {
    case "Monday":
        console.log("Start of the week!");
        break; // Crucial! Prevents falling through
    case "Friday":
        console.log("Weekend is near.");
        break;
    case "Saturday":
    case "Sunday": // Multiple cases same result
        console.log("Enjoy the weekend!");
        break;
    default:
        console.log("Just another day.");
}

// 4. Truthy and Falsy values
console.log("\n--- Truthy/Falsy check ---");
const values = [0, "", null, undefined, NaN, [], {}];

values.forEach(v => {
    if (v) {
        console.log(`'${v}' is Truthy`);
    } else {
        console.log(`'${v}' is Falsy`);
    }
});
// Note: [] and {} are TRUTHY! Only 0, "", null, undef, NaN are falsy.
