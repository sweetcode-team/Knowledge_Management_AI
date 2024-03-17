"use client"
import * as React from "react"
import {
  Search,
  MessageSquarePlusIcon,
} from "lucide-react"

import { ChatDisplay } from "@/app/chatbot/components/chat-display"
import { ChatList } from "@/app/chatbot/components/chat-list"
import { Chat } from "@/app/chatbot/data"
import { Separator } from "@/components/ui/separator"
import { Input } from "@/components/ui/input"
import {
  Tabs,
  TabsContent
} from "@/components/ui/tabs"
import { TooltipProvider } from "@/components/ui/tooltip"
import { Button } from "@/components/ui/button"
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable"

import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import { useChat } from "../use-chat"

interface ChatbotProps {
  chats: Chat[]
  defaultLayout: number[] | undefined
}

export function Chatbot({
  chats,
  defaultLayout = [30, 70],
}: ChatbotProps) {
  const [chat, setChat] = useChat()

  return (
    <>
      <TooltipProvider delayDuration={0}>
        <ResizablePanelGroup
          direction="horizontal"
          onLayout={(sizes: number[]) => {
            document.cookie = `react-resizable-panels:chat-layout=${JSON.stringify(
              sizes
            )}`
          }}
          className="items-stretch"
        >
          <ResizablePanel
            defaultSize={defaultLayout[0]}
            minSize={25}
            maxSize={40}
            className="flex flex-col"
          >
            <div className="flex items-center px-4 py-2">
              <h3 className="text-xl font-bold">Chat list</h3>
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button variant="info" className="ml-auto" size="icon">
                    <MessageSquarePlusIcon className="h-4 w-4" />
                    <span className="sr-only">New Chat</span>
                  </Button>
                </TooltipTrigger>
                <TooltipContent>New Chat</TooltipContent>
              </Tooltip>
            </div>
            <Separator />
            <div className="bg-background/95 p-4 backdrop-blur supports-[backdrop-filter]:bg-background/60">
              <div className="relative">
                <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
                <Input placeholder="Search" className="pl-8" />
              </div>
            </div>
            <ChatList items={chats} />
          </ResizablePanel>
          <ResizableHandle withHandle />
          <ResizablePanel
            defaultSize={defaultLayout[1]}
          >
            <ChatDisplay
              chat={chats.find((item) => item.id === chat.selected) || null}
              
            />
          </ResizablePanel>
        </ResizablePanelGroup>
      </TooltipProvider>
    </>
  )
}
