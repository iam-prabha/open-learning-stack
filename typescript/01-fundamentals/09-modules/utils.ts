// utils.ts
export const APP_VERSION = "2.0.0";

export function log(msg: string): void {
    console.log(`[TS-LOG]: ${msg}`);
}

// Default export
const config = { api: "/v1", timeout: 5000 };
export default config;
