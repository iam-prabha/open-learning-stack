// example.ts - Contracts for Objects with Interfaces

// 1. Basic Interface
interface User {
    readonly id: number; // Cannot be changed after creation
    name: string;
    email: string;
    age?: number; // Optional property
}

const alice: User = {
    id: 101,
    name: "Alice",
    email: "alice@example.com"
};

// alice.id = 200; // Error: Cannot assign to 'id' because it is a read-only property

console.log("--- Basic Interface ---");
console.log(`User: ${alice.name}, Email: ${alice.email}`);

// 2. Extending Interfaces (Inheritance)
interface Employee extends User {
    role: string;
    salary: number;
}

const bob: Employee = {
    id: 102,
    name: "Bob",
    email: "bob@tech.co",
    role: "Developer",
    salary: 80000
};

console.log("\n--- Extended Interface ---");
console.log(`${bob.name} is a ${bob.role} with ID ${bob.id}`);

// 3. Index Signatures (For dynamic keys)
interface StringMap {
    [key: string]: string;
}

const translations: StringMap = {
    "hello": "ciao",
    "goodbye": "addio"
};

console.log("\n--- Index Signatures ---");
console.log(`Translate 'hello': ${translations["hello"]}`);
