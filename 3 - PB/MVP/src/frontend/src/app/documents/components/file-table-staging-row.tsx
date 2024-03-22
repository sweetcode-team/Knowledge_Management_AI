'use client'

import { forwardRef } from 'react'
import { TrashIcon } from 'lucide-react'

import { cn } from "@/lib/utils";
import { Button } from '@/components/ui/button'

interface FileUploadProps extends React.HTMLAttributes<HTMLTableRowElement> {
    name: string
    size: number
    getUrl: string
    type: string
    error?: boolean | undefined
    deleteAction: () => void
}

export const FileUpload = forwardRef<HTMLTableRowElement, FileUploadProps>(
    ({ getUrl, error, type, name, size, className, deleteAction, ...props }, ref) => {


        return (
            <tr ref={ref} {...props} className={cn('', className)}>
                <td className="px-6 py-4 truncate whitespace-normal text-sm font-medium dark:text-slate-400 ">
                    <div className="">
                        <p
                            className={cn('dark:text-slate-300', {
                                'dark:text-red-500': error,
                            })}
                        >
                            {name}
                        </p>

                    </div>
                </td>
                <td
                    className={cn(
                        'px-6 py-4 whitespace-nowrap text-sm dark:text-slate-400',
                        {
                            'dark:text-red-500': error,
                        }
                    )}
                >
                    {(size / 1000).toFixed(0)} KB
                </td>
                <td
                    className={cn(
                        'px-6 py-4 whitespace-nowrap text-sm dark:text-slate-400',
                        {
                            'dark:text-red-500': error,
                        }
                    )}
                >
                    {type.toUpperCase()}
                </td>
                <td>
                    <Button
                        size="icon"
                        variant="ghost"
                        className="hover:text-error-foreground"
                        onClick={() => {
                            deleteAction()
                        }}>
                        <TrashIcon className="h-4 w-4" />
                    </Button>
                </td>
            </tr>
        )
    }
)
FileUpload.displayName = 'FileUpload'