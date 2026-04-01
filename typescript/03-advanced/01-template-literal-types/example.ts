// example.ts - String Patterns and Union Expansion

// 1. Basic Template Literal Type
type World = "world";
type Greeting = `hello ${World}`;

const g: Greeting = "hello world";
// const g2: Greeting = "hello there"; // Error

// 2. Union Expansion (Cartesian Product)
type Color = "red" | "blue";
type Intensity = "light" | "dark";

type Swatch = `${Intensity}-${Color}`;
// Result: "light-red" | "light-blue" | "dark-red" | "dark-blue"

const s: Swatch = "light-blue";

// 3. String Manipulation Utilities
type UppercaseGreeting = Uppercase<Greeting>; // "HELLO WORLD"
type CapitalizedColor = Capitalize<Color>; // "Red" | "Blue"

// 4. Practical Example: CSS Positions
type Vertical = "top" | "bottom";
type Horizontal = "left" | "right";
type Position = `${Vertical}-${Horizontal}` | "center";

const pos: Position = "top-left";

// 5. Combining with Mapped Types
interface User {
    id: number;
    name: string;
}

type GetterKeys<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type UserGetters = GetterKeys<User>;
// Result: { getId: () => number, getName: () => string }

export {};
