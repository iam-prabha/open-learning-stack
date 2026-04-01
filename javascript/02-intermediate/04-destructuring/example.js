// example.js - Mastering Destructuring in JavaScript

// 1. Basic Object Destructuring
const user = {
    id: 101,
    username: "coder123",
    email: "coder@example.com",
    role: "admin"
};

const { username, email } = user;
console.log(`User: ${username}, Email: ${email}`);

// 2. Aliasing and Default Values
const { role: userRole, status = "active" } = user;
console.log(`Role: ${userRole}, Status: ${status}`);

// 3. Array Destructuring
const coordinates = [40.7128, -74.0060];
const [lat, lng] = coordinates;
console.log(`Lat: ${lat}, Lng: ${lng}`);

// 4. Skipping items and Rest Operator
const colors = ["red", "green", "blue", "yellow"];
const [first, , third, ...others] = colors; // Skip index 1
console.log(`First: ${first}, Third: ${third}, Rest:`, others);

// 5. Nested Destructuring
const metadata = {
    title: "Document 1",
    info: {
        author: "Alice",
        date: "2024-01-01"
    }
};

const { info: { author } } = metadata;
console.log(`Author: ${author}`);

// 6. Function Parameter Destructuring (Very Common!)
function printHeader({ title, info: { author } }) {
    console.log(`--- ${title} (by ${author}) ---`);
}
printHeader(metadata);
