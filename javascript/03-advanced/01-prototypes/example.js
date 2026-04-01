// example.js - Understanding the Prototype Chain

// 1. Basic Inheritance via __proto__
const animal = {
    eats: true,
    walk() {
        console.log("Animal walks...");
    }
};

const rabbit = {
    jumps: true,
    __proto__: animal // rabbit inherits from animal
};

console.log("--- Basic Prototype ---");
console.log(`Rabbit eats? ${rabbit.eats}`); // true (inherited)
rabbit.walk(); // inherited method

// 2. Overriding Properties
rabbit.eats = false; // Shadowing the prototype property
console.log(`Rabbit eats (after override)? ${rabbit.eats}`); // false
console.log(`Animal still eats? ${animal.eats}`); // true (untouched)

// 3. Object.create (The cleaner way)
const worker = {
    work() { console.log(`${this.name} is working.`); }
};

const programmer = Object.create(worker);
programmer.name = "Alice";
console.log("\n--- Object.create ---");
programmer.work();

// 4. Function.prototype (Constructor inheritance)
function Car(make) {
    this.make = make;
}

// Adding a method to all instances via the prototype
Car.prototype.drive = function() {
    console.log(`${this.make} is driving!`);
};

const myCar = new Car("Toyota");
console.log("\n--- Constructor Prototype ---");
myCar.drive();

// 5. Checking the Chain
console.log("\n--- Chain Verification ---");
console.log(`Rabbit has own jumps? ${rabbit.hasOwnProperty("jumps")}`); // true
console.log(`Rabbit has own eats? ${rabbit.hasOwnProperty("eats")}`);   // true (because we overrode it)
console.log(`rabbit's proto:`, Object.getPrototypeOf(rabbit) === animal);
