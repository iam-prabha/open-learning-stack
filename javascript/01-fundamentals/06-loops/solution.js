// solution.js - Loop answers

// TODO 1
console.log("Countdown:");
for (let i = 10; i >= 1; i--) {
    console.log(i);
}

// TODO 2
let sum = 0;
let num = 1;
while (sum <= 50) {
    sum += num;
    num++;
}
console.log(`Sum is ${sum}`);

// TODO 3
const techs = ["HTML", "CSS", "JS"];
for (const t of techs) {
    console.log(t.toUpperCase());
}

// TODO 4
const book = { title: "1984", author: "George Orwell" };
for (const key in book) {
    console.log(`${key}: ${book[key]}`);
}

// TODO 5
for (let k = 1; k <= 7; k++) {
    if (k === 5) continue;
    console.log(k);
}

// TODO 6
let factorial = 1;
for (let f = 5; f >= 1; f--) {
    factorial *= f;
}

// CHALLENGE ANSWER
const phrase = "javascript is amazing";
let count = 0;
for (const char of phrase) {
    if (char === "a") count++;
}
console.log(`Count of 'a': ${count}`);

// --- Verification ---
console.log("--- Verification ---");
console.log(`Fact(5): ${factorial}`);
console.log(`Sum result: ${sum}`);

console.log("\n--- Why it works ---");
console.log("1. 'for' loop: Best when you know the number of iterations in advance.");
console.log("2. 'for...of': The modern way to iterate over iterable collections (Arrays, Sets, Strings).");
console.log("3. 'for...in': Used ONLY for objects. Avoid for arrays as it returns keys as strings.");
console.log("4. Control keywords: 'continue' ends the current iteration; 'break' ends the entire loop.");
