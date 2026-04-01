// example.ts - Using untyped JS with declaration files

// This import works because of my-lib.d.ts!
import { version, greet, calculate } from "my-lib";

console.log("--- Declaration Files ---");
console.log(`Library Version: ${version}`);
console.log(greet("Alice"));
console.log(`5 + 10 = ${calculate(5, 10)}`);

// Custom global declaration example
declare global {
    interface Window {
        myCustomFlag: boolean;
    }
}

// Now TS knows window has this flag!
// if (window.myCustomFlag) { ... }
