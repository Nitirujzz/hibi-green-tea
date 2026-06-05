import { google, drive_v3 } from "googleapis";
import { OAuth2Client } from "google-auth-library";

export type DriveFile = drive_v3.Schema$File;

// โครงสร้าง Folder สำหรับ Hibi Matcha
export const HIBI_FOLDER_STRUCTURE = {
  root: "📁 Hibi Matcha — Marketing Hub",
  children: {
    "01_Marketing_Plan": {
      name: "📊 01 — Marketing Plan",
      children: {
        "Annual_Plans": "📅 Annual Plans",
        "Campaign_Briefs": "📋 Campaign Briefs",
        "Budgets": "💰 Budgets & Finance",
      },
    },
    "02_Creative_Assets": {
      name: "🎨 02 — Creative Assets",
      children: {
        "Facebook_Instagram": "📸 Facebook & Instagram",
        "TikTok": "🎵 TikTok Videos & Scripts",
        "Grab_LineMan_Wongnai": "🛵 Delivery Platform Banners",
        "Brand_Guidelines": "🎨 Brand Guidelines",
        "Templates": "📐 Design Templates",
      },
    },
    "03_Media_Buying": {
      name: "📢 03 — Media Buying",
      children: {
        "Meta_Ads": "💙 Meta Ads (FB + IG)",
        "TikTok_Ads": "🎵 TikTok Ads",
        "Google_Ads": "🔍 Google Ads",
        "Reports": "📈 Ad Performance Reports",
      },
    },
    "04_Analytics": {
      name: "📈 04 — Analytics & Data",
      children: {
        "Weekly_Reports": "📊 Weekly Reports",
        "Monthly_Reports": "📅 Monthly Reports",
        "AB_Tests": "🧪 A/B Test Results",
        "Dashboards": "🖥️ Dashboard Exports",
        "AI_Learning": "🤖 AI Audit & Learning Reports",
      },
    },
    "05_Food_Delivery": {
      name: "🛵 05 — Food Delivery Platforms",
      children: {
        "Grab": "🟢 Grab",
        "LINE_MAN": "🟡 LINE MAN",
        "Wongnai": "🔴 Wongnai Food",
        "GMV_Reports": "💰 GMV & Sales Reports",
      },
    },
    "06_CRM_Loyalty": {
      name: "💌 06 — CRM & Loyalty",
      children: {
        "Email_Templates": "✉️ Email Templates & Flows",
        "LINE_OA": "💬 LINE Official Account",
        "Loyalty_Program": "⭐ Hibi Tea Club",
        "Customer_Segments": "👥 Customer Segments",
      },
    },
    "07_Influencer": {
      name: "🌟 07 — Influencer & Growth",
      children: {
        "KOL_Database": "📋 KOL Database & Scorecards",
        "Campaign_Reports": "📊 Campaign Reports",
        "Partnerships": "🤝 B2B & Partnerships",
        "Referral_Program": "🔗 Referral Program",
      },
    },
    "08_AI_Agents": {
      name: "🤖 08 — AI Agents & Automation",
      children: {
        "Agent_Docs": "📄 Agent Documentation",
        "Prompts": "💡 Prompt Library",
        "Audit_Reports": "🔍 AI Audit Reports",
        "Learning_Reports": "🧠 AI Learning Reports",
      },
    },
    "09_Meeting_Notes": {
      name: "📝 09 — Meeting Notes & Summaries",
      children: {
        "Weekly": "📅 Weekly Syncs",
        "Campaign_Reviews": "🎯 Campaign Reviews",
        "Strategy_Sessions": "🗺️ Strategy Sessions",
      },
    },
  },
} as const;

export class GoogleDriveService {
  private drive: drive_v3.Drive;

  constructor(auth: OAuth2Client) {
    this.drive = google.drive({ version: "v3", auth });
  }

  async createFolder(name: string, parentId?: string): Promise<string> {
    const metadata: drive_v3.Schema$File = {
      name,
      mimeType: "application/vnd.google-apps.folder",
      ...(parentId ? { parents: [parentId] } : {}),
    };

    const res = await this.drive.files.create({
      requestBody: metadata,
      fields: "id, name, webViewLink",
    });

    return res.data.id!;
  }

  async findOrCreateFolder(name: string, parentId?: string): Promise<string> {
    const query = [
      `name = '${name}'`,
      `mimeType = 'application/vnd.google-apps.folder'`,
      `trashed = false`,
      ...(parentId ? [`'${parentId}' in parents`] : []),
    ].join(" and ");

    const res = await this.drive.files.list({
      q: query,
      fields: "files(id, name)",
      spaces: "drive",
    });

    if (res.data.files && res.data.files.length > 0) {
      return res.data.files[0].id!;
    }

    return this.createFolder(name, parentId);
  }

  async setupHibiFolderStructure(): Promise<Record<string, string>> {
    const ids: Record<string, string> = {};

    const rootId = await this.findOrCreateFolder(HIBI_FOLDER_STRUCTURE.root);
    ids["root"] = rootId;

    for (const [key, value] of Object.entries(HIBI_FOLDER_STRUCTURE.children)) {
      const parentId = await this.findOrCreateFolder(value.name, rootId);
      ids[key] = parentId;

      for (const [childKey, childName] of Object.entries(value.children)) {
        const childId = await this.findOrCreateFolder(childName as string, parentId);
        ids[`${key}/${childKey}`] = childId;
      }
    }

    return ids;
  }

  async uploadFile(
    name: string,
    content: string,
    mimeType: string,
    parentId?: string
  ): Promise<{ id: string; webViewLink: string }> {
    const { Readable } = await import("stream");
    const stream = Readable.from([content]);

    const res = await this.drive.files.create({
      requestBody: {
        name,
        mimeType,
        ...(parentId ? { parents: [parentId] } : {}),
      },
      media: {
        mimeType: "text/plain",
        body: stream,
      },
      fields: "id, name, webViewLink",
    });

    return {
      id: res.data.id!,
      webViewLink: res.data.webViewLink!,
    };
  }

  async listFolder(folderId: string): Promise<DriveFile[]> {
    const res = await this.drive.files.list({
      q: `'${folderId}' in parents and trashed = false`,
      fields: "files(id, name, mimeType, webViewLink, createdTime, modifiedTime)",
      orderBy: "name",
    });
    return res.data.files || [];
  }

  async getFileLink(fileId: string): Promise<string> {
    const res = await this.drive.files.get({
      fileId,
      fields: "webViewLink",
    });
    return res.data.webViewLink || `https://drive.google.com/file/d/${fileId}`;
  }

  async moveFile(fileId: string, newParentId: string): Promise<void> {
    const file = await this.drive.files.get({
      fileId,
      fields: "parents",
    });

    const previousParents = file.data.parents?.join(",") || "";

    await this.drive.files.update({
      fileId,
      addParents: newParentId,
      removeParents: previousParents,
      fields: "id, parents",
    });
  }
}
