// example.ts
// 1. Importing Types (Type-only import)
import type { User, Role } from "./types";

// 2. Importing Names and Defaults
import appConfig, { log, APP_VERSION } from "./utils";

const myUser: User = { id: 1, username: "Alice" };
const userRole: Role = "admin";

console.log("--- Type-safe Modules ---");
log(`Running Version ${APP_VERSION}`);
console.log(`Current User: ${myUser.username} (${userRole})`);
console.log(`API Path from default: ${appConfig.api}`);

// 3. Namespace Import (everything as one object)
import * as Utils from "./utils";
console.log("\n--- Namespace Access ---");
console.log(`Version from Utils: ${Utils.APP_VERSION}`);
