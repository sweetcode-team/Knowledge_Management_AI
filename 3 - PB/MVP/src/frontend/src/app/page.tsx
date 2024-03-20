import { ActionButton } from '@/components/action-button'
import { Button } from '@/components/ui/button';
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from '@/components/ui/resizable';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Separator } from '@/components/ui/separator';
import { Tooltip, TooltipContent, TooltipTrigger } from '@/components/ui/tooltip';
import { ExpandIcon, FilePlusIcon, MessageSquarePlusIcon } from 'lucide-react';
import Link from 'next/link';
import { ChatContent } from '@/app/chatbot/components/chat-content';
import { Chat } from '@/app/chatbot/data';

export default async function Dashboard() {

  const lastChat = {
    id: "6c84fb90-12c4-11eqrhqee1-840d-7b25c5ee775a",
    title: "William Smith",
    messages: [
      {
        role: "user",
        content: "Hello",
        timestamp: "2023-10-22T09:00:00",
        relevantDocuments: [
          "Document1.pdf",
          "Docx123.docx"
        ]
      },
      {
        role: "bot",
        content: "Hello, how can I help you?",
        timestamp: "2023-10-22T09:00:00",
        relevantDocuments: [
          "Documenfssf.pdf",
          "Docx123.docx"
        ]
      },
      {
        role: "user",
        content: "I would like to book an appointment",
        timestamp: "2023-10-22T09:00:00",
        relevantDocuments: [
          "Document1.pdf",
          "Docx1gr463.docx"
        ]
      },
      {
        role: "bot",
        content: "Sure, when would you like to book the appointment?",
        timestamp: "2023-10-22T09:00:00",
        relevantDocuments: [
          "Docxvf3425.docx",
          "Docccc99.pdf"
        ]
      },
      {
        role: "user",
        content: "Tomorrow",
        timestamp: "2023-10-22T09:00:00",
        relevantDocuments: [
          "Document1.pdf",
          "Docx123.docx"
        ]
      },
      {
        role: "bot",
        content: "What time?",
        timestamp: "2023-10-22T09:00:00",
        relevantDocuments: [
          "Document1.pdf",
          "Docx123.docx"
        ]
      },
      {
        role: "user",
        content: "9am",
        timestamp: "2023-10-22T09:00:00",
        relevantDocuments: [
          "Document1.pdf",
          "Docx123.docx"
        ]
      },
    ]
  } as Chat

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
            <div className="px-2 w-full flex justify-between align-top">
              <h3 className="pt-2 ml-3 font-semibold text-nowrap">Last chat</h3>
              <ScrollArea className='w-full h-[50vh]'>
                <div className="m-auto p-4 pb-0">
                  <ChatContent messages={lastChat.messages} />
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
            <div className="p-2">
              <h3 className="ml-3 font-semibold">Recent chats</h3>
            </div>
          </ResizablePanel>
        </ResizablePanelGroup>
        <Separator />
        <ResizablePanelGroup direction="horizontal" className="min-h-[50vh] max-h-[50vh]">
          <ResizablePanel defaultSize={50} minSize={40}>
            <div className="p-2">
              <h3 className="ml-3 font-semibold">Recently uploaded documents</h3>
            </div>
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel defaultSize={50} minSize={40}>
            <div className="p-2">
              <h3 className="ml-3 font-semibold">Recently viewed documents</h3>
            </div>
          </ResizablePanel>
        </ResizablePanelGroup>
      </div >
    </ScrollArea>
  )
}
