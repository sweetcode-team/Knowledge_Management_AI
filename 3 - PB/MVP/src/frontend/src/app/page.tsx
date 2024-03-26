import { ActionButton } from '@/components/action-button'
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from '@/components/ui/resizable';
import { ScrollArea } from '@/components/ui/scroll-area';
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
  LightDocument
} from '@/types/types'

import { getChats, getDocuments, getChatMessages } from '@/lib/actions';
import { ChatContent } from './chatbot/components/chat-content';

export default async function Dashboard() {
  let documents: LightDocument[] = []
  try {
    documents = await getDocuments()
  } catch (e) {
    console.error(e)
  }

  let chats: ChatPreview[] = []
  try {
    chats = await getChats()
  } catch (e) {
    console.error(e)
  }

  let lastChat: Chat | null = null
  if (chats.length !== 0) {
    lastChat = await getChatMessages(chats[0].id)
  }

  let recentlyViewedDocumentIds = new Set<string | undefined>()
  if (chats.length !== 0) {
    recentlyViewedDocumentIds = new Set(chats.map((chat: ChatPreview) => chat.lastMessage.relevantDocuments).flat())
  }

  let recentlyViewedDocuments: LightDocument[] = []
  if (documents.length !== 0) {
    console.log("\n\n\n\n\n\n", documents)
    recentlyViewedDocuments = documents.filter((document) => recentlyViewedDocumentIds.has(document.id))
  }

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
                  <ChatContent messages={lastChat?.messages} />
                </div>
              </ScrollArea>
              <Tooltip>
                <TooltipTrigger className="pt-2 h-6 w-6" hidden={!lastChat}>
                  <Link
                    href={`/chatbot/${lastChat?.id}`}
                  >
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