// example.ts - Fixed sets of constants with Enums

// 1. Numeric Enums (Default starts at 0)
enum Status {
    Pending, // 0
    InProgress, // 1
    Completed, // 2
}

console.log("--- Numeric Enum ---");
let currentStatus: Status = Status.Pending;
console.log(`Status value: ${currentStatus}`); // Output: 0

// 2. Initialized Numeric Enum
enum UserRole {
    Admin = 1,
    Editor = 5,
    Viewer = 10
}
console.log(`Admin Role ID: ${UserRole.Admin}`);

// 3. String Enums (Most recommended for readability)
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT"
}

console.log("\n--- String Enum ---");
function move(dir: Direction) {
    console.log(`Moving ${dir}...`);
}
move(Direction.Up); // "Moving UP..."

// 4. Reverse Mapping (Numeric only!)
const statusName = Status[0];
console.log("\n--- Reverse Mapping ---");
console.log(`Status 0 is named: ${statusName}`);

// 5. Heterogeneous Enums (Avoid this!)
enum Mix {
    No = 0,
    Yes = "YES"
}
