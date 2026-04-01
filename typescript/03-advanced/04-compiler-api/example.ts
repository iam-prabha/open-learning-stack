// example.ts - Programmatic Code Analysis
// Note: Requires 'npm install typescript'

import * as ts from "typescript";

// 1. Basic AST Traversal
const code = `
function hello(name: string) {
    console.log("Hello, " + name);
}
const x = 42;
`;

// Create a 'SourceFile' (The root of the AST)
const sourceFile = ts.createSourceFile(
    "temp.ts",
    code,
    ts.ScriptTarget.Latest,
    true
);

console.log("--- AST Traversal ---");

// Helper to visit every node recursively
function visit(node: ts.Node) {
    // If it's a function declaration, print its name
    if (ts.isFunctionDeclaration(node)) {
        console.log(`Found function: ${node.name?.getText(sourceFile)}`);
    }

    // If it's a variable declaration, print its identifier
    if (ts.isVariableDeclaration(node)) {
        console.log(`Found variable: ${node.name.getText(sourceFile)}`);
    }

    ts.forEachChild(node, visit);
}

visit(sourceFile);

// 2. Simple Transformation Demo
// (In a real app, you'd use ts.transform)
console.log("\n--- Structural Knowledge ---");
console.log(`File contains ${sourceFile.getChildCount()} top-level nodes.`);

// 3. Finding Types programmatically
// (Requires a 'Program' and 'TypeChecker', which usually needs a real file system)
// const program = ts.createProgram(["file.ts"], {});
// const checker = program.getTypeChecker();

export {};
