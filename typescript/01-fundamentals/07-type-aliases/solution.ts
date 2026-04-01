// solution.ts - Type Aliases answers

// TODO 1
type ID = string | number;

// TODO 2 & 3
type Coordinates = {
    lat: number;
    lng: number;
};

function move(pos: Coordinates): void {
    console.log(`Moving to ${pos.lat}, ${pos.lng}`);
}

// TODO 4
type Callback = (error: string | null) => void;

// TODO 5
type UserResponse = 
    | { success: true; data: string }
    | { success: false; error: string };

// TODO 6
// Answer: Use an interface when you are defining the shape of an 
// object that you might want to extend later (inheritance) 
// or if you need declaration merging.

// CHALLENGE ANSWER
type Circle = { kind: "circle"; radius: number };
type Square = { kind: "square"; side: number };
type Shape = Circle | Square;

const myShape: Shape = { kind: "circle", radius: 5 };

console.log("\n--- Why it works ---");
console.log("1. Modularity: You can break down complex types into smaller, named parts that are easier to understand.");
console.log("2. Reusability: By naming a type, you only have to define it once and can reuse it across multiple functions and components.");
console.log("3. Readability: nicknames like 'UserID' or 'AppState' are much clearer than seeing 'string | number' or a 10-line object block everywhere.");
console.log("4. Flexibility: Type aliases can describe unions, intersections, and primitives, making them more powerful than interfaces for certain tasks.");
