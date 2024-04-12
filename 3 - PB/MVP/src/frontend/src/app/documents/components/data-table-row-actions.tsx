"use client"

import { DotsHorizontalIcon } from "@radix-ui/react-icons"
import { Row } from "@tanstack/react-table"

import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

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

import { DOCUMENT_STATUSES } from "@/constants/constants"

import {
  concealDocuments,
  deleteDocuments,
  embedDocuments,
  enableDocuments
} from "@/lib/actions";
import { LightDocument, DocumentOperationResponse } from "@/types/types";
import { toast } from 'sonner';
import Link from "next/link";

interface DataTableRowActionsProps<TData> {
  row: Row<TData>
}

export function DataTableRowActions<TData>({
  row,
}: DataTableRowActionsProps<TData>) {
  const document = row.original as LightDocument

  const handleAction = async () => {
    const toastId = toast.loading("Loading...", {
      description: "Updating document status.",
    })

    let results: DocumentOperationResponse[] = []
    if (document.status == "NOT_EMBEDDED") {
      try {
        results = await embedDocuments([document.id])
      } catch (e) {
        toast.error("Operation failed", {
          description: "Failed to embed the selected document.",
          id: toastId
        })
      }
    } else if (document.status == "ENABLED") {
      try {
        results = await concealDocuments([document.id])
      } catch (e) {
        toast.error("Operation failed", {
          description: "Failed to disable the selected document.",
          id: toastId
        })
      }
    } else if (document.status == "CONCEALED") {
      try {
        results = await enableDocuments([document.id])
      } catch (e) {
        toast.error("Operation failed", {
          description: "Failed to enable the selected document.",
          id: toastId
        })
      }
    }
    toast.dismiss(toastId)

    results.forEach((result) => {
      if (!result) {
        toast.error("An error occurred", {
          description: "Please try again later.",
        })
        return
      }
      else if (result.status) {
        toast.success("Operation successful", {
          description: result.id + " status modified successfully.",
        })
      }
      else {
        toast.error("An error occurred for " + result.id, {
          description: "Please try again. " + result.message,
        })
      }
    })
  }

  const handleDelete = async () => {
    const toastId = toast.loading("Loading...", {
      description: "Deleting the selected document.",
    })

    let results: DocumentOperationResponse[] = []
    try {
      results = await deleteDocuments([document.id])
    } catch (e) {
      toast.error("Operation failed", {
        description: "Failed to delete the selected document.",
        id: toastId
      })
    }

    toast.dismiss(toastId)

    results.forEach((result) => {
      if (!result) {
        toast.error("An error occurred", {
          description: "Please try again later.",
        })
        return
      }
      else if (result.status) {
        toast.success("Operation successful", {
          description: result.id + " deleted successfully.",
        })
      }
      else {
        toast.error("An error occurred for " + result.id, {
          description: "Please try again. " + result.message,
        })
      }
    })
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button
          variant="ghost"
          className="flex h-8 w-8 p-0 data-[state=open]:bg-muted"
        >
          <DotsHorizontalIcon className="h-4 w-4" />
          <span className="sr-only">Open menu</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-[160px]">
        <DropdownMenuItem>
          <Link
            href={`/documents/${document.id}`}
            className="w-full"
          >
            View details
          </Link>
        </DropdownMenuItem>
        <AlertDialog>
          <AlertDialogTrigger asChild>
            <Button variant="ghost" size="sm" className="w-full justify-start px-2 py-[6px] h-8">
              {
                DOCUMENT_STATUSES.find((status) => status.value === document.status)?.action
              }
            </Button>
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>Are you sure?</AlertDialogTitle>
              <AlertDialogDescription>
                {
                  DOCUMENT_STATUSES.find((status) => status.value === document.status)?.actionMessage
                }
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Abort</AlertDialogCancel>
              <AlertDialogAction className={
                cn(buttonVariants(),
                  "mt-2 sm:mt-0")} onClick={() => handleAction()}>
                {DOCUMENT_STATUSES.find((status) => status.value === document.status)?.action}
              </AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>
        <DropdownMenuSeparator />
        <AlertDialog>
          <AlertDialogTrigger asChild>
            <Button variant="ghost" size="sm" className="text-error-foreground hover:bg-error hover:text-error-foreground w-full justify-start px-2 py-[6px] h-8">Delete</Button>
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
              <AlertDialogDescription>
                This action cannot be undone. This will permanently delete the selected document.
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Abort</AlertDialogCancel>
              <AlertDialogAction className={
                cn(buttonVariants({ variant: "destructive" }),
                  "mt-2 sm:mt-0")} onClick={() => handleDelete()}>Delete</AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>

      </DropdownMenuContent>
    </DropdownMenu>
  )
}

