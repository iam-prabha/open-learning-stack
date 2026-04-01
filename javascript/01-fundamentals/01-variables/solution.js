// solution.js - Variable answers

// TODO 1
const DAYS_IN_WEEK = 7;

// TODO 2
let currentAge = 30;
currentAge += 1;

// TODO 3
try {
    {
        let secret = "hidden";
    }
    // console.log(secret); // This would crash
} catch (e) {
    console.log("Caught expected scope error.");
}

// TODO 4
console.log(`var status: ${hoisted}`); // undefined
var hoisted = "Value";

try {
    // console.log(notHoisted); // ReferenceError
    let notHoisted = "Value";
} catch (e) {
    console.log("Caught expected TDZ error for let.");
}

// TODO 5
const settings = { theme: "dark" };
settings.theme = "light";

// TODO 6
let a = 1, b = 2, c = 3;

// CHALLENGE ANSWER
// 'const' is preferred because it conveys INTENT. It tells the reader (and the engine)
// that this name will not be pointing to a different value later. 
// This reduces mental overhead when reading code and prevents accidental re-assignments.

// --- Verification ---
console.log("--- Verification ---");
console.log(`Days in week: ${DAYS_IN_WEEK}`);
console.log(`Age: ${currentAge}`);
console.log(`Theme: ${settings.theme}`);
console.log(`Multiple variables: ${a}, ${b}, ${c}`);

console.log("\n--- Why it works ---");
console.log("1. 'const' prevents re-binding, but NOT mutation of objects/arrays.");
console.log("2. 'let' and 'const' are block-scoped — they stay inside { }.");
console.log("3. 'var' is function-scoped and 'hoists' its declaration (but not value) to the top.");
console.log("4. TDZ (Temporal Dead Zone) is safe mode: it forces you to declare before use.");
