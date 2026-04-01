// solution.js - DOM answers

// TODO 1
const title = document.getElementById("main-title");
title.textContent = "DOM Mastered!";

// TODO 2
const desc = document.querySelector(".description");
desc.style.color = "green";

// TODO 3
const btn = document.querySelector("#btn-click");
btn.addEventListener("click", () => {
    console.log("Button clicked");
});

// TODO 4
const input = document.querySelector("#user-input");
const output = document.querySelector("#output");
input.addEventListener("input", (e) => {
    output.textContent = `Character count: ${e.target.value.length}`;
});

// TODO 5
btn.addEventListener("mouseenter", () => btn.classList.add("highlight"));
btn.addEventListener("mouseleave", () => btn.classList.remove("highlight"));

// TODO 6
const ul = document.createElement("ul");
const li = document.createElement("li");
li.textContent = "List Item";
ul.appendChild(li);
document.body.appendChild(ul);

// CHALLENGE ANSWER
const counterDiv = document.createElement("div");
let count = 0;
const display = document.createElement("span");
display.textContent = ` ${count} `;

const up = document.createElement("button");
up.textContent = "+";
up.onclick = () => { count++; display.textContent = ` ${count} `; };

const down = document.createElement("button");
down.textContent = "-";
down.onclick = () => { count--; display.textContent = ` ${count} `; };

counterDiv.append(down, display, up);
document.body.appendChild(counterDiv);

console.log("--- Why it works ---");
console.log("1. textContent vs innerHTML: textContent is safer because it treats all data as plain text, not HTML code.");
console.log("2. Event Listeners: Separating JS logic from HTML (addEventListener) makes testing and debugging much easier.");
console.log("3. DOM Tree: Every element is a node you can access, move, or delete without reloading the page.");
console.log("4. classList: The best way to manage styles — let CSS handle the looks, and JS handle the 'triggering'.");
