import { docs_v1 } from "googleapis";
import { OAuth2Client } from "google-auth-library";
export declare class GoogleDocsService {
    private docs;
    private drive;
    constructor(auth: OAuth2Client);
    createDoc(title: string, parentFolderId?: string): Promise<{
        id: string;
        url: string;
    }>;
    appendContent(docId: string, requests: docs_v1.Schema$Request[]): Promise<void>;
    writeMarkdownToDoc(docId: string, markdown: string): Promise<void>;
    private markdownToDocRequests;
    getDocContent(docId: string): Promise<string>;
    createSessionSummaryDoc(parentFolderId: string, summaryContent: string, sessionDate: string): Promise<{
        id: string;
        url: string;
    }>;
}
