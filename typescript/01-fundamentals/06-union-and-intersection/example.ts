// example.ts - Combining Types with | and &

// 1. Union Types (OR)
// A variable that can be a string OR a number
function formatId(id: string | number) {
    if (typeof id === "string") {
        return id.toUpperCase();
    }
    return id.toFixed(2);
}

console.log("--- Union Types ---");
console.log(`ID string: ${formatId("abc")}`);
console.log(`ID number: ${formatId(123)}`);

// 2. Literal Union Types
type Direction = "North" | "South" | "East" | "West";
let currentDir: Direction = "North";
// currentDir = "Up"; // Error

// 3. Intersection Types (AND)
interface HasName {
    name: string;
}

interface HasAge {
    age: number;
}

// Combine both interfaces
type Person = HasName & HasAge;

const alice: Person = {
    name: "Alice",
    age: 25
};

console.log("\n--- Intersection Types ---");
console.log(`${alice.name} is ${alice.age} years old.`);

// 4. Practical Application: Redux-like State
interface SuccessState {
    status: "success";
    data: string[];
}

interface ErrorState {
    status: "error";
    error: string;
}

type AppState = SuccessState | ErrorState;

function render(state: AppState) {
    if (state.status === "success") {
        console.log(`Loaded ${state.data.length} items`);
    } else {
        console.log(`Error: ${state.error}`);
    }
}
