// types.ts
export interface User {
    id: number;
    username: string;
}

export type Role = "admin" | "user" | "guest";
