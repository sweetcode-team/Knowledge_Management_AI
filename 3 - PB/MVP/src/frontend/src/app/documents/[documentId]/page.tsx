import {getDocumentContent} from "@/lib/actions";
import {DocumentViewer} from "@/app/documents/[documentId]/components/document-viewer";

export default async function DocumentPage({ params }: { params: { documentId: string } }) {
    const documentContent = await getDocumentContent(params.documentId)
    return (
        <div className="flex h-full flex-col">
            <DocumentViewer document={documentContent} />
        </div >
    )
}
