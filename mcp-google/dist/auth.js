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
export function createOAuth2Client() {
    const clientId = process.env.GOOGLE_CLIENT_ID;
    const clientSecret = process.env.GOOGLE_CLIENT_SECRET;
    const redirectUri = process.env.GOOGLE_REDIRECT_URI || "http://localhost:3001/oauth2callback";
    if (!clientId || !clientSecret) {
        throw new Error("Missing GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET in environment variables.\n" +
            "โปรดตั้งค่าใน mcp-google/.env — ดู .env.example สำหรับรายละเอียด");
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
    return oauth2Client;
}
// ใช้ Run ครั้งแรกเพื่อรับ Refresh Token ผ่าน OAuth2 Flow
export async function runAuthFlow() {
    const clientId = process.env.GOOGLE_CLIENT_ID;
    const clientSecret = process.env.GOOGLE_CLIENT_SECRET;
    const redirectUri = "http://localhost:3001/oauth2callback";
    const oauth2Client = new google.auth.OAuth2(clientId, clientSecret, redirectUri);
    const authUrl = oauth2Client.generateAuthUrl({
        access_type: "offline",
        scope: SCOPES,
        prompt: "consent",
    });
    console.log("\n🔐 HIBI MATCHA — Google OAuth2 Setup");
    console.log("━".repeat(50));
    console.log("1. เปิด URL นี้ในเบราว์เซอร์:");
    console.log(`\n   ${authUrl}\n`);
    console.log("2. ล็อกอิน Google แล้วอนุญาต Permissions");
    console.log("3. รอ Callback อัตโนมัติ...\n");
    await new Promise((resolve, reject) => {
        const server = http.createServer(async (req, res) => {
            if (!req.url?.startsWith("/oauth2callback"))
                return;
            const url = new URL(req.url, "http://localhost:3001");
            const code = url.searchParams.get("code");
            if (!code) {
                res.writeHead(400);
                res.end("ไม่พบ Authorization Code");
                reject(new Error("No code"));
                return;
            }
            try {
                const { tokens } = await oauth2Client.getToken(code);
                oauth2Client.setCredentials(tokens);
                fs.writeFileSync(TOKEN_PATH, JSON.stringify(tokens, null, 2));
                res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
                res.end(`
          <html><body style="font-family:sans-serif;padding:40px;background:#f7f3e9">
          <h2 style="color:#16a34a">✅ เชื่อมต่อ Google สำเร็จ!</h2>
          <p>Refresh Token บันทึกแล้ว ปิดหน้าต่างนี้และกลับไปที่ Terminal</p>
          <pre style="background:#fff;padding:20px;border-radius:8px">${tokens.refresh_token}</pre>
          <p>คัดลอก Refresh Token ด้านบนไปใส่ใน .env</p>
          </body></html>
        `);
                console.log("✅ Authentication สำเร็จ!");
                console.log(`📝 Refresh Token: ${tokens.refresh_token}`);
                console.log(`\nคัดลอกไปใส่ใน .env:\nGOOGLE_REFRESH_TOKEN=${tokens.refresh_token}`);
                server.close();
                resolve();
            }
            catch (err) {
                res.writeHead(500);
                res.end("เกิดข้อผิดพลาด");
                reject(err);
            }
        });
        server.listen(3001, () => {
            console.log("🚀 Callback server รอรับ Token บน port 3001...");
        });
        server.on("error", reject);
    });
}
