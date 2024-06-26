"use client"

import {
    useReducer,
    useState,
    type ChangeEvent,
    type DragEvent,
} from 'react'
import { StagingAreaTableRow } from './staging-area-table-row'
import { MAX_FILE_SIZE } from '@/constants/constants'
import { toast } from "sonner"
import { cn, validateFileType } from "@/lib/utils";
import { Button } from '@/components/ui/button'
import { CircleSlashIcon, FolderUpIcon } from 'lucide-react'
import { ScrollArea, ScrollBar } from '@/components/ui/scroll-area'
import prettyBytes from 'pretty-bytes'

import { uploadDocuments } from '@/lib/actions'
import { Checkbox } from '@/components/ui/checkbox'
import {
    AlertDialog,
    AlertDialogContent,
    AlertDialogHeader,
    AlertDialogDescription,
    AlertDialogAction,
    AlertDialogTitle,
    AlertDialogCancel,
    AlertDialogFooter

} from '@/components/ui/alert-dialog'

const addFilesToInput = () => ({
    type: 'ADD_FILES_TO_INPUT' as const,
    payload: [] as File[],
})

const removeFilesFromInput = (name: string[]) => ({
    type: 'REMOVE_FILES_FROM_INPUT' as const,
    payload: name,
})

const removeAllFilesFromInput = () => ({
    type: 'REMOVE_ALL_FILES_FROM_INPUT' as const,
})

type ActionAdd = ReturnType<typeof addFilesToInput>
type ActionRemove = ReturnType<typeof removeFilesFromInput>
type ActionRemoveAll = ReturnType<typeof removeAllFilesFromInput>
type Action = ActionAdd | ActionRemove | ActionRemoveAll
type State = File[]

const filesAlreadyPresent = (files: FileList, stagingFiles: File[]): File[] => {
    const filesNotOk = []
    for (let i = 0; i < files.length; i++) {
        for (let j = 0; j < stagingFiles.length; j++) {
            if (files[i].name === stagingFiles[j].name)
                filesNotOk.push(files[i])
        }
    }
    return filesNotOk
}

const removeAlreadyPresentFiles = (files: FileList, stagingFiles: File[]): File[] => {
    const updatedFilesArray: File[] = Array.from(files);
    return updatedFilesArray.filter(file => !stagingFiles.some(stagingFile => stagingFile.name === file.name));
}

interface StagingAreaProps {
    documentIds: string[]
}

