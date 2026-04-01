// solution.js - String answers

// TODO 1
const product = "Laptop";
const price = 999;
console.log(`The ${product} costs $${price}.`);

// TODO 2
const poem = `
Roses are red,
Violets are blue,
JavaScript is cool,
And so are you.
`;

// TODO 3
const message = "  HELLO WORLD  ";
const cleaned = message.trim().toLowerCase();

// TODO 4
const sentence = "I love coding";
const hasLove = sentence.includes("love");

// TODO 5
const csv = "apple,orange,banana";
const fruits = csv.split(",");

// TODO 6
const fullText = "Learning JS is fun";
const onlyJS = fullText.slice(9, 11);

// CHALLENGE ANSWER
function capitalize(word) {
    if (!word) return "";
    return word[0].toUpperCase() + word.slice(1).toLowerCase();
}

// --- Verification ---
console.log("--- Verification ---");
console.log(`Cleaned: '${cleaned}'`);
console.log(`Has 'love'? ${hasLove}`);
console.log(`Fruits:`, fruits);
console.log(`Slice result: ${onlyJS}`);
console.log(`Capitalize('python'): ${capitalize('python')}`);

console.log("\n--- Why it works ---");
console.log("1. Template Literals: Use backticks `` and ${} to embed values directly, avoiding messy + concatenation.");
console.log("2. Chaining: Methods return new strings, allowing you to chain like .trim().toLowerCase().");
console.log("3. Immutability: String methods NEVER change the original string. They return a copy.");
console.log("4. Array-like: You can access characters by index (word[0]) just like in an array.");
