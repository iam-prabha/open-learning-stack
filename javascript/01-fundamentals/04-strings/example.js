// example.js - Modern String handling in JavaScript

// 1. Template Literals (Interpolation)
const name = "Alice";
const greeting = `Hello, ${name}! Welcome to JS.`;
console.log("--- Template Literals ---");
console.log(greeting);

// 2. Multi-line Strings
const htmlTemplate = `
<div>
  <h1>Title</h1>
  <p>Description here...</p>
</div>
`;
console.log("\n--- Multi-line ---");
console.log(htmlTemplate.trim());

// 3. Useful String Methods
const text = "  JavaScript is awesome!  ";

console.log("\n--- Methods ---");
console.log(`Length: ${text.length}`);
console.log(`Trimmed: '${text.trim()}'`);
console.log(`Lowercase: ${text.toLowerCase()}`);
console.log(`Result of includes('awesome'): ${text.includes('awesome')}`);
console.log(`Result of startsWith(' '): ${text.startsWith(' ')}`);

// 4. Slicing and Splitting
const phrase = "The quick brown fox";
const words = phrase.split(" "); // ["The", "quick", "brown", "fox"]

console.log("\n--- Slice & Split ---");
console.log(`Words Array:`, words);
console.log(`Sliced (0-3): ${phrase.slice(0, 3)}`);

// 5. Immutability Demo
let myStr = "hello";
myStr.toUpperCase(); // This returns "HELLO"
console.log(`\nOriginal myStr: ${myStr}`); // Still "hello"!
myStr = myStr.toUpperCase(); // This updates the variable
console.log(`Updated myStr: ${myStr}`);
