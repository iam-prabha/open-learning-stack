// solution.ts - Type Guards and Narrowing answers

// TODO 1
function getLength(input: string | number) {
    if (typeof input === "string") {
        return input.length;
    }
    return input.toString().length;
}

// TODO 2
function handleError(error: unknown) {
    if (error instanceof Error) {
        console.error(error.message);
    }
}

// TODO 3
interface Bird { fly: () => void; }
interface Fish { swim: () => void; }

function move(pet: Bird | Fish) {
    if ("swim" in pet) {
        pet.swim();
    } else {
        pet.fly();
    }
}

// TODO 4
function isString(val: any): val is string {
    return typeof val === "string";
}

// TODO 5
function processUnknown(val: unknown) {
    if (isString(val)) {
        console.log(val.toLowerCase());
    }
}

// TODO 6
// Answer: Interfaces are a TypeScript-only feature. During compilation, 
// they are completely removed. 'instanceof' is a JavaScript runtime 
// check that looks for a constructor function (like a class). 
// Since interfaces don't exist at runtime, 'instanceof' can't find them.

// CHALLENGE ANSWER
interface Success { type: 'success'; data: string }
interface Failure { type: 'failure'; message: string }
type ApiResponse = Success | Failure;

function handleResponse(res: ApiResponse) {
    if (res.type === 'success') {
        console.log(`Data: ${res.data}`);
    } else {
        console.log(`Error: ${res.message}`);
    }
}

console.log("\n--- Why it works ---");
console.log("1. Type Safety: Narrowing ensures that you only access properties that definitely exist, preventing 'undefined is not a function' errors.");
console.log("2. Runtime-to-Compile link: Guards like 'typeof' and 'instanceof' allow TS to follow the runtime logic of your app.");
console.log("3. Modular guards: Type predicates let you extract complex narrowing logic into clean, reusable functions.");
console.log("4. Exhaustiveness checking: Narrowing helps TS ensure that you've handled every possible case in a union.");
