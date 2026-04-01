// example.js - Mastering Arrays in JavaScript

// 1. Creation and Manipulation
const colors = ["red", "green"];
colors.push("blue");      // Add to back
colors.unshift("yellow"); // Add to front
console.log("--- Manipulation ---");
console.log(`Array after push/unshift:`, colors);

const lastColor = colors.pop(); // Remove "blue"
console.log(`Popped item: ${lastColor}`);

// 2. Powerful Methods (Map, Filter, Reduce)
const nums = [1, 2, 3, 4, 5];
const doubled = nums.map(n => n * 2);
const evens = nums.filter(n => n % 2 === 0);
const sum = nums.reduce((acc, curr) => acc + curr, 0);

console.log("\n--- Functional Methods ---");
console.log(`Doubled: ${doubled}`);
console.log(`Evens:   ${evens}`);
console.log(`Sum:     ${sum}`);

// 3. Slice vs Splice
const days = ["Mon", "Tue", "Wed", "Thu", "Fri"];
const midWeek = days.slice(1, 3); // ["Tue", "Wed"] - Copy
console.log("\n--- Slice vs Splice ---");
console.log(`Slice (copy 1-3):`, midWeek);

const removed = days.splice(0, 1); // Removes "Mon" from original!
console.log(`After Splice(0, 1):`, days);

// 4. Spread and Destructuring
const moreDays = ["Sat", "Sun"];
const allDays = [...days, ...moreDays]; // Merge arrays
const [tuesday, wednesday, ...rest] = allDays; // Destructure

console.log("\n--- ES6 Features ---");
console.log(`Merged:`, allDays);
console.log(`First variable: ${tuesday}`);
console.log(`Remaining items:`, rest);

// 5. Indexing and Searching
console.log("\n--- Searching ---");
console.log(`Index of 'Wed': ${allDays.indexOf("Wed")}`);
console.log(`Includes 'Sat'? ${allDays.includes("Sat")}`);
