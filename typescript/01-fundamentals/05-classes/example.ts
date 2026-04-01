// example.ts - Typed Object-Oriented Programming

// 1. Basic Class with Type Annotations
class Animal {
    // Explicit property declaration
    name: string;
    
    constructor(name: string) {
        this.name = name;
    }

    makeSound(): void {
        console.log(`${this.name} makes a noise.`);
    }
}

// 2. Visibility Modifiers (The Shorthand Way!)
class Person {
    // This constructor automatically creates 'name' and 'age' properties
    constructor(
        public name: string, 
        private age: number,
        protected role: string = "User"
    ) {}

    public getInfo(): string {
        return `${this.name} is ${this.age} years old and is a ${this.role}.`;
    }
}

const alice = new Person("Alice", 28);
console.log("--- Visibility Modifiers ---");
console.log(alice.getInfo());
// console.log(alice.age); // Error: 'age' is private

// 3. Inheritance in TypeScript
class Employee extends Person {
    constructor(name: string, age: number, public salary: number) {
        super(name, age, "Employee"); // Can pass "Employee" to the protected 'role'
    }

    promote(): void {
        this.role = "Manager"; // Accessing protected property from parent
        console.log(`${this.name} was promoted to ${this.role}!`);
    }
}

const bob = new Employee("Bob", 35, 90000);
console.log("\n--- Inheritance ---");
bob.promote();

// 4. Abstract Classes
abstract class Shape {
    abstract getArea(): number;
}

class Circle extends Shape {
    constructor(public radius: number) { super(); }
    getArea(): number {
        return Math.PI * this.radius ** 2;
    }
}
