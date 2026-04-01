// example.ts - Transforming Types with Built-in Utilities

interface User {
    id: number;
    name: string;
    email: string;
    isAdmin: boolean;
}

// 1. Partial<T> - All properties become optional
type UserUpdate = Partial<User>;
const update: UserUpdate = { email: "new@example.com" }; // OK

// 2. Required<T> - Opposite of Partial (makes everything required)
type FullUser = Required<UserUpdate>;

// 3. Readonly<T> - Properties cannot be reassigned
const admin: Readonly<User> = {
    id: 99,
    name: "Admin",
    email: "admin@system.com",
    isAdmin: true
};
// admin.name = "New Name"; // Error

// 4. Pick<T, Keys> - Select specific properties
type UserPreview = Pick<User, "id" | "name">;
const preview: UserPreview = { id: 1, name: "Alice" };

// 5. Omit<T, Keys> - Remove specific properties
type PublicUser = Omit<User, "isAdmin">;
const pub: PublicUser = { id: 2, name: "Bob", email: "bob@web.com" };

// 6. Record<Keys, Value> - Map keys to a type
type PageInfo = { title: string };
type Router = Record<"home" | "about" | "contact", PageInfo>;

const nav: Router = {
    home: { title: "Home Page" },
    about: { title: "About Us" },
    contact: { title: "Contact" }
};

// 7. ReturnType<T> - Get the type of a function's return value
function getUser() {
    return { id: 1, login: "alice" };
}
type UserData = ReturnType<typeof getUser>;
