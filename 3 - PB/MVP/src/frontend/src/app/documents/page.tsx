import { promises as fs } from "fs"
import path from "path"
import { Metadata } from "next"
import { z } from "zod"

import { columns } from "./components/columns"
import { DataTable } from "./components/data-table"
import { documentSchema } from "./data/schema"
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"

export const metadata: Metadata = {
  title: "KMAI - Document Manager",
  description: "Document Manager for KMAI.",
}

async function getDocuments() {
  const data = await fs.readFile(
    path.join(process.cwd(), "src/app/documents/data/documents.json")
  )

  const documents = JSON.parse(data.toString())

  return z.array(documentSchema).parse(documents)
}

export default async function DocumentManagerPage() {
  const documents = await getDocuments()

  return (
    <ScrollArea className="h-full">
      <div className="h-full flex-1 flex-col space-y-2 p-4">
        <div className="flex items-center justify-between space-y-2">
          <h3 className="text-xl font-bold tracking-tight">List of documents</h3>
        </div>
        <DataTable data={documents} columns={columns} />
      </div>
    </ScrollArea>
  )
}
