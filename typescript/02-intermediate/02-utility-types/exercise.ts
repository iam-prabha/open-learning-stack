// exercise.ts - Practice with Utility Types

interface Product {
    id: number;
    name: string;
    price: number;
    description: string;
    category: "electronics" | "home" | "food";
}

// TODO 1: Create a type 'ProductUpdate' that makes all 
// properties of 'Product' optional.

// TODO 2: Create a type 'ProductBasicInfo' that ONLY 
// includes 'id', 'name', and 'price'.

// TODO 3: Create a type 'ProductPublic' that includes 
// everything EXCEPT 'description'.

// TODO 4: Create a variable 'inventory' using 'Record' 
// that maps product IDs (numbers) to their 'Product' object.

// TODO 5: Create a readonly version of 'Product' called 'ReadonlyProduct'.

// TODO 6: Why is 'ReturnType<typeof myFunc>' useful in 
// large projects?
// Answer: ...

// CHALLENGE: Create a function 'updateProduct(id, changes)' 
// where 'changes' uses one of the utility types above.

// --- Verification ---
console.log("--- Results ---");
// Fill in the logic and verify!
