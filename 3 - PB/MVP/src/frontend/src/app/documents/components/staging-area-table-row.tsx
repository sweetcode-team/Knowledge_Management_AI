'use client'

import { forwardRef } from 'react'
import { TrashIcon } from 'lucide-react'

import { cn } from "@/lib/utils";
import { Button } from '@/components/ui/button'
import prettyBytes from 'pretty-bytes';

import { ALLOWED_FILE_TYPES } from '@/constants/constants'

interface StagingAreaTableRowProps extends React.HTMLAttributes<HTMLTableRowElement> {
    file: File
    deleteAction: (fileIds: string[]) => void
}

export const StagingAreaTableRow = forwardRef<HTMLTableRowElement, StagingAreaTableRowProps>(
    ({ file, className, deleteAction, ...props }, ref) => {
        return (
            <tr ref={ref} {...props} className={cn('', className)}>
                <td className="px-2 py-4 truncate whitespace-normal text-sm font-medium dark:text-slate-400 ">
                    <div className="">
                        <p
                            className='dark:text-slate-300'
                        >
                            {file.name}
                        </p>

                    </div>
                </td>
                <td
                    className='px-2 py-4 whitespace-nowrap text-sm dark:text-slate-400'
                >
                    {prettyBytes(file.size)}
                </td>
                <td
                    className='px-2 py-4 whitespace-nowrap text-sm dark:text-slate-400 truncate'
                >
                    {
                        ALLOWED_FILE_TYPES.find((allowedFileType) => allowedFileType.type === file.type)?.label
                    }
                </td>
                <td>
                    <Button
                        size="icon"
                        variant="ghost"
                        className="hover:text-error-foreground"
                        onClick={(e) => {
                            e.preventDefault()
                            deleteAction([file.name])
                        }}>
                        <TrashIcon className="h-4 w-4" />
                    </Button>
                </td>
            </tr>
        )
    }
)
StagingAreaTableRow.displayName = 'StagingAreaTableRow'