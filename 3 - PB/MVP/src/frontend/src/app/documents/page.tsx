import { Metadata } from "next"

import { columns } from "./components/columns"
import { DataTable } from "./components/data-table"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"
import { StagingArea } from "./components/staging-area"
import { getDocuments } from "@/lib/actions"

export const metadata: Metadata = {
  title: "KMAI - Document Manager",
  description: "Document Manager for KMAI.",
}

export default async function DocumentManagerPage() {
  const documents = await getDocuments()

  return (
    <ScrollArea className="h-full">
      <div className="h-full flex-1 flex-col space-y-4 p-4">
        <h3 className="text-xl font-bold tracking-tight">Staging area</h3>
        <StagingArea
          documentIds={documents.map((document) => document.id)}
        />
        <Separator />
        <h3 className="text-xl font-bold tracking-tight">List of documents</h3>
        <DataTable data={documents} columns={columns} />
      </div>
    </ScrollArea>
  )
}
