// example.ts - Giving types a name with Type Aliases

// 1. Primtive Alias
type UserID = string | number;
let currentUserID: UserID = "abc-123";

// 2. Object Alias
type Point = {
    x: number;
    y: number;
};

function draw(p: Point) {
    console.log(`Drawing at ${p.x}, ${p.y}`);
}
draw({ x: 10, y: 20 });

// 3. Union Alias (Very common!)
type Status = "success" | "error" | "loading";
let status: Status = "loading";

// 4. Function Alias
type MathFunc = (n1: number, n2: number) => number;

const add: MathFunc = (a, b) => a + b;
const sub: MathFunc = (a, b) => a - b;

// 5. Combining types with Intersection in an Alias
type User = { name: string };
type Admin = User & { role: "admin" };

const admin: Admin = {
    name: "Alice",
    role: "admin"
};
