// solution.ts - Unions and Intersections answers

// TODO 1
let result: boolean | 0 = true;
result = 0;

// TODO 2
function printLength(input: string | string[]): number {
    if (Array.isArray(input)) {
        return input.length;
    }
    return input.length; // string also has a length!
}

// TODO 3
type Status = "Online" | "Offline" | "Away";

// TODO 4
interface Logger {
    log: (msg: string) => void;
}
interface Writer {
    write: (content: string) => void;
}

// TODO 5
type LogWriter = Logger & Writer;
const myTool: LogWriter = {
    log: (m) => console.log(m),
    write: (c) => console.log(`Writing: ${c}`)
};

// TODO 6
// Answer: Because TypeScript must guarantee that the property 
// exists on BOTH sides of the union. If you access a property 
// that only exists on one, it might be undefined at runtime, 
// which is exactly what TS is designed to prevent.

// CHALLENGE ANSWER
interface UserInfo { type: "user"; info: string }
interface AdminInfo { type: "admin"; level: number }
type Info = UserInfo | AdminInfo;

function processData(data: Info) {
    if (data.type === "user") {
        console.log(`User Info: ${data.info}`);
    } else {
        console.log(`Admin Level: ${data.level}`);
    }
}

console.log("\n--- Why it works ---");
console.log("1. Union Power: It allows functions to be flexible (like receiving an ID) while still maintaining strict types.");
console.log("2. Composition: Intersection allows building complex types out of small, reusable parts (the modularity principle).");
console.log("3. Discriminant Unions: The 'type' property pattern is a standard way to choose between members of a union (narrowing).");
console.log("4. Type-checking: TS ensures you handle each case in a union, reducing bugs in conditional logic.");
