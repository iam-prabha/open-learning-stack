// solution.ts - Classes answers

// TODO 1 & 2 & 4 & 5
class Car {
    private speed: number = 0;
    protected owner: string = "Unknown";
    
    constructor(public make: string, public readonly serialNumber: string) {}

    accelerate(): void {
        this.speed += 10;
        console.log(`${this.make} speed is ${this.speed}`);
    }
}

// TODO 3
class ElectricCar extends Car {
    constructor(make: string, serial: string, public batteryLevel: number) {
        super(make, serial);
    }

    setOwner(name: string) {
        this.owner = name; // Allowed because it's protected
    }
}

const myTesla = new ElectricCar("Tesla", "XYZ-123", 95);
myTesla.accelerate();
// console.log(myTesla.speed); // Error: private

// TODO 6
// Answer: It significantly reduces boilerplate. You don't have to 
// declare the property AND assign it (this.x = x) manually. 
// TypeScript does it all in one line.

// CHALLENGE ANSWER
abstract class AppNotification {
    abstract send(): void;
}

class SmsNotification extends AppNotification {
    constructor(public phone: string, public message: string) { super(); }
    send(): void {
        console.log(`Sending SMS to ${this.phone}: ${this.message}`);
    }
}

console.log("\n--- Why it works ---");
console.log("1. Modifiers: TS provides access control at the compiler level, helping you build more robust APIs.");
2. "Parameter Properties: This unique TS feature makes your constructors much cleaner and easier to read.");
3. "Abstract Classes: Perfect for defining a 'base' that isn't supposed to be used on its own, only inherited from.");
4. "Readonly: Prevents bugs where critical data (like IDs or serial numbers) is changed after initialization.");
