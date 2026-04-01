// solution.ts - Enums answers

// TODO 1
enum Day {
    Monday = 1,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday
}

// TODO 2
let today: Day = Day.Monday;

// TODO 3
enum LogLevel {
    INFO = "INFO",
    WARN = "WARN",
    ERROR = "ERROR"
}

// TODO 4
function logMessage(level: LogLevel, msg: string) {
    console.log(`[${level}] ${msg}`);
}

// TODO 5
logMessage(LogLevel.WARN, "Disk space low!");

// TODO 6
// Answer: No, string enums do not support reverse mapping like 
// numeric enums. You would get an error or undefined.

// CHALLENGE ANSWER
enum ErrorCode {
    NOT_FOUND = 404,
    UNAUTHORIZED = 401,
    SERVER_ERROR = 500
}

console.log("\n--- Why it works ---");
console.log("1. Documentation: Enums make your code more readable by using human names instead of magic numbers or strings.");
console.log("2. Type Safety: TypeScript will ensure you only use values defined in the enum, preventing typos like 'PENDNG' instead of 'Pending'.");
console.log("3. Refactoring: If you change an enum value in one place, it's updated everywhere the enum is used.");
console.log("4. Intent: Using an enum signal to other developers that this variable has a fixed, restricted set of possible values.");
