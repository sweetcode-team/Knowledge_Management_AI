import * as React from "react"
import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import { Separator } from "@/components/ui/separator"
import { Switch } from "@/components/ui/switch"
import { Textarea } from "@/components/ui/textarea"
import { Chat } from "@/app/chatbot/data"
import { ScrollArea } from '@/components/ui/scroll-area';
import { CardsChat } from "@/app/chatbot/components/chat"
import { ChatHeader } from "./chat-header"

interface ChatDisplayProps {
  chat: Chat | null
}

export function ChatDisplay({ chat }: ChatDisplayProps) {

  return (
    <div className="flex h-full flex-col">
      <ChatHeader chatTitle={chat?.name} isChatSelected={!!chat} />

      <Separator />
      {chat ? (
        <div className="h-full flex flex-1 flex-col justify-between overflow-auto">
          <div className="flex-1 whitespace-pre-wrap text-sm overflow-auto">
            <ScrollArea className="h-full">
              <div className="p-4">
                <CardsChat />
              </div>
            </ScrollArea>
          </div>
          <div>
            <Separator className="mt-auto" />
            <form className="p-4">
              <div className="grid gap-4 max-h-full">
                <div className="flex items-center">
                  <Label
                    htmlFor="mute"
                    className="flex items-center gap-2 text-xs font-normal"
                  >
                    <Switch id="mute" aria-label="Mute thread" /> Mute this
                    thread
                  </Label>
                  <Button
                    onClick={(e) => e.preventDefault()}
                    size="sm"
                    className="ml-auto"
                  >
                    Send
                  </Button>
                </div>
                <Textarea
                  className="p-4"
                  placeholder={`Reply ${chat.name}...`}
                />
              </div>
            </form>
          </div>
        </div>
      ) : (
        // TODO: schermata nuova chat
        <div className="p-12 text-center text-muted-foreground">
          No chat selected.
        </div>
      )}
    </div>
  )
}
