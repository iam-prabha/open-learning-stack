// example.ts - Advanced Computations in the Type System

// 1. Recursive Types: DeepPartial
// Makes every property at every level optional
type DeepPartial<T> = T extends object 
    ? { [P in keyof T]?: DeepPartial<T[P]> } 
    : T;

interface ComplexUser {
    id: number;
    profile: {
        bio: string;
        social: { twitter: string; github: string };
    };
}

const partialUser: DeepPartial<ComplexUser> = {
    profile: { social: { github: "@alice" } }
};

// 2. Tuple Manipulation: Filtering
// Removes 'null' elements from a tuple type
type FilterNull<T extends any[]> = T extends [infer First, ...infer Rest]
    ? First extends null 
        ? FilterNull<Rest> 
        : [First, ...FilterNull<Rest>]
    : [];

type Cleaned = FilterNull<[string, null, number, null]>; // [string, number]

// 3. String Splitting
type Split<S extends string, D extends string> = 
    S extends `${infer T}${D}${infer U}`
        ? [T, ...Split<U, D>]
        : [S];

type PathParts = Split<"user/profile/settings", "/">; 
// Result: ["user", "profile", "settings"]

// 4. Practical Example: Route Parsing
type ParseParams<Path extends string> = 
    Path extends `${string}:${infer Param}/${infer Rest}`
        ? Param | ParseParams<Rest>
        : Path extends `${string}:${infer Param}`
            ? Param
            : never;

type Params = ParseParams<"/users/:userId/posts/:postId">; 
// Result: "userId" | "postId"

export {};
