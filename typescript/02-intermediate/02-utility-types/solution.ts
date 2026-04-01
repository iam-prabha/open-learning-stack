// solution.ts - Utility Types answers

interface Product {
    id: number;
    name: string;
    price: number;
    description: string;
    category: "electronics" | "home" | "food";
}

// TODO 1
type ProductUpdate = Partial<Product>;

// TODO 2
type ProductBasicInfo = Pick<Product, "id" | "name" | "price">;

// TODO 3
type ProductPublic = Omit<Product, "description">;

// TODO 4
type Inventory = Record<number, Product>;
const inv: Inventory = {
    1: { id: 1, name: "IPhone", price: 999, description: "Fancy phone", category: "electronics" }
};

// TODO 5
type ReadonlyProduct = Readonly<Product>;

// TODO 6
// Answer: In large projects, you don't have to manually keep 
// your types in sync with your functions. If the function 
// starts returning a new field, 'ReturnType' picks it up 
// automatically throughout your whole code.

// CHALLENGE ANSWER
function updateProduct(id: number, changes: Partial<Product>) {
    console.log(`Updating ${id} with:`, changes);
}

updateProduct(101, { price: 899 });

console.log("\n--- Why it works ---");
console.log("1. Modularity: Utility types allow you to build many variations of a single 'source of truth' interface.");
console.log("2. Dry Principle: Instead of copying and pasting similar interfaces, you transform them with utilities.");
console.log("3. Precision: Utilities like 'Pick' and 'Omit' make it clear exactly what data a component or function needs.");
console.log("4. Safety: 'Readonly' ensures that data meant to be immutable is actually treated that way by the compiler.");
