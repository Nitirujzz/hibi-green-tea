import { Auth } from "googleapis";
export declare function createAuthClient(): Auth.OAuth2Client | Auth.GoogleAuth;
export declare function createOAuth2Client(): Auth.OAuth2Client;
export declare function validateAuth(): Promise<void>;
export declare function runAuthFlow(): Promise<void>;
