// solution.js - Prototypes answers

// TODO 1 & 2
const parent = { role: "user" };
const child = { __proto__: parent };

// TODO 3
console.log(`Initial child role: ${child.role}`);
child.role = "admin";
console.log(`After override: child=${child.role}, parent=${parent.role}`);

// TODO 4
const shape = { type: "basic" };
const square = Object.create(shape);
square.side = 4;

// TODO 5
function Person(name) {
    this.name = name;
}
Person.prototype.greet = function() {
    console.log(`Hi, I'm ${this.name}`);
};

// TODO 6
const p1 = new Person("Alice");
const p2 = new Person("Bob");
console.log(`Same greet function? ${p1.greet === p2.greet}`);

// CHALLENGE ANSWER
if (!Array.prototype.last) {
    Array.prototype.last = function() {
        return this[this.length - 1];
    };
}
console.log(`Challenge [1, 2, 3].last(): ${[1, 2, 3].last()}`);

// --- Verification ---
console.log("--- Verification ---");
p1.greet();
p2.greet();
console.log(`Square type: ${square.type}`);

console.log("\n--- Why it works ---");
console.log("1. Memory Efficiency: By putting methods on the prototype, thousands of objects share ONE function in memory, rather than each having their own copy.");
console.log("2. Shadowing: When you set a property directly on an object, it hides (shadows) the property with the same name on the prototype.");
console.log("3. Chain lookup: JS follows the __proto__ pointers until it finds the property or reaches null (Object.prototype is usually the end).");
console.log("4. Object.create: The modern, explicit way to set up inheritance without the overhead of constructor functions.");
