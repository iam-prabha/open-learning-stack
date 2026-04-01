// example.ts - Adding Metadata and Behavior with Decorators

// 1. Class Decorator
function Logger(constructor: Function) {
    console.log(`[DECORATOR]: Class '${constructor.name}' was created.`);
}

@Logger
class User {
    constructor(public name: string) {}
}

// 2. Decorator Factory (Passing arguments)
function Log(prefix: string) {
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        const originalMethod = descriptor.value;
        descriptor.value = function (...args: any[]) {
            console.log(`[${prefix}]: Calling ${propertyKey}...`);
            return originalMethod.apply(this, args);
        };
    };
}

class Product {
    @Log("DEBUG")
    save() {
        console.log("Saving product to database...");
    }
}

const p = new Product();
p.save();

// 3. Property Decorator
function ReadOnly(target: any, propertyKey: string) {
    Object.defineProperty(target, propertyKey, {
        writable: false
    });
}

class Settings {
    @ReadOnly
    public api_url: string = "https://api.example.com";
}

const s = new Settings();
// s.api_url = "hack"; // This will either error or fail silently at runtime

// 4. Accessor Decorator (Get/Set)
function Enumerable(value: boolean) {
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        descriptor.enumerable = value;
    };
}

class Point {
    private _x: number = 0;
    
    @Enumerable(false)
    get x() { return this._x; }
}

export {};
