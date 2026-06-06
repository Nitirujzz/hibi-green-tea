import { drive_v3, Auth } from "googleapis";
import { OAuth2Client } from "google-auth-library";
export type DriveFile = drive_v3.Schema$File;
export declare const HIBI_FOLDER_STRUCTURE: {
    readonly root: "📁 Hibi Matcha — Marketing Hub";
    readonly children: {
        readonly "01_Marketing_Plan": {
            readonly name: "📊 01 — Marketing Plan";
            readonly children: {
                readonly Annual_Plans: "📅 Annual Plans";
                readonly Campaign_Briefs: "📋 Campaign Briefs";
                readonly Budgets: "💰 Budgets & Finance";
            };
        };
        readonly "02_Creative_Assets": {
            readonly name: "🎨 02 — Creative Assets";
            readonly children: {
                readonly Facebook_Instagram: "📸 Facebook & Instagram";
                readonly TikTok: "🎵 TikTok Videos & Scripts";
                readonly Grab_LineMan_Wongnai: "🛵 Delivery Platform Banners";
                readonly Brand_Guidelines: "🎨 Brand Guidelines";
                readonly Templates: "📐 Design Templates";
            };
        };
        readonly "03_Media_Buying": {
            readonly name: "📢 03 — Media Buying";
            readonly children: {
                readonly Meta_Ads: "💙 Meta Ads (FB + IG)";
                readonly TikTok_Ads: "🎵 TikTok Ads";
                readonly Google_Ads: "🔍 Google Ads";
                readonly Reports: "📈 Ad Performance Reports";
            };
        };
        readonly "04_Analytics": {
            readonly name: "📈 04 — Analytics & Data";
            readonly children: {
                readonly Weekly_Reports: "📊 Weekly Reports";
                readonly Monthly_Reports: "📅 Monthly Reports";
                readonly AB_Tests: "🧪 A/B Test Results";
                readonly Dashboards: "🖥️ Dashboard Exports";
                readonly AI_Learning: "🤖 AI Audit & Learning Reports";
            };
        };
        readonly "05_Food_Delivery": {
            readonly name: "🛵 05 — Food Delivery Platforms";
            readonly children: {
                readonly Grab: "🟢 Grab";
                readonly LINE_MAN: "🟡 LINE MAN";
                readonly Wongnai: "🔴 Wongnai Food";
                readonly GMV_Reports: "💰 GMV & Sales Reports";
            };
        };
        readonly "06_CRM_Loyalty": {
            readonly name: "💌 06 — CRM & Loyalty";
            readonly children: {
                readonly Email_Templates: "✉️ Email Templates & Flows";
                readonly LINE_OA: "💬 LINE Official Account";
                readonly Loyalty_Program: "⭐ Hibi Tea Club";
                readonly Customer_Segments: "👥 Customer Segments";
            };
        };
        readonly "07_Influencer": {
            readonly name: "🌟 07 — Influencer & Growth";
            readonly children: {
                readonly KOL_Database: "📋 KOL Database & Scorecards";
                readonly Campaign_Reports: "📊 Campaign Reports";
                readonly Partnerships: "🤝 B2B & Partnerships";
                readonly Referral_Program: "🔗 Referral Program";
            };
        };
        readonly "08_AI_Agents": {
            readonly name: "🤖 08 — AI Agents & Automation";
            readonly children: {
                readonly Agent_Docs: "📄 Agent Documentation";
                readonly Prompts: "💡 Prompt Library";
                readonly Audit_Reports: "🔍 AI Audit Reports";
                readonly Learning_Reports: "🧠 AI Learning Reports";
            };
        };
        readonly "09_Meeting_Notes": {
            readonly name: "📝 09 — Meeting Notes & Summaries";
            readonly children: {
                readonly Weekly: "📅 Weekly Syncs";
                readonly Campaign_Reviews: "🎯 Campaign Reviews";
                readonly Strategy_Sessions: "🗺️ Strategy Sessions";
            };
        };
    };
};
export declare class GoogleDriveService {
    private drive;
    constructor(auth: OAuth2Client | Auth.GoogleAuth);
    createFolder(name: string, parentId?: string): Promise<string>;
    findOrCreateFolder(name: string, parentId?: string): Promise<string>;
    setupHibiFolderStructure(): Promise<Record<string, string>>;
    uploadFile(name: string, content: string, mimeType: string, parentId?: string): Promise<{
        id: string;
        webViewLink: string;
    }>;
    listFolder(folderId: string): Promise<DriveFile[]>;
    getFileLink(fileId: string): Promise<string>;
    moveFile(fileId: string, newParentId: string): Promise<void>;
}
