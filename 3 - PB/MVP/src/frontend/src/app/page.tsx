import { ActionButton } from '@/components/action-button'
import { Button } from '@/components/ui/button';
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from '@/components/ui/resizable';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Separator } from '@/components/ui/separator';
import { Tooltip, TooltipContent, TooltipTrigger } from '@/components/ui/tooltip';
import { ExpandIcon, FilePlusIcon, MessageSquarePlusIcon } from 'lucide-react';
import { Chat } from "@/app/chatbot/data"
import { RecentChats } from "@/app/chatbot/components/recent-chats"
import { RecentDocuments } from "@/app/chatbot/components/recent-documents"
import Link from 'next/link';
import { chats } from "@/app/chatbot/data"
import { documentSchema } from "@/app/documents/data/schema"
import { promises as fs } from "fs"
import { z } from "zod"
import path from "path"

async function getDocuments() {
  const data = await fs.readFile(
    path.join(process.cwd(), "src/app/documents/data/documents.json")
  )

  const documents = JSON.parse(data.toString())

  return z.array(documentSchema).parse(documents)
}


export default async function Dashboard() {
  const documents = await getDocuments()

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
        <ResizablePanelGroup direction="horizontal" className="min-h-[50vh] max-h-[50vh]">
          <ResizablePanel defaultSize={60} minSize={55}>
            <div className="px-2 flex justify-between align-top">
              <h3 className="pt-2 ml-3 font-semibold  mb-2">Last chat</h3>
              <ScrollArea className='h-[50vh]'>
                <div className="flex-1 px-2 text-center">

                </div>
              </ScrollArea>
              <Tooltip>
                <TooltipTrigger className="pt-2 h-6 w-6">
                  <Link href="/chatbot">
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
            <ScrollArea className='h-[50vh] mr-6'>
            <div className="p-2">       
            <h3 className="ml-3 font-semibold  mb-2">Recently visited chats</h3>      
             <RecentChats items={chats} />    
            </div> 
            </ScrollArea>
          </ResizablePanel>
        </ResizablePanelGroup>
        <Separator />
        <ResizablePanelGroup direction="horizontal" className="min-h-[50vh] max-h-[50vh]">
          <ResizablePanel defaultSize={50} minSize={40}>
            <div className="p-2">
              <h3 className="ml-3 font-semibold mb-2">Recently uploaded documents</h3>
            </div>
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={50} minSize={40}>
            <ScrollArea className='h-[50vh] mr-6'>
            <div className="p-2">
              <h3 className="ml-3 font-semibold mb-2">Recently viewed documents</h3>
                <RecentDocuments items={documents} />
            </div>
            </ScrollArea>
          </ResizablePanel>
        </ResizablePanelGroup>
      </div >
    </ScrollArea>
  )
}
