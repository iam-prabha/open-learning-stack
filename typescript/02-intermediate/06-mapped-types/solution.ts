// solution.ts - Mapped Types answers

interface Point {
    x: number;
    y: number;
}

// TODO 1
type Stringify<T> = {
    [P in keyof T]: string;
};

// TODO 2
type PointStrings = Stringify<Point>;

// TODO 3
type Nullable<T> = {
    [P in keyof T]: T[P] | null;
};

// TODO 4
type Mandatory<T> = {
    [P in keyof T]-?: T[P];
};

// TODO 5
type EventHandlers<T> = {
    [P in keyof T as `on${Capitalize<string & P>}`]: T[P];
};

// TODO 6
// Answer: '-readonly' allows you to take an interface that is 
// entirely immutable (readonly) and create a "mutable" version of 
// it. This is useful for building data or for certain initialization 
// patterns where you want to change values temporarily.

// CHALLENGE ANSWER
type DataChanges<T> = {
    [P in keyof T as `data_${string & P}`]: { old: T[P], new: T[P] };
};

console.log("\n--- Why it works ---");
console.log("1. Consistency: Mapped types ensure that when the 'original' interface changes, the 'mapped' version updates automatically.");
console.log("2. Power: They allow for complex transformations (Nullable, Required, Readonly) that would be impossible to maintain manually.");
console.log("3. Productivity: With key remapping, you can generate getters, setters, or event handlers for an entire API in one line of code.");
console.log("4. Type-safety: Mapped types maintain the strict link between keys and values, giving you full IDE support for your transformed data.");
