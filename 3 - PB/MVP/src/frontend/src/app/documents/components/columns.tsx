"use client"

import { parseISO, format } from "date-fns"
import prettyBytes from 'pretty-bytes';

import { ColumnDef } from "@tanstack/react-table"

import { StatusBadge } from "@/components/status-badge"
import { Checkbox } from "@/components/ui/checkbox"

import { types, statuses } from "@/app/documents/data/data"
import { DataTableColumnHeader } from "./data-table-column-header"
import { DataTableRowActions } from "./data-table-row-actions"
import { DocumentMetadata } from "@/types/types";

export const columns: ColumnDef<DocumentMetadata>[] = [
  {
    id: "select",
    header: ({ table }) => (
      <Checkbox
        checked={
          table.getIsAllPageRowsSelected() ||
          (table.getIsSomePageRowsSelected() && "indeterminate")
        }
        onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
        aria-label="Select all"
        className="translate-y-[2px]"
      />
    ),
    cell: ({ row }) => (
      <Checkbox
        checked={row.getIsSelected()}
        onCheckedChange={(value) => row.toggleSelected(!!value)}
        aria-label="Select row"
        className="translate-y-[2px]"
      />
    ),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: "id",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Title" />
    ),
    cell: ({ row }) => {
      return (
        <div className="flex space-x-2">
          <span className="max-w-[500px] truncate font-medium">
            {row.getValue("id")}
          </span>
        </div>
      )
    },
    enableSorting: true,
    enableHiding: false,
  },
  {
    accessorKey: "size",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="size" />
    ),
    cell: ({ row }) => {
      return (
        <div className="flex items-center justify-center">
          {prettyBytes(row.getValue("size"))}
        </div >
      )
    }
  },
  {
    accessorKey: "status",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Status" />
    ),
    cell: ({ row }) => {
      const status = statuses.find(
        (status) => status.value === row.getValue("status")
      )

      if (!status) {
        return null
      }

      return (
        <div className="flex items-center justify-center">
          <StatusBadge variant={status.style as any}>
            <span className="text-nowrap">{status?.label}</span>
          </StatusBadge>
        </div >
      )
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id))
    },
  },
  {
    accessorKey: "type",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Type" />
    ),
    cell: ({ row }) => {
      const type = types.find(
        (type) => type.value === row.getValue("type")
      )

      if (!type) {
        return null
      }

      return (
        <div className="flex items-center justify-center">
          {type.icon && (
            <type.icon className="mr-2 h-4 w-4 text-muted-foreground" />
          )}
          <span>{type.label}</span>
        </div>
      )
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id))
    },
  },
  {
    accessorKey: "uploadDate",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Upload Time" />
    ),
    cell: ({ row }) => {
      const date:Date = row.getValue("uploadDate");
      return (
        <div className="flex items-center justify-center">
          <span className="truncate font-medium">
            <time dateTime={row.getValue("uploadDate")}>{format(date, 'yyyy-MM-dd hh:mm')}</time>
          </span>
        </div>
      )
    },
  },
  {
    id: "actions",
    cell: ({ row }) => <DataTableRowActions row={row} />,
  },
]
