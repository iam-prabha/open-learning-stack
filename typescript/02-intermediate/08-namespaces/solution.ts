// solution.ts - Namespaces answers

// TODO 1 & 2
namespace MathUtils {
    export const PHI = 1.618;
    export function add(a: number, b: number) { return a + b; }

    // TODO 4 & 5
    export namespace Geometry {
        export class Circle {
            constructor(public radius: number) {}
            area() { return Math.PI * this.radius ** 2; }
        }
    }
}

// TODO 3
console.log(MathUtils.add(10, 20));

// TODO 6
// Answer: ES Modules are a JavaScript standard, while namespaces 
// are TypeScript-specific. ESM is better for performance because 
// it allows for "tree-shaking" (removing unused code). It's also 
// clearer because it uses the file system for structure instead 
// of an arbitrary global object.

// CHALLENGE ANSWER
import G = MathUtils.Geometry;
const myCircle = new G.Circle(5);
console.log(myCircle.area());

console.log("\n--- Why it works ---");
console.log("1. Organization: Namespaces allow grouped logic (like a Math library) to live together ohne cluttering the global space.");
console.log("2. Nesting: You can create deep hierarchies to organize complex internal APIs.");
console.log("3. Aliasing: The 'import alias' syntax makes it easy to work with deep namespaces without repetitive typing.");
console.log("4. Types AND Values: Namespaces can export both interfaces (types) and classes/functions (values), all in one package.");
