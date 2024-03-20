"use client";
import { formatDate, formatDistanceToNow } from "date-fns";
import { cn } from "@/lib/utils"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Chat } from "../app/chatbot/data";
import { Button } from "@/components/ui/button"
import { buttonVariants } from "@/components/ui/button"
import {
  ContextMenu,
  ContextMenuContent,
  ContextMenuTrigger,
} from "@/components/ui/context-menu"

import { types, statuses } from "@/app/documents/data/data"
import { Document } from "@/app/documents/data/schema"

import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"

import {
  Table,
  TableBody,
  TableCell,
  TableRow,
} from "@/components/ui/table"

import Link from "next/link";
import prettyBytes from "pretty-bytes";
import { StatusBadge } from "./status-badge";

interface RecentDocumentsProps {
  items: Document[]
}

export function RecentDocuments({
  items,
}: RecentDocumentsProps) {

  return (
    <ScrollArea>
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2 m-2">
        {items.map((item) => (
          <Drawer key={item.id}>
            <DrawerTrigger asChild>
              <div
                className={cn(
                  "flex flex-col items-start gap-1 rounded-lg border p-3 text-left text-sm transition-all hover:bg-accent w-full",
                )}
              >
                <div className="font-semibold line-clamp-1">{item.id}</div>
                <div className="flex flex-col md:flex-row w-full items-center justify-between gap-2">
                  {/* <StatusBadge variant={item.status as any} /> */}
                  <div className="text-xs line-clamp-1">{prettyBytes(item.dimension)} | {item.type.toUpperCase()}</div>
                  {
                    item.status &&
                    <StatusBadge
                      className="truncate"
                      variant={statuses.find(
                        (status) => status.value === item.status
                      )?.style as any}>
                      <span className="truncate">{item.status}</span>
                    </StatusBadge>
                  }
                  {/* <ArrowRightIcon className="h-4 w-4 text-blue-600 ml-auto " /> */}
                </div>
              </div>
            </DrawerTrigger>
            <DrawerContent className="max-h-screen">
              <div className="mx-auto w-full sm:w-6/12 xl:w-4/12 max-h-screen overflow-auto">
                <DrawerHeader className="pb-0">
                  <DrawerTitle>{item.id}</DrawerTitle>
                  <DrawerDescription>Document details.</DrawerDescription>
                </DrawerHeader>
                <div className="px-4 pb-0 xl:py-4 w-full">
                  <Table className="mt-3">
                    <TableBody>
                      <TableRow>
                        <TableCell className="font-bold">Type</TableCell>
                        <TableCell>{item.type}</TableCell>
                      </TableRow>
                      <TableRow>
                        <TableCell className="font-bold">Dimension</TableCell>
                        <TableCell>{prettyBytes(item.dimension)}</TableCell>
                      </TableRow>
                      <TableRow>
                        <TableCell className="font-bold">Upload time</TableCell>
                        <TableCell>
                          {
                            formatDate(item.uploadTime, "dd MMM yyyy HH:mm")
                          }
                        </TableCell>
                      </TableRow>
                      <TableRow>
                        <TableCell className="font-bold">Status</TableCell>
                        <TableCell>
                          {
                            item.status &&
                            <StatusBadge
                              variant={statuses.find(
                                (status) => status.value === item.status
                              )?.style as any}>
                              <span className="truncate">{item.status}</span>
                            </StatusBadge>
                          }
                        </TableCell>
                      </TableRow>
                    </TableBody>
                  </Table>
                </div>
                <DrawerFooter>
                  <Button asChild>
                    <Link href={`/documents/${item.id}`}>
                      View content
                    </Link>
                  </Button>
                  <DrawerClose asChild>
                    <Button variant="outline">Close</Button>
                  </DrawerClose>
                </DrawerFooter>
              </div>
            </DrawerContent>
          </Drawer>
          /* <AlertDialog>
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
      </AlertDialog> */
        ))}
      </div>
    </ScrollArea >
  )
}