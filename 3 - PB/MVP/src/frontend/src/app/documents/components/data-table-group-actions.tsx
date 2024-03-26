"use client"

import { Table } from "@tanstack/react-table"

import { Button } from "@/components/ui/button"

import * as React from "react"

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
import { TrashIcon } from "lucide-react"
import { LightDocument, DocumentOperationResponse } from "@/types/types";
import { concealDocuments, deleteDocuments, embedDocuments, enableDocuments } from "@/lib/actions"
import { toast } from "sonner";


interface DataTableGroupActionsProps<TData> {
  table: Table<TData>
}

export function DataTableGroupActions<TData>({
  table,
}: DataTableGroupActionsProps<TData>) {

  const handleAction = async () => {
    const toastId = toast.loading("Loading...", {
      description: "Updating document status.",
    })

    let results: DocumentOperationResponse[] = []
    if (selectedRowsStatuses.has("NOT_EMBEDDED")) {
      try {
        results = await embedDocuments(table.getSelectedRowModel().rows.map((row) => (row.original as LightDocument).id))
      } catch (e) {
        toast.error("Operation failed", {
          description: "Failed to embed the selected documents.",
          id: toastId
        })
      }
    } else if (selectedRowsStatuses.has("ENABLED")) {
      try {
        results = await concealDocuments(table.getSelectedRowModel().rows.map((row) => (row.original as LightDocument).id))
      } catch (e) {
        toast.error("Operation failed", {
          description: "Failed to disable the selected documents.",
          id: toastId
        })
      }
    } else if (selectedRowsStatuses.has("CONCEALED")) {
      try {
        results = await enableDocuments(table.getSelectedRowModel().rows.map((row) => (row.original as LightDocument).id))
      } catch (e) {
        toast.error("Operation failed", {
          description: "Failed to enable the selected documents.",
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
          description: result.id + " uploaded successfully",
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
      description: "Deleting documents.",
    })

    let results: DocumentOperationResponse[] = []
    try {
      results = await deleteDocuments(table.getSelectedRowModel().rows.map((row) => (row.original as LightDocument).id))
    } catch (e) {
      toast.error("Operation failed", {
        description: "Failed to delete the selected documents.",
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
          description: result.id + " uploaded successfully",
        })
      }
      else {
        toast.error("An error occurred for " + result.id, {
          description: "Please try again. " + result.message,
        })
        return
      }
    })
  }

  const selectedRowsStatuses = new Set((table.getSelectedRowModel().rows).map((row) => (row.original as LightDocument).status))

  const Icon = DOCUMENT_STATUSES.find((status) => selectedRowsStatuses.has(status.value))?.actionIcon as React.ComponentType<{ className?: string }>

  return (
    <>
      {
        (selectedRowsStatuses.size === 1 || (
          selectedRowsStatuses.size === 2 &&
          selectedRowsStatuses.has("not embedded") &&
          selectedRowsStatuses.has("inconsistent"))) ?
          (
            <AlertDialog>
              <AlertDialogTrigger asChild>
                <Button variant="default" size="sm" className="w-full justify-start px-4 py-[6px] h-8 space-x-2">
                  <Icon className="h-4 w-4" />
                  <div>
                    {DOCUMENT_STATUSES.find((status) => selectedRowsStatuses.has(status.value))?.action}
                  </div>
                </Button>
              </AlertDialogTrigger>
              <AlertDialogContent>
                <AlertDialogHeader>
                  <AlertDialogTitle>Are you sure?</AlertDialogTitle>
                  <AlertDialogDescription>
                    {DOCUMENT_STATUSES.find((status) => selectedRowsStatuses.has(status.value))?.groupActionMessage}
                  </AlertDialogDescription>
                </AlertDialogHeader>
                <AlertDialogFooter>
                  <AlertDialogCancel>Abort</AlertDialogCancel>
                  <AlertDialogAction className={
                    cn(buttonVariants(),
                      "mt-2 sm:mt-0")} onClick={() => handleAction()}>{DOCUMENT_STATUSES.find((status) => selectedRowsStatuses.has(status.value))?.action}</AlertDialogAction>
                </AlertDialogFooter>
              </AlertDialogContent>
            </AlertDialog>
          ) : null
      }
      <AlertDialog>
        <AlertDialogTrigger asChild>
          <Button disabled={
            table.getSelectedRowModel().rows.length === 0
          } variant="destructive" size="sm" className="h-8">
            <TrashIcon className="h-4 w-4" />
          </Button>
        </AlertDialogTrigger>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
            <AlertDialogDescription>
              This action cannot be undone. This will permanently delete the selected documents.
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
    </>
  )
}

