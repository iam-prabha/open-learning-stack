// my-lib.js (PRETEND THIS IS A 3RD PARTY LIBRARY)
const version = "1.0.0";

function greet(name) {
    return "Hello, " + name;
}

function calculate(a, b) {
    return a + b;
}

module.exports = { version, greet, calculate };
