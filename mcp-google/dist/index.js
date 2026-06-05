import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import * as dotenv from "dotenv";
import * as path from "path";
import * as fs from "fs";
import { fileURLToPath } from "url";
import { createOAuth2Client, runAuthFlow } from "./auth.js";
import { GoogleDriveService } from "./google-drive.js";
import { GoogleDocsService } from "./google-docs.js";
import { SESSION_SUMMARY, SESSION_DATE } from "./summary.js";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: path.join(__dirname, "..", ".env") });
// ─── จัดการ Auth Flow เมื่อ run ด้วย --auth flag ───────────────────────────
if (process.argv.includes("--auth")) {
    await runAuthFlow();
    process.exit(0);
}
// ─── Server Setup ────────────────────────────────────────────────────────────
const server = new McpServer({
    name: "hibi-google-workspace",
    version: "1.0.0",
});
function getServices() {
    const auth = createOAuth2Client();
    return {
        drive: new GoogleDriveService(auth),
        docs: new GoogleDocsService(auth),
    };
}
// ─── TOOL: สร้าง Folder Structure ทั้งหมดใน Google Drive ────────────────────
server.tool("setup_hibi_drive", "สร้างโครงสร้าง Folder ทั้งหมดสำหรับ Hibi Matcha ใน Google Drive (9 หมวดหลัก)", {}, async () => {
    const { drive } = getServices();
    const ids = await drive.setupHibiFolderStructure();
    const rootLink = `https://drive.google.com/drive/folders/${ids["root"]}`;
    const folderList = Object.entries(ids)
        .filter(([k]) => !k.includes("/"))
        .map(([k, id]) => `• ${k}: https://drive.google.com/drive/folders/${id}`)
        .join("\n");
    // บันทึก IDs ไว้ใช้งานครั้งต่อไป
    const idsPath = path.join(__dirname, "..", ".folder-ids.json");
    fs.writeFileSync(idsPath, JSON.stringify(ids, null, 2));
    return {
        content: [
            {
                type: "text",
                text: `✅ สร้าง Folder Structure สำเร็จ!\n\n📁 Root: ${rootLink}\n\n${folderList}\n\nFolder IDs บันทึกไว้ที่ .folder-ids.json`,
            },
        ],
    };
});
// ─── TOOL: สร้าง Google Doc ใหม่ ────────────────────────────────────────────
server.tool("create_google_doc", "สร้าง Google Document ใหม่ใน Folder ที่กำหนด", {
    title: z.string().describe("ชื่อเอกสาร"),
    content: z.string().optional().describe("เนื้อหาเริ่มต้น (Markdown)"),
    folder_key: z
        .string()
        .optional()
        .describe("Key ของ Folder จาก setup (เช่น '09_Meeting_Notes/Weekly', '04_Analytics/Monthly_Reports')"),
}, async ({ title, content, folder_key }) => {
    const { docs } = getServices();
    let parentId;
    if (folder_key) {
        const idsPath = path.join(__dirname, "..", ".folder-ids.json");
        if (fs.existsSync(idsPath)) {
            const ids = JSON.parse(fs.readFileSync(idsPath, "utf-8"));
            parentId = ids[folder_key];
        }
    }
    const doc = await docs.createDoc(title, parentId);
    if (content) {
        await docs.writeMarkdownToDoc(doc.id, content);
    }
    return {
        content: [
            {
                type: "text",
                text: `✅ สร้าง Document สำเร็จ!\n📄 ชื่อ: ${title}\n🔗 Link: ${doc.url}\n📁 Folder: ${folder_key || "My Drive (root)"}`,
            },
        ],
    };
});
// ─── TOOL: สร้าง Session Summary Doc อัตโนมัติ ──────────────────────────────
server.tool("create_session_summary", "สร้าง Google Doc สรุปบทสนทนาปัจจุบันโดยอัตโนมัติ แล้วบันทึกใน Folder Meeting Notes", {
    custom_content: z
        .string()
        .optional()
        .describe("เนื้อหาเพิ่มเติม (ถ้าไม่ระบุจะใช้ Summary มาตรฐาน)"),
}, async ({ custom_content }) => {
    const { docs } = getServices();
    const idsPath = path.join(__dirname, "..", ".folder-ids.json");
    let parentId;
    if (fs.existsSync(idsPath)) {
        const ids = JSON.parse(fs.readFileSync(idsPath, "utf-8"));
        parentId = ids["09_Meeting_Notes/Strategy_Sessions"];
    }
    const content = custom_content || SESSION_SUMMARY;
    const doc = await docs.createSessionSummaryDoc(parentId || "", content, SESSION_DATE);
    return {
        content: [
            {
                type: "text",
                text: `✅ สร้าง Session Summary สำเร็จ!\n📄 ชื่อ: Hibi Matcha — Session Summary ${SESSION_DATE}\n🔗 Link: ${doc.url}\n📁 บันทึกใน: 09 Meeting Notes / Strategy Sessions`,
            },
        ],
    };
});
// ─── TOOL: อัปโหลดไฟล์ขึ้น Drive ────────────────────────────────────────────
server.tool("upload_to_drive", "อัปโหลดไฟล์จาก Repository ขึ้น Google Drive", {
    file_path: z.string().describe("Path ของไฟล์ใน Repository"),
    folder_key: z
        .string()
        .describe("Key ของ Folder ปลายทาง (เช่น '01_Marketing_Plan/Annual_Plans')"),
    rename: z.string().optional().describe("ชื่อใหม่ของไฟล์ (optional)"),
}, async ({ file_path, folder_key, rename }) => {
    const { drive } = getServices();
    const fullPath = path.join("/home/user/hibi-green-tea", file_path);
    if (!fs.existsSync(fullPath)) {
        return {
            content: [{ type: "text", text: `❌ ไม่พบไฟล์: ${fullPath}` }],
        };
    }
    const content = fs.readFileSync(fullPath, "utf-8");
    const fileName = rename || path.basename(file_path);
    const idsPath = path.join(__dirname, "..", ".folder-ids.json");
    let parentId;
    if (fs.existsSync(idsPath)) {
        const ids = JSON.parse(fs.readFileSync(idsPath, "utf-8"));
        parentId = ids[folder_key];
    }
    const result = await drive.uploadFile(fileName, content, "text/plain", parentId);
    return {
        content: [
            {
                type: "text",
                text: `✅ อัปโหลดสำเร็จ!\n📄 ไฟล์: ${fileName}\n🔗 Link: ${result.webViewLink}\n📁 Folder: ${folder_key}`,
            },
        ],
    };
});
// ─── TOOL: อัปโหลดเอกสารการตลาดทั้งหมด ──────────────────────────────────────
server.tool("upload_all_marketing_docs", "อัปโหลดเอกสารการตลาดทั้งหมดใน Repository ขึ้น Google Drive ตาม Folder Structure", {}, async () => {
    const { drive } = getServices();
    const idsPath = path.join(__dirname, "..", ".folder-ids.json");
    if (!fs.existsSync(idsPath)) {
        return {
            content: [
                {
                    type: "text",
                    text: "❌ ยังไม่ได้สร้าง Folder Structure — กรุณารัน setup_hibi_drive ก่อน",
                },
            ],
        };
    }
    const ids = JSON.parse(fs.readFileSync(idsPath, "utf-8"));
    const baseDir = "/home/user/hibi-green-tea";
    const fileMap = [
        { file: "MARKETING-PLAN.md", folderKey: "01_Marketing_Plan/Annual_Plans" },
        { file: "MARKETING-AGENTS.md", folderKey: "08_AI_Agents/Agent_Docs" },
        { file: "MARKETING-AI-LEARNING-SYSTEM.md", folderKey: "08_AI_Agents/Learning_Reports" },
        { file: "HIBI-BRAND-GUIDE.md", folderKey: "02_Creative_Assets/Brand_Guidelines" },
    ];
    const results = [];
    for (const { file, folderKey } of fileMap) {
        const fullPath = path.join(baseDir, file);
        if (!fs.existsSync(fullPath))
            continue;
        const content = fs.readFileSync(fullPath, "utf-8");
        const parentId = ids[folderKey];
        const result = await drive.uploadFile(file, content, "text/plain", parentId);
        results.push(`✅ ${file} → ${folderKey}\n   🔗 ${result.webViewLink}`);
    }
    return {
        content: [
            {
                type: "text",
                text: `📤 อัปโหลดเอกสารทั้งหมดสำเร็จ!\n\n${results.join("\n\n")}`,
            },
        ],
    };
});
// ─── TOOL: แสดงรายการ Folder ────────────────────────────────────────────────
server.tool("list_drive_folder", "แสดงรายการไฟล์และ Folder ใน Google Drive", {
    folder_key: z
        .string()
        .optional()
        .describe("Key ของ Folder (ถ้าไม่ระบุจะแสดง Root)"),
}, async ({ folder_key }) => {
    const { drive } = getServices();
    const idsPath = path.join(__dirname, "..", ".folder-ids.json");
    if (!fs.existsSync(idsPath)) {
        return {
            content: [{ type: "text", text: "❌ ยังไม่มี Folder IDs — รัน setup_hibi_drive ก่อน" }],
        };
    }
    const ids = JSON.parse(fs.readFileSync(idsPath, "utf-8"));
    const folderId = folder_key ? ids[folder_key] : ids["root"];
    if (!folderId) {
        return {
            content: [{ type: "text", text: `❌ ไม่พบ Folder: ${folder_key}` }],
        };
    }
    const files = await drive.listFolder(folderId);
    if (files.length === 0) {
        return {
            content: [{ type: "text", text: `📁 Folder ${folder_key || "root"} ว่างเปล่า` }],
        };
    }
    const fileList = files
        .map((f) => {
        const isFolder = f.mimeType === "application/vnd.google-apps.folder";
        const icon = isFolder ? "📁" : "📄";
        return `${icon} ${f.name}\n   🔗 ${f.webViewLink}`;
    })
        .join("\n\n");
    return {
        content: [
            {
                type: "text",
                text: `📂 เนื้อหาใน Folder: ${folder_key || "Hibi Matcha Root"}\n\n${fileList}`,
            },
        ],
    };
});
// ─── TOOL: สร้าง Google Doc สำหรับ Audit Report ────────────────────────────
server.tool("create_audit_report_doc", "สร้าง Google Doc สำหรับ AI Audit Report รายสัปดาห์", {
    week_number: z.number().describe("สัปดาห์ที่ (เช่น 24)"),
    year: z.number().describe("ปี (เช่น 2026)"),
    content: z.string().describe("เนื้อหา Audit Report"),
}, async ({ week_number, year, content }) => {
    const { docs } = getServices();
    const idsPath = path.join(__dirname, "..", ".folder-ids.json");
    let parentId;
    if (fs.existsSync(idsPath)) {
        const ids = JSON.parse(fs.readFileSync(idsPath, "utf-8"));
        parentId = ids["08_AI_Agents/Audit_Reports"];
    }
    const title = `🔍 AI Audit Report — Week ${week_number}/${year}`;
    const doc = await docs.createDoc(title, parentId);
    await docs.writeMarkdownToDoc(doc.id, content);
    return {
        content: [
            {
                type: "text",
                text: `✅ สร้าง Audit Report Doc สำเร็จ!\n📄 ชื่อ: ${title}\n🔗 Link: ${doc.url}\n📁 บันทึกใน: 08 AI Agents / Audit Reports`,
            },
        ],
    };
});
// ─── Start Server ────────────────────────────────────────────────────────────
const transport = new StdioServerTransport();
await server.connect(transport);
console.error("🍵 Hibi Matcha Google Workspace MCP Server — พร้อมทำงาน");
