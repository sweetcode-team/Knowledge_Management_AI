"use client"
import { formatDistanceToNow } from "date-fns";

import { cn } from "@/lib/utils"
import { ScrollArea } from "@/components/ui/scroll-area"

import { useChat } from "../use-chat";
import { ChatPreview } from "@/types/types";
import { CopyXIcon, ListTodoIcon, Search, Undo2Icon } from "lucide-react";
import { Input } from "@/components/ui/input";
import { useState, useCallback } from 'react';
import { Checkbox } from "@/components/ui/checkbox";
import { Button, buttonVariants } from "@/components/ui/button";
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger } from "@/components/ui/alert-dialog";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import {deleteChats} from "@/lib/actions";
import {toast} from "sonner";

interface ChatListProps {
  items: ChatPreview[]
}

export function ChatList({ items }: ChatListProps) {
  const [chat, setChat] = useChat()
  const [filteredChats, setFilteredChats] = useState(items)

  const [isBeingSelected, setIsBeingSelected] = useState(false)
  const [selectedChats, setSelectedChats] = useState<number[]>([])

  const handleDelete = async () => {
  try {
    const result = await deleteChats(selectedChats);
    if (result.status) {
      toast("Chats deleted successfully");
    }
  } catch (error) {
    console.error("An error occurred while deleting chats:", error);
    toast("An error occurred while deleting chats");
  }
  setIsBeingSelected(false);
  setSelectedChats([]);
}


  return (
    <div>
      <div
        className="flex w-full space-x-2 bg-background/95 p-4 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="relative w-full">
          <Search
            className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground"
          />
          <Input
            placeholder="Search"
            className="pl-8"
            onChange={(e) => {
              setFilteredChats(items.filter((item) => item.title.toLowerCase().includes(e.target.value.toLowerCase())))
            }}
          />
        </div>
          {
            isBeingSelected ?
              <div className="flex space-x-2">
                <Tooltip>
                  <TooltipTrigger asChild>
                    <Button
                      variant="secondary"
                      size="icon"
                      onClick={() => {
                        setIsBeingSelected(false)
                        setSelectedChats([])
                      }}
                    >
                      <Undo2Icon className="h-4 w-4 min-w-[40px]" />
                    </Button>
                  </TooltipTrigger>
                  <TooltipContent className="">Abort</TooltipContent>
                </Tooltip>
                <AlertDialog>
                  <AlertDialogTrigger asChild>
                    <Button disabled={selectedChats.length === 0} variant="destructive" size="icon" className="min-w-[40px]">
                      <CopyXIcon className="h-4 w-4" />
                    </Button>
                  </AlertDialogTrigger>
                  <AlertDialogContent>
                    <AlertDialogHeader>
                      <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                      <AlertDialogDescription>
                        This action cannot be undone. This will permanently delete the selected chats.
                      </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                      <AlertDialogCancel id="dialog-cancel">Abort</AlertDialogCancel>
                      <AlertDialogAction id="dialog-action"
                        className={cn(buttonVariants({ variant: "destructive" }), "mt-2 sm:mt-0")}
                        onClick={() => handleDelete()}
                      >Delete
                      </AlertDialogAction>
                    </AlertDialogFooter>
                  </AlertDialogContent>
                </AlertDialog>
              </div>
              :
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    variant={isBeingSelected ? "destructive" : "outline"}
                    size="icon"
                    onClick={() => setIsBeingSelected(true)}
                  >
                    <ListTodoIcon className="h-4 w-4 min-w-[40px]" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent className="">Select chats</TooltipContent>
              </Tooltip>
          }
        </div>
      <ScrollArea className="h-full">
        <div className="flex flex-col space-y-2 p-4 pt-0">
          {
            filteredChats.length !== 0 ?
              filteredChats.map((item) => (
                <div
                  tabIndex={0}
                  key={item.chatId}
                  className={cn(
                    "flex flex-col items-start gap-2 rounded-lg border p-3 text-left text-sm transition-all hover:bg-accent",
                    chat.selected === item.chatId && "bg-muted"
                  )}
                  onClick={() =>
                    setChat({
                      ...chat,
                      selected: item.chatId,
                    })
                  }
                >
                  <div className="flex w-full flex-col gap-1">
                    <div className="flex items-center gap-x-2">
                      <div className="flex items-center gap-x-2">
                        {
                          isBeingSelected &&
                          <Checkbox onClick={
                            (e) => {
                              e.stopPropagation()
                              setSelectedChats((prev) => {
                                if (prev.includes(item.chatId)) {
                                  return prev.filter((id) => id !== item.chatId)
                                } else {
                                  return [...prev, item.chatId]
                                }
                              })
                            }
                          } />
                        }
                        <div className="font-semibold line-clamp-1">{item.title}</div>
                      </div>
                      <div
                        className={cn(
                          "ml-auto text-xs line-clamp-1",
                          chat.selected === item.chatId
                            ? "text-foreground"
                            : "text-muted-foreground"
                        )}
                      >
                        {formatDistanceToNow(new Date(item.lastMessage.timestamp), {
                          addSuffix: true,
                        })}
                      </div>
                    </div>
                  </div>
                  <div className="line-clamp-2 text-xs text-muted-foreground">
                    {item.lastMessage.content.substring(0, 300)}
                  </div>
                </div>
              ))
              :
              <div className="text-center text-muted-foreground">
                No chat selected.
              </div>
          }
        </div>
      </ScrollArea>
    </div>
  )
}