"use client";
import { formatDistanceToNow } from "date-fns";
import { cn } from "@/lib/utils"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Chat } from "../data";
import { Button } from "@/components/ui/button"
import { buttonVariants } from "@/components/ui/button"
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"

import { types, statuses } from "@/app/documents/data/data"
import { Document } from "@/app/documents/data/schema"

import { ArrowRightIcon, File } from "lucide-react"

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

interface RecentDocumentsProps{
  items: Document[]
}

export function RecentDocuments({
  items,
  }: RecentDocumentsProps) {

    const hideContextMenu = (id: string) => {
      document.getElementById(id)!.style.display = "none";
    }

  function deleteDocument(id: string) {
    console.log('Document deleted:', id);
  }

  return ( 
    <ScrollArea>
         <div className="grid grid-cols-3 gap-2 p-4 pt-0 justify-stretch"> 
              {items.map((item) => (
                <ContextMenu>
                <ContextMenuTrigger> 
                <button
                  key={item.id }
                  className={cn(
                    "flex flex-growth items-start gap-2 rounded-lg border p-3 text-left text-sm transition-all hover:bg-accent w-full",
                  )}
                >                
                <div className="flex w-full flex-col gap-1">
                  <div className="flex items-center gap-x-2">
                    <File className="align-middle w-7 h-7" />
                    <div className="flex flex-col justify-between ml-2">
                      <div className="font-semibold line-clamp-1">{item.id}</div>
                      <div className="text-xs line-clamp-1">{item.dimension}KB | .{item.type} | {item.status}</div>
                    </div>
                    <ArrowRightIcon className="h-4 w-4 text-blue-600 ml-auto " />
                  </div>
                </div>
                </button>  
                </ContextMenuTrigger> 
                <ContextMenuContent id={item.id}> 
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
                          This action cannot be undone. This will permanently delete the selected document.
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                      <AlertDialogCancel
                      onClick={() => hideContextMenu(item.id)}
                        >
                        Abort</AlertDialogCancel>
                        <AlertDialogAction className={
                          cn(buttonVariants({ variant: "destructive" }),
                            "mt-2 sm:mt-0")}
                              onClick={() => {
                                hideContextMenu(item.id)
                                deleteDocument(item.id)                              
                              }}
                            >Delete</AlertDialogAction>
                    </AlertDialogFooter>
                  </AlertDialogContent> 
                  </AlertDialog>
                </ContextMenuContent> 
                </ContextMenu>          
              ))}  
          </div>   
    </ScrollArea>
  )
}