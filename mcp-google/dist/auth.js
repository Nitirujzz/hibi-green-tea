import { google } from "googleapis";
import * as fs from "fs";
import * as path from "path";
import * as http from "http";
import { fileURLToPath } from "url";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const TOKEN_PATH = path.join(__dirname, "..", ".token.json");
const SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file",
];
// ─── ตรวจว่าใช้ Service Account หรือ OAuth2 ─────────────────────────────────
export function createAuthClient() {
    const serviceKeyPath = process.env.GOOGLE_SERVICE_ACCOUNT_KEY_PATH;
    const serviceKeyJson = process.env.GOOGLE_SERVICE_ACCOUNT_KEY_JSON;
    // วิธีที่ 1: Service Account Key File (แนะนำสำหรับ Remote/Server)
    if (serviceKeyPath && fs.existsSync(serviceKeyPath)) {
        return new google.auth.GoogleAuth({
            keyFile: serviceKeyPath,
            scopes: SCOPES,
        });
    }
    // วิธีที่ 2: Service Account Key JSON (inline ใน .env)
    if (serviceKeyJson) {
        const keyData = JSON.parse(serviceKeyJson);
        return new google.auth.GoogleAuth({
            credentials: keyData,
            scopes: SCOPES,
        });
    }
    // วิธีที่ 3: OAuth2 + Refresh Token (สำหรับ Local / Personal Account)
    return createOAuth2Client();
}
export function createOAuth2Client() {
    const clientId = process.env.GOOGLE_CLIENT_ID;
    const clientSecret = process.env.GOOGLE_CLIENT_SECRET;
    const redirectUri = process.env.GOOGLE_REDIRECT_URI || "http://localhost:3001/oauth2callback";
    if (!clientId || !clientSecret) {
        throw new Error([
            "❌ ไม่พบ Google Credentials",
            "",
            "ตั้งค่าด้วยวิธีใดวิธีหนึ่ง:",
            "",
            "วิธีที่ 1 — Service Account (แนะนำสำหรับ Remote):",
            "  GOOGLE_SERVICE_ACCOUNT_KEY_PATH=/path/to/key.json",
            "",
            "วิธีที่ 2 — OAuth2 (สำหรับ Local):",
            "  GOOGLE_CLIENT_ID=xxx",
            "  GOOGLE_CLIENT_SECRET=xxx",
            "  GOOGLE_REFRESH_TOKEN=xxx",
            "",
            "ดูรายละเอียดที่ mcp-google/SETUP.md",
        ].join("\n"));
    }
    const oauth2Client = new google.auth.OAuth2(clientId, clientSecret, redirectUri);
    const refreshToken = process.env.GOOGLE_REFRESH_TOKEN;
    if (refreshToken) {
        oauth2Client.setCredentials({ refresh_token: refreshToken });
    }
    else if (fs.existsSync(TOKEN_PATH)) {
        const token = JSON.parse(fs.readFileSync(TOKEN_PATH, "utf-8"));
        oauth2Client.setCredentials(token);
    }
    else {
        throw new Error("ไม่พบ GOOGLE_REFRESH_TOKEN — รัน: node dist/index.js --auth เพื่อรับ Token");
    }
    return oauth2Client;
}
// ─── ตรวจสอบว่า Auth พร้อมใช้งาน ─────────────────────────────────────────────
export async function validateAuth() {
    const auth = createAuthClient();
    if (auth instanceof google.auth.GoogleAuth) {
        const client = await auth.getClient();
        await client.getAccessToken();
    }
    else {
        await auth.getAccessToken();
    }
}
// ─── OAuth2 Flow สำหรับ Local Environment ──────────────────────────────────
export async function runAuthFlow() {
    const clientId = process.env.GOOGLE_CLIENT_ID;
    const clientSecret = process.env.GOOGLE_CLIENT_SECRET;
    if (!clientId || !clientSecret) {
        console.error("❌ ต้องมี GOOGLE_CLIENT_ID และ GOOGLE_CLIENT_SECRET ใน .env\n" +
            "   (OAuth2 Flow ใช้เฉพาะ Local environment)");
        process.exit(1);
    }
    const redirectUri = "http://localhost:3001/oauth2callback";
    const oauth2Client = new google.auth.OAuth2(clientId, clientSecret, redirectUri);
    const authUrl = oauth2Client.generateAuthUrl({
        access_type: "offline",
        scope: SCOPES,
        prompt: "consent",
    });
    console.log("\n🔐 HIBI MATCHA — Google OAuth2 Setup");
    console.log("━".repeat(60));
    console.log("\n⚠️  หมายเหตุ: ขั้นตอนนี้ใช้สำหรับ Local environment เท่านั้น");
    console.log("    สำหรับ Remote/Cloud แนะนำใช้ Service Account แทน\n");
    console.log("1. เปิด URL นี้ในเบราว์เซอร์:");
    console.log(`\n   ${authUrl}\n`);
    console.log("2. ล็อกอิน Google แล้วอนุญาต Permissions");
    console.log("3. รอ Callback อัตโนมัติบน http://localhost:3001\n");
    await new Promise((resolve, reject) => {
        const server = http.createServer(async (req, res) => {
            if (!req.url?.startsWith("/oauth2callback"))
                return;
            const url = new URL(req.url, "http://localhost:3001");
            const code = url.searchParams.get("code");
            if (!code) {
                res.writeHead(400);
                res.end("ไม่พบ Authorization Code");
                reject(new Error("No code in callback"));
                return;
            }
            try {
                const { tokens } = await oauth2Client.getToken(code);
                oauth2Client.setCredentials(tokens);
                fs.writeFileSync(TOKEN_PATH, JSON.stringify(tokens, null, 2));
                res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
                res.end(`
          <html><body style="font-family:sans-serif;padding:40px;background:#f7f3e9;color:#1a1a1a">
          <h2 style="color:#16a34a">✅ เชื่อมต่อ Google สำเร็จ!</h2>
          <p>คัดลอก Refresh Token ด้านล่างไปใส่ใน <code>.env</code></p>
          <pre style="background:#fff;padding:20px;border-radius:8px;word-break:break-all;font-size:13px">${tokens.refresh_token}</pre>
          <p style="color:#888">ปิดหน้าต่างนี้และกลับไปที่ Terminal</p>
          </body></html>
        `);
                console.log("\n✅ Authentication สำเร็จ!");
                console.log(`\n📝 Refresh Token:\n${tokens.refresh_token}`);
                console.log("\n⬇️  ใส่ค่าต่อไปนี้ใน mcp-google/.env:");
                console.log(`GOOGLE_REFRESH_TOKEN=${tokens.refresh_token}\n`);
                server.close();
                resolve();
            }
            catch (err) {
                res.writeHead(500);
                res.end("เกิดข้อผิดพลาด");
                reject(err);
            }
        });
        server.listen(3001, () => console.log("🚀 Callback server รอรับ Token บน port 3001..."));
        server.on("error", reject);
    });
}
