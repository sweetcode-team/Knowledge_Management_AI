import { promises as fs } from "fs"
import path from "path"
import { Metadata } from "next"
import { z } from "zod"

import { columns } from "./components/columns"
import { DataTable } from "./components/data-table"
import { documentSchema } from "./data/schema"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"
import { StagingArea } from "./components/staging-area"
import {DocumentContent, DocumentMetadata, DocumentOperationResponse} from "@/types/types";
import {headers} from "next/headers";

export const metadata: Metadata = {
  title: "KMAI - Document Manager",
  description: "Document Manager for KMAI.",
}
export async function getDocuments(id : string = ""): Promise<DocumentMetadata[]> {
  if (id === "") {
    const result = await fetch(`http://localhost:4000/getDocuments`, {cache : 'no-store'});
    return result.json()
  }else {
    const result = await fetch(`http://localhost:4000/getDocuments/${id}`);
    return result.json()
  }
}


export default async function DocumentManagerPage() {
  const documents = await getDocuments()
  return (
    <ScrollArea className="h-full">
      <div className="h-full flex-1 flex-col space-y-4 p-4">
        <h3 className="text-xl font-bold tracking-tight">Staging area</h3>
        <StagingArea />
        <Separator />
        <h3 className="text-xl font-bold tracking-tight">Lista dei documenti</h3>
        <DataTable data={documents} columns={columns} />
      </div>
    </ScrollArea>
  )
}
