// example.ts - Structuring Multi-Project Builds

/* 
// 1. SHARED CORE (core/tsconfig.json)
{
    "compilerOptions": {
        "composite": true,      // REQUIRED for project refs
        "declaration": true,    // Composite projects must emit declarations
        "outDir": "../dist/core"
    }
}

// 2. MAIN APP (app/tsconfig.json)
{
    "compilerOptions": {
        "outDir": "../dist/app"
    },
    "references": [
        { "path": "../core" }   // REFS the core project
    ]
}

// 3. BUILDING EVERYTHING
// Command: tsc --build app/tsconfig.json
// This command will:
// - Check if 'core' needs to be rebuilt
// - Build 'core' first (if needed)
// - Build 'app' second
*/

console.log("--- Project References Architecture ---");
console.log("1. 'composite' is the key flag for dependencies.");
console.log("2. 'tsc -b' handles the build graph and incremental updates.");
console.log("3. Great for Monorepos and large enterprise apps.");

export {};
