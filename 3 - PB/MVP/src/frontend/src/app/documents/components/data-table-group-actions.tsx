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

import { statuses } from "../data/data"
import { TrashIcon } from "lucide-react"
import {DocumentMetadata, DocumentOperationResponse} from "@/types/types";
import {revalidatePath} from "next/cache";


interface DataTableGroupActionsProps<TData> {
  table: Table<TData>
}
export async function embeddDocument(ids : string[] = []): Promise<DocumentOperationResponse[]> {

  const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

  const result = await fetch(`http://localhost:4000/embedDocuments`,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: formData.toString()
  });
  return result.json()
}
export async function concealDocument(ids : string[] = []): Promise<DocumentOperationResponse[]> {

  const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

  const result = await fetch(`http://localhost:4000/concealDocuments`,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: formData.toString()
  });
  return result.json()
}
export async function deleteDocument(ids: string[]): Promise<DocumentOperationResponse> {
  const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`http://localhost:4000/deleteDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
        }
    )
    return result.json()
}
export async function enableDocument(ids : string[] = []): Promise<DocumentOperationResponse[]> {
  const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

  const result = await fetch(`http://localhost:4000/enableDocuments`,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: formData.toString()
  });
  return result.json()
}

export function DataTableGroupActions<TData>({
  table,
}: DataTableGroupActionsProps<TData>) {

  const handleAction = () => {
    console.log(selectedRowsStatuses)
    if (selectedRowsStatuses.has("NOT_EMBEDDED")) {
        const result = embeddDocument(table.getSelectedRowModel().rows.map((row) => (row.original as DocumentMetadata).id))
        result.then((res) => console.log(res))
    }else if(selectedRowsStatuses.has("ENABLED")){
        const result = concealDocument(table.getSelectedRowModel().rows.map((row) => (row.original as DocumentMetadata).id))
        result.then((res) => console.log(res))
    }else if(selectedRowsStatuses.has("CONCEALED")){
      const result = enableDocument(table.getSelectedRowModel().rows.map((row) => (row.original as DocumentMetadata).id))
        result.then((res) => console.log(res))
    }
  }

  const handleDelete = () => {
    const result = deleteDocument(table.getSelectedRowModel().rows.map((row) => (row.original as DocumentMetadata).id))
    result.then((res) => console.log(res))
    }

  const selectedRowsStatuses = new Set((table.getSelectedRowModel().rows).map((row) => (row.original as DocumentMetadata).status))

  const Icon = statuses.find((status) => selectedRowsStatuses.has(status.value))?.actionIcon as React.ComponentType<{ className?: string }>

  return (
    <>{
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
                  {statuses.find((status) => selectedRowsStatuses.has(status.value))?.action}
                </div>
              </Button>
            </AlertDialogTrigger>
            <AlertDialogContent>
              <AlertDialogHeader>
                <AlertDialogTitle>Are you sure?</AlertDialogTitle>
                <AlertDialogDescription>
                  {statuses.find((status) => selectedRowsStatuses.has(status.value))?.groupActionMessage}
                </AlertDialogDescription>
              </AlertDialogHeader>
              <AlertDialogFooter>
                <AlertDialogCancel>Abort</AlertDialogCancel>
                <AlertDialogAction className={
                  cn(buttonVariants(),
                    "mt-2 sm:mt-0")} onClick={() => handleAction()}>{statuses.find((status) => selectedRowsStatuses.has(status.value))?.action}</AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        ) : null
    }
      <AlertDialog>
        <AlertDialogTrigger asChild>
          <Button disabled={!table.getIsSomeRowsSelected()} variant="destructive" size="sm" className="h-8">
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

