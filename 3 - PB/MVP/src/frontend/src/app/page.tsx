import { ActionButton } from '@/components/action-button'
import { Button } from '@/components/ui/button';
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from '@/components/ui/resizable';
import { ScrollArea, ScrollBar } from '@/components/ui/scroll-area';
import { Separator } from '@/components/ui/separator';
import { Tooltip, TooltipContent, TooltipTrigger } from '@/components/ui/tooltip';
import { ExpandIcon, FilePlusIcon, MessageSquarePlusIcon } from 'lucide-react';
import { RecentChats } from "@/components/recent-chats"
import { RecentDocuments } from "@/components/recent-documents"
import Link from 'next/link';
import { documentSchema } from "@/app/documents/data/schema"
import { promises as fs } from "fs"
import { z } from "zod"
import path from "path"
import { ChatContent } from './chatbot/components/chat-content';
import { Label } from "@/components/ui/label"
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"
import type {
    Chat,
    ChatPreview,
    Configuration,
    DocumentContent,
    DocumentOperationResponse,
    MessageResponse
} from '@/types/types'
import {toast} from "sonner";
//import {useEffect, useState} from "react";
import {getDocuments} from "@/app/documents/page"

async function getDocumentContent(id: string): Promise<DocumentContent> {
  const result = await fetch(`http://localhost:4000/getDocumentContent/${id}`, { cache: 'no-store' })
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

export default async function Dashboard() {
  const documents = await getDocuments()

  const lastChats = [] as ChatPreview[]

  return (
    <ScrollArea className='h-full'>
      <div className="flex space-x-3 p-4">
        <ActionButton text={"Carica documento"} path={"/documents"}>
          <MessageSquarePlusIcon />
        </ActionButton>
        <ActionButton text={"Nuova chat"} path={"/chatbot"}>
          <FilePlusIcon />
        </ActionButton>
      </div>
      <Separator />
      <div className="">
        <ResizablePanelGroup direction="horizontal" className="min-h-[50vh] max-h-[100vh]">
          <ResizablePanel defaultSize={60} minSize={55}>
            <div className="px-2 w-full flex justify-between align-top">
              <h3 className="pt-2 ml-3 font-semibold text-nowrap">Last chat</h3>
              <ScrollArea className='w-full h-[50vh]'>
                <div className="m-auto p-3 pb-0">
                </div>
              </ScrollArea>
              <Tooltip>
                <TooltipTrigger className="pt-2 h-6 w-6">
                  <Link href="/chatbot/page">
                    <ExpandIcon className="text-border hover:text-primary" />
                  </Link>
                </TooltipTrigger>
                <TooltipContent>
                  Espandi
                </TooltipContent>
              </Tooltip>
            </div>
            {/* <ChatBody /> */}
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={40} minSize={35}>
            <ScrollArea className='h-[50vh] mr-2'>
              <div className="p-2">
                <h3 className="ml-3 font-semibold  mb-2">Recently visited chats</h3>
              </div>
            </ScrollArea>
          </ResizablePanel>
        </ResizablePanelGroup>
        <Separator />
        <div className="min-h-[50vh] max-h-[70vh] p-2">
          <h3 className="ml-3 font-semibold mb-2">Recent documents</h3>
          <Tabs defaultValue="uploaded">
            <TabsList className="grid grid-cols-2 mx-4 md:mx-auto md:w-6/12 max-w-[800px] mb-4">
              <TabsTrigger value="uploaded">Recently uploaded</TabsTrigger>
              <TabsTrigger value="viewed">Recently viewed</TabsTrigger>
            </TabsList>
            <TabsContent value="uploaded">
              <ScrollArea className='h-[50vh] px-2'>
                <RecentDocuments
                  items={
                    documents
                      .sort((a, b) => new Date(b.uploadDate).getTime() - new Date(a.uploadDate).getTime())
                      .slice(0, 12)
                  }
                />
              </ScrollArea>
            </TabsContent>
            <TabsContent value="viewed">
              <ScrollArea className='h-[50vh] px-2'>
                <RecentDocuments items={documents} />
              </ScrollArea>
            </TabsContent>
          </Tabs>
        </div>
      </div >
    </ScrollArea>
  )}

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