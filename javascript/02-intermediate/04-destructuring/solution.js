// solution.js - Destructuring answers

// TODO 1
const car = { brand: "Tesla", model: "Model 3", year: 2022 };
const { brand, model } = car;

// TODO 2
const profile = { firstName: "Bob" };
const { firstName: name, status = "User" } = profile;

// TODO 3 & 4
const points = [10, 20, 30, 40];
const [p1, , p3, ...remaining] = points;

// TODO 5
const user = {
    name: "Alice",
    address: {
        city: "New York",
        zip: 10001
    }
};
const { address: { city } } = user;

// TODO 6
let a = 5, b = 10;
[a, b] = [b, a]; // Swapped!

// CHALLENGE ANSWER
function displaySummary({ title, stats: { views, likes } }) {
    console.log(`${title}: ${views} views, ${likes} likes`);
}
displaySummary({ title: "JS Tips", stats: { views: 500, likes: 42 } });

// --- Verification ---
console.log("--- Verification ---");
console.log(`Car: ${brand} ${model}`);
console.log(`Profile: ${name} (${status})`);
console.log(`Points 1 & 3: ${p1}, ${p3}`);
console.log(`Remaining points: ${remaining}`);
console.log(`City: ${city}`);
console.log(`Swapped: a=${a}, b=${b}`);

console.log("\n--- Why it works ---");
console.log("1. Shallow Extraction: It only extracts the references. If you destructure an object, modifying it will still affect the original if it's a reference type.");
console.log("2. Aliasing: Extremely useful when external APIs return property names that clash with your current variables.");
console.log("3. Rest/Spread integration: Destructuring is naturally designed to work with the 'rest' operator to gather leftovers.");
console.log("4. Readability: It tells other developers exactly which data pieces a function dependencies on right in the parameter list.");
