// example.ts - Refining Types with Guards

// 1. typeof Narrowing
function format(val: string | number) {
    if (typeof val === "string") {
        return val.trim(); // Narrowed to string
    }
    return val.toFixed(2); // Narrowed to number
}

// 2. instanceof Narrowing
class Laptop {
    powerOn() { console.log("Laptop is on"); }
}
class Mobile {
    makeCall() { console.log("Calling..."); }
}

function useDevice(d: Laptop | Mobile) {
    if (d instanceof Laptop) {
        d.powerOn();
    } else {
        d.makeCall();
    }
}

// 3. The 'in' operator
interface Bird { fly: () => void; }
interface Fish { swim: () => void; }

function move(animal: Bird | Fish) {
    if ("fly" in animal) {
        animal.fly();
    } else {
        animal.swim();
    }
}

// 4. User-Defined Type Guard (Type Predicate)
interface Admin { roles: string[]; }
interface User { name: string; }

// The 'arg is Admin' is the magic part!
function isAdmin(person: Admin | User): person is Admin {
    return (person as Admin).roles !== undefined;
}

function checkAccess(p: Admin | User) {
    if (isAdmin(p)) {
        console.log(`Admin roles: ${p.roles.join(", ")}`);
    } else {
        console.log(`Standard User: ${p.name}`);
    }
}

// 5. Truthiness Narrowing
function log(msg: string | null) {
    if (msg) {
        console.log(msg.toUpperCase()); // Narrowed to string (and not empty)
    }
}
