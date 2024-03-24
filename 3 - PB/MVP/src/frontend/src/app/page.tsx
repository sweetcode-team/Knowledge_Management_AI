import { ActionButton } from '@/components/action-button'
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from '@/components/ui/resizable';
import { ScrollArea, ScrollBar } from '@/components/ui/scroll-area';
import { Separator } from '@/components/ui/separator';
import { Tooltip, TooltipContent, TooltipTrigger } from '@/components/ui/tooltip';
import { ExpandIcon, FilePlusIcon, MessageSquarePlusIcon } from 'lucide-react';
import { RecentChats } from "@/components/recent-chats"
import { RecentDocuments } from "@/components/recent-documents"
import Link from 'next/link';

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

import { getChats, getDocuments, getChatMessages } from '@/lib/actions';
import { ChatContent } from './chatbot/components/chat-content';
import { useEffect } from 'react';
import { toast } from 'sonner';

export default async function Dashboard() {
  const documents = await getDocuments()
  const chats = await getChats()

  const recentlyViewedDocumentIds = new Set(chats.map((chat: ChatPreview) => chat.lastMessage.relevantDocuments).flat())

  const recentlyViewedDocuments = documents.filter((document) => recentlyViewedDocumentIds.has(document.id))

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
      <div>
        <ResizablePanelGroup direction="horizontal" className="min-h-[50vh] max-h-[100vh]">
          <ResizablePanel defaultSize={60} minSize={55}>
            <div className="px-2 w-full flex justify-between align-top">
              <h3 className="pt-2 ml-3 font-semibold text-nowrap">Last chat</h3>
              <ScrollArea className='w-full h-[50vh]'>
                <div className="m-auto p-3 pb-0 h-full">
                  <ChatContent messages={chats[0] ? [chats[0].lastMessage] : []} />
                </div>
              </ScrollArea>
              <Tooltip>
                <TooltipTrigger className="pt-2 h-6 w-6">
                  <Link href="/chatbot">
                    <ExpandIcon className="text-border hover:text-primary" />
                  </Link>
                </TooltipTrigger>
                <TooltipContent>
                  Enlarge
                </TooltipContent>
              </Tooltip>
            </div>
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={40} minSize={35}>
            <ScrollArea className='h-[50vh] mr-2'>
              <div className="p-2">
                <h3 className="ml-3 font-semibold  mb-2">Recent chats</h3>
                {
                  chats.length !== 0 ?
                    <RecentChats chats={
                      chats
                        .sort((a, b) => new Date(b.lastMessage.timestamp).getTime() - new Date(a.lastMessage.timestamp).getTime())
                        .slice(0, 6)
                    } />
                    :
                    <p className='text-center text-sm mt-4'>
                      No recent chats.
                    </p>
                }

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
                {
                  documents ?
                    <RecentDocuments
                      items={
                        documents
                          .sort((a, b) => new Date(b.uploadTime).getTime() - new Date(a.uploadTime).getTime())
                          .slice(0, 12)
                      }
                    />
                    :
                    <p className='text-center text-sm mt-4'>
                      No recently uploaded documents.
                    </p>
                }
              </ScrollArea>
            </TabsContent>
            <TabsContent value="viewed">
              <ScrollArea className='h-[50vh] px-2'>
                {
                  recentlyViewedDocuments.length !== 0 ?
                    <RecentDocuments
                      items={recentlyViewedDocuments}
                    />
                    :
                    <p className='text-center text-sm mt-4'>
                      No recently viewed documents.
                    </p>
                }
              </ScrollArea>
            </TabsContent>
          </Tabs>
        </div>
      </div >
    </ScrollArea>
  )
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
            <p> {document.uploadTime}</p>
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