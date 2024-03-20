"use client"
import type {
    Chat,
    ChatPreview,
    Configuration,
    DocumentContent,
    DocumentOperationResponse,
    MessageResponse
} from '@/types/types'
import {toast} from "sonner";
import {useEffect, useState} from "react";

async function getDocuments(id : string): Promise<DocumentContent[]> {
  const result = await fetch(`http://localhost:4000/getDocuments/${id}`)
  return result.json()
}
async function getDocumentContent(id: string): Promise<DocumentContent> {
  const result = await fetch(`http://localhost:4000/getDocumentContent/${id}`, { cache: 'no-store' })
  return result.json()
}
async function getChats(id: string):Promise<ChatPreview[]> {
    const result = await fetch(`http://localhost:4000/getChats/${id}`, { cache: 'no-store' })
    return result.json()
}
async function getChatMessages(id: string): Promise<Chat> {
    const result = await fetch(`http://localhost:4000/getChatMessages/${id}`, { cache: 'no-store' })
    return result.json()
}
async function getConfiguration(): Promise<Configuration> {
    const result = await fetch(`http://localhost:4000/getConfiguration`, { cache: 'no-store' })
    return result.json()
}
async function askChatbot(id: string): Promise<MessageResponse> {
    const message = "chi è andrea barutta?";
    const formData = new URLSearchParams();
    formData.append('message', message);

    const response = await fetch('http://localhost:4000/askChatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    });


     // Attendiamo che il corpo della risposta sia disponibile
    return await response.json(); // Restituiamo i dati JSON ricevuti dalla richiesta
}
//TODO delete document
async function deleteDocument(ids: string[]): Promise<DocumentOperationResponse> {
    const result = await fetch(`http://localhost:4000/deleteDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: JSON.stringify({'documentIds': 'SWE_Concepts.pdf'})
        }
    )
    return result.json()
}
export default function HomeDeleteDocument() {
    const [documentOperationResponse, setDocumentOperationResponse] = useState<DocumentOperationResponse | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const documentOperationResponse = await deleteDocument(["SWE_Concepts.pdf"]);
                setDocumentOperationResponse(documentOperationResponse);
                console.log(documentOperationResponse);
            } catch (error) {
                console.error('Errore durante la richiesta:', error);
            }
        };

        fetchData(); // Chiamare fetchData al di fuori del blocco try-catch
    }, []); // Passare un array vuoto come dipendenza per eseguire l'effetto solo al mount

    return (
        <div>
                <div>
                    <p>Document ID: {documentOperationResponse?.documentId}</p>
                    <p>Status: {documentOperationResponse?.status}</p>
                    <p>Message: {documentOperationResponse?.message}</p>
                </div>
        </div>
    );
}
/*
export function HomeAskChatbot(message: string){
    const [messageResponse, setMessageResponse] = useState<MessageResponse | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const messageResponse = await askChatbot("2");
                setMessageResponse(messageResponse);
                console.log(messageResponse)
            } catch (error) {
                console.error('Errore durante la richiesta:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <p>{messageResponse?.chatId}</p>
            <p>{messageResponse?.status}</p>
            <p>{messageResponse?.messageResponse.content}</p>
        </div>
    );
}

export async function HomeDeleteDocument() {
    const result = deleteDocument("2024-02-19.pdf")
    result.then(() => {
        toast.success('Documento eliminato');
    });
}
export async function HomeGetConfiguration() {
    const configuration = await getConfiguration();
    return (
        <div>
            <p>
                {configuration.vectorStore.name}
            </p>
            <p>
                {configuration.LLMModel.name}
            </p>
            <p>
                {configuration.documentStore.name}
            </p>
            <p>
                {configuration.embeddingModel.name}
            </p>
        </div>
    );

}

export async function HomegetChatMessages(){
    const chatsMessages = await getChatMessages("2");
    return (
        <div>
            {chatsMessages.messages.map((message) => (
                <div key={message.sender}>
                    <p>{message.sender}</p>
                    <p>{message.content}</p>
                    <p>{message.timestamp}</p>
                    <p>{message.relevantDocuments?.map((relevantDocument) => (
                        <div key={relevantDocument.id}>
                            <p>{relevantDocument.id}</p>
                        </div>
                    ))}
                    </p>
                </div>
            ))}
        </div>
    );

}

export function HomegetDocumentContent2() {
    const [src, setSrc] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            const documentContent = await getDocumentContent("2024-02-19.pdf");
            const prova = Buffer.from(documentContent.content, 'hex');
            const blob = new Blob([prova], { type: 'application/pdf' });
            const pdfUrl = URL.createObjectURL(blob);
            setSrc(pdfUrl);
        };

        fetchData();
    }, []); // Empty dependency array ensures the effect runs only once on component mount

    return (
        <div>
            <a href={src} target="_blank"> prova </a>
        </div>
    );
}

export async function HomegetDocumentContent() {

    const [src, setSrc] = useState('');
     const documentContent = await getDocumentContent("2024-02-19.pdf");
    useEffect(() => {
         const prova = Buffer.from(documentContent.content, 'hex')
        const blob = new Blob([prova], { type: 'application/pdf' });
        //Object.assign(prova, {preview:  URL.createObjectURL(blob)});
        const pdfUrl = URL.createObjectURL(blob);
        setSrc(pdfUrl);
    }, [documentContent.content]);

    return (
        <div>
            <a href={src} target="_blank"> prova </a>
        </div>
    );

}

export async function HomegetDocuments(){
    const documents = await getDocuments("2024");
    return (
        <div>
        {documents.map((document) => (
            <div key={document.id}>
            <p>{document.id}</p>
            <p>{document.type}</p>
            <p>{document.size}</p>
            <p> {document.uploadDate}</p>
            <p> {document.status}</p>
            </div>
        ))}
        </div>
    );
}

export async function HomegetChats(){
    const chatPreviews = await getChats("2");
    return (
    <div>
        {chatPreviews.map((chatPreview) => (
            <div key={chatPreview.chatId}>
                <p>{chatPreview.chatId}</p>
                <p>{chatPreview.lastMessage.content}</p>
                <p>{chatPreview.lastMessage.timestamp}</p>
                <p>{chatPreview.lastMessage.sender}</p>
            </div>
        ))}
    </div>
  );
}
*/