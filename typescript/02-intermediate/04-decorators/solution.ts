// solution.ts - Decorators answers

// TODO 1 & 2
function Sealed(constructor: Function) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
}

@Sealed
class Database {}

// TODO 3 & 4
function Deprecated(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.warn(`[WARNING]: Method '${propertyKey}' is deprecated.`);
        return originalMethod.apply(this, args);
    };
}

class ApiService {
    @Deprecated
    getData() { return { data: [] }; }
}

// TODO 5
function Color(value: string) {
    return function (constructor: Function) {
        constructor.prototype.color = value;
    };
}

@Color("Red")
class Home {}

// TODO 6
// Answer: 'experimentalDecorators' must be set to true in the 
// 'compilerOptions' section of your tsconfig.json.

// CHALLENGE ANSWER
function Required(target: any, propertyKey: string) {
    const targetClass = target.constructor;
    if (!targetClass.requiredMetadata) {
        targetClass.requiredMetadata = [];
    }
    targetClass.requiredMetadata.push(propertyKey);
}

class UserForm {
    @Required
    name: string = "";
}

console.log("\n--- Why it works ---");
console.log("1. Meta-programming: Decorators allow you to separate cross-cutting concerns (like logging or validation) from your core business logic.");
console.log("2. DRY Principle: Instead of adding logs inside every single method, you apply one @Log decorator once.");
console.log("3. Declarative Code: Decorators make your code much more readable by clearly showing the 'intent' (e.g., @Deprecated) directly above the code.");
console.log("4. Extensibility: Frameworks like NestJS and Angular use decorators heavily to handle dependency injection and routing.");
