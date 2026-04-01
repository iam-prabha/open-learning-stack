// exercise.ts - Practice with Mapped Types

interface Point {
    x: number;
    y: number;
}

// TODO 1: Create a mapped type 'Stringify<T>' that 
// transforms every property of T into a 'string'.

// TODO 2: Create a type 'PointStrings' by using 
// 'Stringify' on the 'Point' interface.

// TODO 3: Create a mapped type 'Nullable<T>' that 
// makes every property 'T[P] | null'.

// TODO 4: Create a mapped type 'Mandatory<T>' that 
// REMOVES the optional ('?') modifier from all properties.

// TODO 5: Use key remapping to create a type 'EventHandlers<T>' 
// that transforms { click: any } into { onClick: any }.

// TODO 6: What is the benefit of the '-readonly' modifier?
// Answer: ...

// CHALLENGE: Create a mapped type that prefixes every key 
// with 'data_' and changes the value to { old: T[P], new: T[P] }.

// --- Verification ---
console.log("--- Results ---");
// Check your mapping logic vs the solution!
