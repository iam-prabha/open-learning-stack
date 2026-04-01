// example.ts - Transforming Objects Dynamically

interface User {
    id: number;
    name: string;
}

// 1. Basic Mapped Type
// Turns every property into a boolean
type OptionsFlags<T> = {
    [Property in keyof T]: boolean;
};

type UserOptions = OptionsFlags<User>;
const opts: UserOptions = { id: true, name: false };

// 2. Mapping Modifiers
// Makes all properties optional and readonly
type CreateReadonly<T> = {
    readonly [P in keyof T]?: T[P];
};
type ReadonlyUser = CreateReadonly<User>;

// 3. Removing Modifiers (The '-' prefix)
interface PartialConfig {
    id?: number;
    host?: string;
}

// Removes the '?' from all properties
type Concrete<T> = {
    [P in keyof T]-?: T[P];
};
type Config = Concrete<PartialConfig>; // id and host are now required

// 4. Key Remapping (via 'as')
// Renames keys to 'get' + OriginalName
type Getters<T> = {
    [P in keyof T as `get${Capitalize<string & P>}`]: () => T[P];
};

type UserGetters = Getters<User>;
/* Result: 
{ 
    getId: () => number, 
    getName: () => string 
} */
const userApi: UserGetters = {
    getId: () => 1,
    getName: () => "Alice"
};

export {};
