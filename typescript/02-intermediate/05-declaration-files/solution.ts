// solution.ts - Declaration Files answers

// TODO 1 & 2 & 3
/*
// logger.js
module.exports = { info: (m) => console.log(m) };

// logger.d.ts
declare module "logger" {
    export function info(msg: string): void;
}

// main.ts
import { info } from "logger";
info("Test log");
*/

// TODO 4
declare global {
    namespace NodeJS {
        interface ProcessEnv {
            appName: string;
        }
    }
}

// TODO 5
// Answer: 'npm install --save-dev @types/lodash'

// TODO 6
// Answer: JavaScript runtimes (Node/Browser) do not understand 
// TypeScript syntax. By using a separate '.d.ts' file, we keep 
// the production code clean and compatible while still 
// getting the development benefits of TypeScript's type system.

// CHALLENGE ANSWER
/*
declare module "api" {
    export class Client {
        fetch(url: string): Promise<any>;
    }
}
*/

console.log("\n--- Why it works ---");
console.log("1. Multi-language support: TS can work with assets from other languages and formats as long as there's a declaration file.");
console.log("2. Tooling: IDEs like VS Code use .d.ts files to provide autocomplete even in plain JavaScript files.");
console.log("3. Erasure: Declaration files have zero runtime impact. They are purely for the development phase.");
console.log("4. Community: DefinitelyTyped contains type definitions for thousands of libraries, saving developers from writing their own.");
