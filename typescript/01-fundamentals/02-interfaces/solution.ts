// solution.ts - Interfaces answers

// TODO 1
interface Product {
    readonly id: number;
    name: string;
    price: number;
    description?: string;
}

// TODO 2
const laptop: Product = {
    id: 1,
    name: "ThinkPad",
    price: 1200
};

// TODO 3
// laptop.id = 2; // Error: Cannot assign to 'id' (readonly)

// TODO 4 & 5
interface DigitalProduct extends Product {
    downloadUrl: string;
}

const musicFile: DigitalProduct = {
    id: 50,
    name: "Song.mp3",
    price: 0.99,
    downloadUrl: "https://example.com/dl"
};

// TODO 6
interface Settings {
    [key: string]: boolean;
}
const config: Settings = {
    darkMode: true,
    showSidebar: false
};

// CHALLENGE ANSWER
interface MathOperation {
    (a: number, b: number): number;
}
const add: MathOperation = (x, y) => x + y;

console.log("\n--- Why it works ---");
console.log("1. Consistency: Interfaces ensure that different parts of your app use the same data structure, preventing 'undefined' errors.");
console.log("2. Extensibility: By using 'extends', you can build complex types from simpler ones, keeping your code DRY (Don't Repeat Yourself).");
console.log("3. Erasure: Interfaces disappear during compilation. They add zero weight to your final JavaScript bundle.");
console.log("4. Readonly/Optional: These features give you fine-grained control over how data can be accessed and modified.");
