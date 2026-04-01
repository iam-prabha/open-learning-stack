// example.ts - Organizing Code with Namespaces

// 1. Basic Namespace
namespace Validation {
    export const PI = 3.14;

    export interface StringValidator {
        isAcceptable(s: string): boolean;
    }

    export class LettersOnlyValidator implements StringValidator {
        isAcceptable(s: string) {
            return /^[A-Za-z]+$/.test(s);
        }
    }
}

console.log("--- Basic Namespace ---");
const validator = new Validation.LettersOnlyValidator();
console.log(`'abc' is valid: ${validator.isAcceptable("abc")}`);
console.log(`'123' is valid: ${validator.isAcceptable("123")}`);

// 2. Nested Namespaces
namespace App {
    export namespace Utils {
        export function log(msg: string) {
            console.log(`[APP-LOG]: ${msg}`);
        }
    }

    export namespace Auth {
        export function login() {
            Utils.log("User logged in");
        }
    }
}

console.log("\n--- Nested Namespace ---");
App.Auth.login();

// 3. Namespace Aliases
import Auth = App.Auth;
Auth.login(); // Much shorter!
