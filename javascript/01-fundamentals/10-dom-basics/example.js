// example.js - Interacting with the webpage

// 1. Selecting Elements
const title = document.querySelector("#main-title");
const button = document.querySelector("#btn-click");
const input = document.querySelector("#user-input");
const output = document.querySelector("#output");

console.log("--- Selection ---");
console.log(`Title text: ${title.textContent}`);

// 2. Changing Content and Style
title.textContent = "DOM Content Updated!";
title.style.color = "blue";

// 3. Handling Events
button.addEventListener("click", () => {
    output.textContent = "Button was clicked! 🚀";
    button.classList.add("highlight");
});

// 4. Input Events
input.addEventListener("input", (event) => {
    const text = event.target.value;
    output.textContent = `You typed: ${text}`;
});

// 5. Creating New Elements
const newPara = document.createElement("p");
newPara.textContent = "I was created dynamically via JS!";
document.body.appendChild(newPara);