export function StagingArea({ documentIds }: StagingAreaProps) {
    const [dragActive, setDragActive] = useState<boolean>(false)
    const [input, dispatch] = useReducer((state: State, action: Action) => {
        switch (action.type) {
            case 'ADD_FILES_TO_INPUT': {
                return [...state, ...action.payload]
            }
            case 'REMOVE_FILES_FROM_INPUT': {
                return state.filter((file) => !action.payload.includes(file.name))
            }
            case 'REMOVE_ALL_FILES_FROM_INPUT': {
                return []
            }
        }
    }, [])
    const noInput = input.length === 0

    const [substituteDialogOpen, setSubstituteDialogOpen] = useState(false)
    const [duplicatedDocumentIds, setDuplicatedDocumentIds] = useState<Set<string>>(new Set())
    const [ignoreDocumentIds, setIgnoreDocumentIds] = useState<string[]>([])

    const toggleIgnoredDocument = (documentId: string) => {
        setIgnoreDocumentIds((prevState) => {
            if (prevState.includes(documentId)) {
                return prevState.filter((id) => id !== documentId);
            } else {
                return [...prevState, documentId];
            }
        })
    }

    const normalizeFilename = (filename: string) => {
        return filename.replace(/[^\w.-]/g, '_').toLowerCase();
    }

    const onPreSubmit = () => {
        let isDuplicated = false
        const normalizedDocumentIds = documentIds.map(normalizeFilename)

        input.forEach((file) => {
            const normalizedFilename = normalizeFilename(file.name)
            if (normalizedDocumentIds.includes(normalizedFilename)) {
                isDuplicated = true
                setDuplicatedDocumentIds((prevState) => new Set(prevState.add(file.name)))
            }
        })

        if (isDuplicated) setSubstituteDialogOpen(true)
        else onSubmit()
    }

    const onSubmit = async () => {
        setSubstituteDialogOpen(false)
        setDuplicatedDocumentIds(new Set())
        setIgnoreDocumentIds([])

        const formData = new FormData()
        input.forEach((file) => {
            formData.append('documents', file)
        })

        const toastId = toast.loading("Loading...", {
            description: "Uploading your documents.",
        })
        removeAllFilesFromState()
        const results = await uploadDocuments(formData, true)

        toast.dismiss(toastId)

        if (!results || !Array.isArray(results)) {
            toast.error("An error occurred", {
                description: "Please try again. " + results,
            })
            return
        }
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



    // handle drag events
    const handleDrag = (e: DragEvent<HTMLFormElement | HTMLDivElement>) => {
        e.preventDefault()
        e.stopPropagation()
        if (e.type === 'dragenter' || e.type === 'dragover') {
            setDragActive(true)
        } else if (e.type === 'dragleave') {
            setDragActive(false)
        }
    }

    // triggers when file is selected with click
    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        e.preventDefault()
        try {
            if (e.target.files && e.target.files[0]) {
                const files = Array.from(e.target.files)
                const validFiles = files.filter((file) => validateFileType(file))

                if (!validFiles) {
                    toast.error("Invalid file type", {
                        description: "Please upload a valid file type.",
                    })
                    return
                }

                if (filesAlreadyPresent(e.target.files, input).length > 0) {
                    toast.info("File already present", {
                        description: "Please upload a different file.",
                    })
                }
                const validFilesWithoutAlreadyPresent = removeAlreadyPresentFiles(e.target.files, input);

                addFilesToState(validFilesWithoutAlreadyPresent)
            }
        } catch (error) {
            toast.error("An error occurred", {
                description: "Please try again.",
            })
        }
    }

    const addFilesToState = (files: File[]) => {
        dispatch({ type: 'ADD_FILES_TO_INPUT', payload: files })
    }

    const removeFilesFromState = (fileIds: string[]) => {
        fileIds.forEach((fileId) => {
            dispatch({ type: 'REMOVE_FILES_FROM_INPUT', payload: [fileId] })
        })
    }

    const removeAllFilesFromState = () => {
        dispatch({ type: 'REMOVE_ALL_FILES_FROM_INPUT' })
    }

    // triggers when file is selected with drag and drop
    const handleDrop = (e: DragEvent<HTMLDivElement>) => {
        e.preventDefault()
        e.stopPropagation()
        try {
            if (e.dataTransfer.files && e.dataTransfer.files[0]) {
                const files = Array.from(e.dataTransfer.files)
                const validFiles = files.filter((file) => validateFileType(file))

                if (files.length !== validFiles.length) {
                    toast.error("Invalid file type", {
                        description: 'Please upload a valid file type.',
                    })
                    return
                }

                if (!validFiles) {
                    toast.error("Invalid file type", {
                        description: 'Please upload a valid file type.',
                    })
                    return
                }

                if (filesAlreadyPresent(e.dataTransfer.files, input).length > 0) {
                    toast.info("File already present", {
                        description: 'Please upload a different file.',
                    })
                }
                const validFilesWithoutAlreadyPresent = removeAlreadyPresentFiles(e.dataTransfer.files, input)

                setDragActive(false)
                addFilesToState(validFilesWithoutAlreadyPresent)
                e.dataTransfer.clearData()
            }
        } catch (error) {
            toast.error("An error occurred", {
                description: 'Please try again.',
            })
        }
    }

    return (
        <>
            <AlertDialog open={substituteDialogOpen} onOpenChange={setSubstituteDialogOpen}>
                <AlertDialogContent className="sm:max-w-md">
                    <AlertDialogHeader>
                        <AlertDialogTitle>Duplicated documents</AlertDialogTitle>
                        <AlertDialogDescription>
                            The following documents are already present in the system.
                            Please select the documents you want to overwrite.
                            The rest will be ignored.
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <div className="flex items-center space-x-2">
                        <div className="grid flex-1 gap-2">
                            {
                                Array.from(duplicatedDocumentIds).map((documentId, index) => (
                                    <div key={index} className="flex items-center space-x-2">
                                        <Checkbox
                                            checked={ignoreDocumentIds.includes(documentId)}
                                            onClick={() => toggleIgnoredDocument(documentId)}
                                        />
                                        <div>
                                            {documentId}
                                        </div>
                                    </div>
                                ))
                            }
                        </div>
                    </div>
                    <AlertDialogFooter>
                        <AlertDialogAction onClick={() => {
                            removeFilesFromState(ignoreDocumentIds)
                            onSubmit()
                        }}>Submit</AlertDialogAction>
                        <AlertDialogCancel onClick={() => {
                            setSubstituteDialogOpen(false)
                        }}>Cancel</AlertDialogCancel>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
            <form
                onSubmit={
                    (e) => {
                        e.preventDefault()
                        onPreSubmit()
                    }
                }
                onDragEnter={handleDrag}
                className="w-full space-y-4"
            >
                <div className="flex md:h-96 items-center md:rounded-lg md:flex-row w-full h-full flex-col-reverse gap-4">
                    {!noInput && (
                        <>
                            {/* Summary of documents */}
                            <div className="w-full md:w-8/12 h-full max-h-96 flex flex-col">
                                <ScrollArea className="rounded-lg">
                                    <table className="min-w-full divide-y dark:divide-slate-600">
                                        <thead className="z-10 sticky top-0">
                                            <tr className="bg-secondary">
                                                <th
                                                    scope="col"
                                                    className="px-6 py-3 text-left font-medium dark:text-slate-300 tracking-wider"
                                                >
                                                    Name
                                                </th>
                                                <th
                                                    scope="col"
                                                    className="px-6 py-3 text-left font-medium dark:text-slate-300 tracking-wider"
                                                >
                                                    Size
                                                </th>
                                                <th
                                                    scope="col"
                                                    className="px-6 py-3 text-left font-medium dark:text-slate-300 tracking-wider"
                                                >
                                                    Type
                                                </th>
                                                <th>
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody className="relative divide-y">
                                            {input.map((file, index) => (
                                                <StagingAreaTableRow
                                                    key={index}
                                                    file={file}
                                                    deleteAction={removeFilesFromState}
                                                />
                                            ))}
                                        </tbody>
                                    </table>
                                    <ScrollBar orientation='horizontal' />
                                </ScrollArea>
                            </div>
                        </>)}

                    {/* Drag and drop area */}
                    <div className={`w-full h-full ${!noInput && "md:w-4/12"}`}>
                        <label
                            htmlFor="dropzone-file"
                            className='h-full flex flex-col items-center cursor-pointer justify-center w-full border-2 border-muted-300 border-dashed rounded-lg'>
                            <div
                                className={cn(
                                    'relative w-full h-full flex flex-col items-center justify-center',
                                    { 'items-start': !noInput }
                                )}
                            >

                                <div
                                    className={cn(
                                        "h-full p-8 text-center flex flex-col items-center justify-center w-full hover:bg-accent/80",
                                        { 'bg-accent/80': dragActive }
                                    )}
                                    onDragEnter={handleDrag}
                                    onDragLeave={handleDrag}
                                    onDragOver={handleDrag}
                                    onDrop={handleDrop}
                                >
                                    <svg
                                        aria-hidden="true"
                                        className="w-10 h-10 mb-3 text-gray-400"
                                        fill="none"
                                        stroke="currentColor"
                                        viewBox="0 0 24 24"
                                        xmlns="http://www.w3.org/2000/svg"
                                    >
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth="2"
                                            d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                                        ></path>
                                    </svg>
                                    <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
                                        <span className="font-semibold">Click to upload</span> or drag
                                        and drop
                                    </p>
                                    <p className="text-xs text-gray-500 dark:text-gray-400">
                                        {prettyBytes(MAX_FILE_SIZE)} per file
                                    </p>
                                    <input
                                        multiple
                                        onChange={handleChange}
                                        accept="application/pdf, application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                                        id="dropzone-file"
                                        type="file"
                                        className="hidden"
                                    />
                                </div>
                            </div>
                        </label>
                    </div>
                </div>
                {!noInput && (
                    <div className="space-x-2 pr-4 w-full flex justify-center">
                        <Button
                            variant="secondary"
                            className="space-x-4 md:w-1/4 w-1/2"
                            onClick={
                                () => {
                                    setDuplicatedDocumentIds(new Set())
                                    setIgnoreDocumentIds([])
                                    removeAllFilesFromState()
                                }
                            }>
                            <div className="font-bold">
                                Cancel upload
                            </div>
                            <CircleSlashIcon className="w-5 h-5" />
                        </Button>
                        <Button
                            variant="info"
                            className="space-x-4 md:w-1/4 w-1/2"
                            type="submit">
                            <div className="font-bold">
                                Upload documents
                            </div>
                            <FolderUpIcon className="w-5 h-5" />
                        </Button>
                    </div>
                )}
            </form>
        </>
    )
}
StagingArea.displayName = 'StagingArea'