// solution.ts - Project References answers

// TODO 1
// Answer: Incremental builds. By splitting your project, 
// TypeScript can recompile ONLY the parts that have changed, 
// rather than checking the entire workspace.

// TODO 2
// Answer: 'composite'

// TODO 3
// Answer: 'tsc --build' or 'tsc -b'

// TODO 4
// Answer: Because other projects only see the '.d.ts' 
// declaration files, not the actual source code. 
// Without declarations, there are no types to reference.

// TODO 5
/*
{
    "references": [
        { "path": "../utils" },
        { "path": "../api" }
    ]
}
*/

// TODO 6
// Answer: No. Circular references are forbidden because 
// TypeScript needs a clear 'Dependency Graph' to build 
// things in the correct order.

// CHALLENGE ANSWER
// Answer: When 'incremental' is enabled, TypeScript creates 
// a '.tsbuildinfo' file that caches information about the 
// project's state. On the next build, it compares this cache 
// to the current files to skip work that doesn't need to be done.

console.log("\n--- Why it works ---");
console.log("1. Modularity: Project references force you to design your code as a set of interacting modules (like 'domain' and 'infra'), which is a best practice.");
console.log("2. Scale: This is the ONLY way to manage TypeScript in projects with millions of lines of code without build times exploding.");
console.log("3. Enforced Hierarchy: It prevents 'spaghetti' imports by clearly defining which projects can see which other projects.");
console.log("4. Shared Logic: It makes it trivial to share types between your backend (Node.js) and frontend (React/Vue) in a monorepo.");

export {};
