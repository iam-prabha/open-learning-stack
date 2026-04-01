// solution.ts - Compiler API answers

import * as ts from "typescript";

// TODO 1
// Answer: Abstract Syntax Tree. It's a hierarchical representation 
// of the structure of source code. It allows you to programmatically 
// find and modify specific parts of a codebase without using 
// fragile regex.

// TODO 2 & 3
const code = `import { foo } from "bar"; const myVar = 100;`;
const sf = ts.createSourceFile("t.ts", code, ts.ScriptTarget.Latest, true);

sf.forEachChild(node => {
    if (ts.isImportDeclaration(node)) {
        console.log(`Found import: ${node.moduleSpecifier.getText(sf)}`);
    }
});

// TODO 4
// Answer: You use 'ts.isClassDeclaration(node)', 'ts.isFunctionDeclaration(node)', 
// etc. These are type guards provided by the TypeScript API.

// TODO 5
// Answer: A 'SourceFile' is the root node of the AST for a single 
// file. It contains the original text and its parsed structure.

// TODO 6
// Answer: 'ts.createSourceFile' only parses the code into a tree. 
// 'ts.createProgram' goes much further—it resolves imports, reads 
// multiple files, and performs full type-checking.

// CHALLENGE ANSWER
function countFunctions(inputCode: string): number {
    const source = ts.createSourceFile("t.ts", inputCode, ts.ScriptTarget.Latest, true);
    let count = 0;
    
    function walk(node: ts.Node) {
        if (ts.isFunctionDeclaration(node)) count++;
        ts.forEachChild(node, walk);
    }
    
    walk(source);
    return count;
}

console.log("\n--- Why it works ---");
console.log("1. AST Power: You can move away from simple string matching to structural analysis, making your tools 100% reliable.");
console.log("2. Ecosystem: This API is what powers VS Code, ESLint, and Prettier. Learning it gives you 'superpowers' for dev productivity.");
console.log("3. Extensibility: You can build custom lint rules that are specific to your team's project architecture.");
console.log("4. Code Gen: Instead of manual writing, you can automate boring tasks (like generating Zod schemas from TypeScript interfaces).");

export {};
