// example.ts - Pattern Matching with 'infer'

// 1. Unwrapping an Array
type UnpackArray<T> = T extends (infer U)[] ? U : T;

type T1 = UnpackArray<string[]>; // string
type T2 = UnpackArray<number>;   // number (not an array, returns original)

// 2. Getting Function Return Type
type MyReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

function greet() { return "Hello!"; }
type GreetRet = MyReturnType<typeof greet>; // string

// 3. Unwrapping a Promise (Awaited)
type UnpackPromise<T> = T extends Promise<infer U> ? U : T;

type P1 = UnpackPromise<Promise<number>>; // number

// 4. Getting Constructor Parameters
type MyConstructorParams<T> = T extends new (...args: infer P) => any ? P : never;

class Person {
    constructor(name: string, age: number) {}
}
type PersonParams = MyConstructorParams<typeof Person>; // [string, number]

// 5. Template Literal Inference
type GetColor<T> = T extends `color-${infer C}` ? C : never;

type C1 = GetColor<"color-red">; // "red"
type C2 = GetColor<"font-large">; // never
