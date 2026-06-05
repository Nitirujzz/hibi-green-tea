import { google } from "googleapis";
export class GoogleDocsService {
    docs;
    drive;
    constructor(auth) {
        this.docs = google.docs({ version: "v1", auth });
        this.drive = google.drive({ version: "v3", auth });
    }
    async createDoc(title, parentFolderId) {
        const res = await this.docs.documents.create({
            requestBody: { title },
        });
        const docId = res.data.documentId;
        if (parentFolderId) {
            const file = await this.drive.files.get({ fileId: docId, fields: "parents" });
            const previousParents = file.data.parents?.join(",") || "";
            await this.drive.files.update({
                fileId: docId,
                addParents: parentFolderId,
                removeParents: previousParents,
                fields: "id, parents",
            });
        }
        return {
            id: docId,
            url: `https://docs.google.com/document/d/${docId}/edit`,
        };
    }
    async appendContent(docId, requests) {
        await this.docs.documents.batchUpdate({
            documentId: docId,
            requestBody: { requests },
        });
    }
    async writeMarkdownToDoc(docId, markdown) {
        const requests = this.markdownToDocRequests(markdown);
        if (requests.length > 0) {
            await this.appendContent(docId, requests);
        }
    }
    // แปลง Markdown พื้นฐานเป็น Google Docs Requests
    markdownToDocRequests(markdown) {
        const requests = [];
        const lines = markdown.split("\n");
        // เริ่มที่ index 1 (ท้ายสุด)
        let insertIndex = 1;
        const insertText = (text) => {
            requests.push({
                insertText: { location: { index: insertIndex }, text },
            });
            insertIndex += text.length;
        };
        const applyStyle = (startIndex, endIndex, style) => {
            requests.push({
                updateTextStyle: {
                    range: { startIndex, endIndex },
                    textStyle: style,
                    fields: Object.keys(style).join(","),
                },
            });
        };
        const applyParagraphStyle = (startIndex, endIndex, namedStyleType) => {
            requests.push({
                updateParagraphStyle: {
                    range: { startIndex, endIndex },
                    paragraphStyle: { namedStyleType },
                    fields: "namedStyleType",
                },
            });
        };
        for (const line of lines) {
            const lineStart = insertIndex;
            if (line.startsWith("# ")) {
                const text = line.slice(2) + "\n";
                insertText(text);
                applyParagraphStyle(lineStart, insertIndex - 1, "HEADING_1");
            }
            else if (line.startsWith("## ")) {
                const text = line.slice(3) + "\n";
                insertText(text);
                applyParagraphStyle(lineStart, insertIndex - 1, "HEADING_2");
            }
            else if (line.startsWith("### ")) {
                const text = line.slice(4) + "\n";
                insertText(text);
                applyParagraphStyle(lineStart, insertIndex - 1, "HEADING_3");
            }
            else if (line.startsWith("- ") || line.startsWith("* ")) {
                const text = line.slice(2) + "\n";
                insertText(text);
                requests.push({
                    createParagraphBullets: {
                        range: { startIndex: lineStart, endIndex: insertIndex - 1 },
                        bulletPreset: "BULLET_DISC_CIRCLE_SQUARE",
                    },
                });
            }
            else if (line.startsWith("**") && line.endsWith("**")) {
                const text = line.slice(2, -2) + "\n";
                insertText(text);
                applyStyle(lineStart, insertIndex - 1, { bold: true });
            }
            else {
                insertText(line + "\n");
            }
        }
        return requests;
    }
    async getDocContent(docId) {
        const res = await this.docs.documents.get({ documentId: docId });
        const body = res.data.body?.content || [];
        let text = "";
        for (const element of body) {
            if (element.paragraph) {
                for (const pe of element.paragraph.elements || []) {
                    text += pe.textRun?.content || "";
                }
            }
        }
        return text;
    }
    async createSessionSummaryDoc(parentFolderId, summaryContent, sessionDate) {
        const title = `📋 Hibi Matcha — Session Summary ${sessionDate}`;
        const doc = await this.createDoc(title, parentFolderId);
        await this.writeMarkdownToDoc(doc.id, summaryContent);
        return doc;
    }
}
