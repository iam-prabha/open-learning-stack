// solution.ts - Functions answers

// TODO 1
function subtract(a: number, b: number): number {
    return a - b;
}

// TODO 2
function greetUser(name: string, age?: number): string {
    return age ? `${name} (${age})` : `Hello ${name}`;
}

// TODO 3
function calculate(amount: number, tax: number = 0.2): number {
    return amount * (1 + tax);
}

// TODO 4
function min(...args: number[]): number {
    return Math.min(...args);
}

// TODO 5
const isEven = (num: number): boolean => num % 2 === 0;

// TODO 6
// Answer: 'void' means the function explicitly DOES NOT return 
// a value. It's used for functions that just log stuff or 
// change a global variable.

// CHALLENGE ANSWER
function callCallback(num: number, cb: (s: string) => void): void {
    cb(`Count is ${num}`);
}

console.log("\n--- Why it works ---");
console.log("1. Parameter Safety: You can't accidentally pass a string into 'add', catching errors at the source.");
console.log("2. Return Contract: If you change your code to return 'null' by mistake, TypeScript will flag it.");
console.log("3. Default/Optional logic: TS helps you ensure that optional parameters are actually checked before use (preventing 'undefined' bugs).");
console.log("4. Rest Parameters: Makes handling flexible amounts of data just as safe as handling a single variable.");
