// my-lib.d.ts - Blueprints for my-lib.js

declare module "my-lib" {
    export const version: string;
    export function greet(name: string): string;
    export function calculate(a: number, b: number): number;
}
