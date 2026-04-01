// math.js - Code to be tested
function sum(a, b) {
    return a + b;
}

function divide(a, b) {
    if (b === 0) throw new Error("Zero division");
    return a / b;
}

module.exports = { sum, divide };
