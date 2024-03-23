import { formatDistanceToNow } from "date-fns";

import { cn } from "@/lib/utils"
import { ScrollArea } from "@/components/ui/scroll-area"

import { ChatPreview } from "@/types/types";
import { CopyXIcon, ListTodoIcon, Search, Undo2Icon } from "lucide-react";
import { Input } from "@/components/ui/input";
import { useState, useCallback } from 'react';
import { Checkbox } from "@/components/ui/checkbox";
import { Button, buttonVariants } from "@/components/ui/button";
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger } from "@/components/ui/alert-dialog";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { deleteChats } from "@/lib/actions";
import { toast } from "sonner";

import { useRouter, useParams } from "next/navigation";

interface ChatItemProps {
  chat: ChatPreview
  isBeingSelected: boolean
}

export function ChatItem({ chat, isBeingSelected }: ChatItemProps) {
  const pathChatId = +useParams().chatId

  const router = useRouter()

  return (
    <div
      tabIndex={0}
      key={chat.id}
      className={cn(
        "flex flex-col items-start gap-2 rounded-lg border p-3 text-left text-sm transition-all hover:bg-accent",
        pathChatId == chat.id && "bg-muted"
      )}
      onClick={(e) => {
        e.preventDefault()
        if (!isBeingSelected) {
          router.push(`/chatbot/${chat.id}`)
        }
      }}
    >
      <>
        <div className="flex w-full flex-col gap-1">
          <div className="flex items-center gap-x-2">
            <div className="flex items-center gap-x-2">
              {
                isBeingSelected &&
                <Checkbox onClick={
                  (e) => {
                    e.stopPropagation()
                    // TODO: form field to select chat for form in chat list
                  }
                } />
              }
              <div className="font-semibold line-clamp-1">{chat.title}</div>
            </div>
            <div
              className={cn(
                "ml-auto text-xs line-clamp-1",
                pathChatId === chat.id
                  ? "text-foreground"
                  : "text-muted-foreground"
              )}
            >
              {formatDistanceToNow(new Date(chat.lastMessage.timestamp), {
                addSuffix: true,
              })}
            </div>
          </div>
        </div>
        <div className="line-clamp-2 text-xs text-muted-foreground">
          {chat.lastMessage.content.substring(0, 300)}
        </div>
      </>
    </div>
  )
}