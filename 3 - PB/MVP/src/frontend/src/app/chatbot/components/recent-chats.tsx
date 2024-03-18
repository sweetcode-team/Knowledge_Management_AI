"use client"
import { formatDistanceToNow } from "date-fns";
import { useRouter } from 'next/navigation'; 
import { cn } from "@/lib/utils"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Chat } from "../data";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

import { Button } from "@/components/ui/button"

import { buttonVariants } from "@/components/ui/button"

import { DotsHorizontalIcon } from "@radix-ui/react-icons"

import {
  AlertDialog,
  AlertDialogTrigger,
  AlertDialogContent,
  AlertDialogHeader,
  AlertDialogFooter,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogAction,
  AlertDialogCancel,
} from "@/components/ui/alert-dialog"
import { useState } from "react";

interface RecentChatsProps {
  items: Chat[]
}

export function RecentChats({ items }: RecentChatsProps) {

  return ( 
    <ScrollArea>
      <div className="p-0 mb-2">
        <h3 className="ml-3 font-semibold">Recently visited chats</h3>
      </div>
      <div className="flex flex-col gap-2 p-4 pt-0">
        {items.map((item) => (
          <button
            key={item.id}
            className={cn(
              "flex flex-col items-start gap-2 rounded-lg border p-3 text-left text-sm transition-all hover:bg-accent",
            )}
          >
            <div className="flex w-full flex-col gap-1">
              <div className="flex items-center gap-x-2">
                <div className="flex items-center gap-x-2">
                  {!item.read && (
                    <span className="flex h-2 w-2 rounded-full bg-blue-600" />
                  )}
                  <div className="font-semibold line-clamp-1">{item.name}</div>
                </div>
                <div
                  className={cn("ml-auto text-xs line-clamp-1")}
                >
                  {formatDistanceToNow(new Date(item.date), {
                    addSuffix: true,
                  })}
                </div>
                 <DropdownMenu>
                  <DropdownMenuTrigger asChild>

                  {/* TODO: FIX DELETE CHAT BUTTON */}
                  
                 {/* <Button
                    variant="ghost"
                    className={`flex h-8 w-8 p-0`}
                  >
                    <DotsHorizontalIcon className="h-4 w-4" />
                    <span className="sr-only">Open menu</span>
                  </Button>  */}

                  </DropdownMenuTrigger>
                  <DropdownMenuContent align="end" className="w-[160px]">
                    <AlertDialog>
                      <AlertDialogTrigger asChild>
                        <Button variant="ghost" size="sm" className="text-error-foreground hover:bg-error hover:text-error-foreground w-full justify-start px-2 py-[6px] h-8"
                        >
                          Delete
                        </Button> 
                      </AlertDialogTrigger>
                      <AlertDialogContent>
                        <AlertDialogHeader>
                          <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                          <AlertDialogDescription>
                            This action cannot be undone. This will permanently delete the selected chat.
                          </AlertDialogDescription>
                        </AlertDialogHeader>
                        <AlertDialogFooter>
                        <AlertDialogCancel>Abort</AlertDialogCancel>
                          <AlertDialogAction className={
                            cn(buttonVariants({ variant: "destructive" }),
                              "mt-2 sm:mt-0")} >Delete</AlertDialogAction>
                        </AlertDialogFooter>
                      </AlertDialogContent>
                    </AlertDialog>
                  </DropdownMenuContent>
                </DropdownMenu>
              </div>
             </div>
            <div className="line-clamp-2 text-xs text-muted-foreground">
              {item.text.substring(0, 300)}
            </div>
          </button>
        ))}        
      </div>   
    </ScrollArea>
  )
}