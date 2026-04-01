// solution.js - Classes answers

// TODO 1 & 2
class Book {
    constructor(title, author, pages) {
        this.title = title;
        this.author = author;
        this.pages = pages;
    }

    read() {
        console.log(`Reading ${this.title} by ${this.author}...`);
    }
}

// TODO 3
const myBook = new Book("JS Guide", "Mozilla", 500);
myBook.read();

// TODO 4 & 5
class EBook extends Book {
    constructor(title, author, pages, fileSize) {
        super(title, author, pages);
        this.fileSize = fileSize;
    }

    read() {
        console.log(`Downloading ${this.title} (${this.fileSize}MB) and reading...`);
    }

    // TODO 6
    static isEBook(obj) {
        return obj instanceof EBook;
    }
}

const myEBook = new EBook("Async JS", "Unknown", 100, 2);
myEBook.read();
console.log(`Is myEBook? ${EBook.isEBook(myEBook)}`);

// CHALLENGE ANSWER
class BankAccount {
    #balance = 0; // Truly private field

    constructor(initial) {
        this.#balance = initial;
    }

    deposit(amount) {
        this.#balance += amount;
    }

    get balance() {
        return this.#balance;
    }
}

// --- Verification ---
console.log("--- Verification ---");
const acc = new BankAccount(100);
acc.deposit(50);
console.log(`Acc Balance: ${acc.balance}`);

console.log("\n--- Why it works ---");
console.log("1. 'new' keyword: This is the trigger that actually builds the object from the class template.");
console.log("2. Inheritance: Classes don't need to reinvent the wheel. 'extends' lets you build specialized versions easily.");
console.log("3. super(): This connects the 'child' constructor to the 'parent' so properties are inherited correctly.");
console.log("4. Encapsulation: Static methods and private fields (#) help hide implementation details while exposing only what's needed.");
