// example.js - Object-Oriented JavaScript with Classes

// 1. Defining a Base Class
class Animal {
    constructor(name, type) {
        this.name = name;
        this.type = type;
    }

    // Method (belongs to instances)
    makeSound() {
        console.log(`${this.name} makes a sound!`);
    }

    // Static Method (belongs to the class itself)
    static describe() {
        console.log("Animals are multicellular organisms.");
    }
}

console.log("--- Base Class ---");
const generic = new Animal("Buddy", "Mamal");
generic.makeSound();
Animal.describe(); // Called on Class, not instance

// 2. Inheritance
class Dog extends Animal {
    constructor(name, breed) {
        // Must call super() to inherit from Animal
        super(name, "Dog");
        this.breed = breed;
    }

    // Overriding a method
    makeSound() {
        console.log(`${this.name} barks! Woof!`);
    }

    fetch() {
        console.log(`${this.name} is fetching the ball...`);
    }
}

console.log("\n--- Inheritance ---");
const rover = new Dog("Rover", "Labrador");
rover.makeSound();
rover.fetch();

// 3. Getters and Setters
class User {
    constructor(name) {
        this._name = name; // Private convention (pre-ES2022)
    }

    get name() {
        return this._name.toUpperCase();
    }

    set name(value) {
        if (value.length < 2) {
            console.log("Name too short!");
            return;
        }
        this._name = value;
    }
}

console.log("\n--- Getters/Setters ---");
const user = new User("alice");
console.log(user.name); // Calls the 'get'
user.name = "b";         // Logs error
user.name = "bob";       // Calls the 'set'
console.log(user.name);
