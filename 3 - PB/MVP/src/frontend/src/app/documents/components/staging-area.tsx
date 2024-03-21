'use client'

import {
  forwardRef,
  useReducer,
  useState,
  type ChangeEvent,
  type DragEvent,
} from 'react'
import { FileUpload } from './file-upload'
import { MAX_FILE_SIZE } from '@/constants/constants'
import { useToast } from '@/components/ui/use-toast'
import {cn, validateFileType} from "@/lib/utils";
import { Button } from '@/components/ui/button'
import { CircleSlashIcon, FolderUpIcon } from 'lucide-react'
import { ScrollArea } from '@/components/ui/scroll-area'

interface FileWithUrl {
  name: string
  getUrl: string
  size: number
  type: string
  error?: boolean | undefined
}

// Reducer action(s)
const addFilesToInput = () => ({
  type: 'ADD_FILES_TO_INPUT' as const,
  payload: [] as FileWithUrl[],
})

const removeFilesFromInput = (name: string) => ({
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
type State = FileWithUrl[]

export interface InputProps
  extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type'> {}

const addFileIfNotPresent = (files: FileList, stagingFiles: FileWithUrl[]): File[] => {
    const filesNotOk = []
    for (let i = 0; i < files.length; i++) {
        for (let j = 0; j < stagingFiles.length; j++) {
            if(files[i].name === stagingFiles[j].name)
                filesNotOk.push(files[i])
        }
    }
    return filesNotOk
};
const removeAlreadyPresentFiles = (files: FileList, stagingFiles: FileWithUrl[]): File[] => {
    const updatedFilesArray: File[] = Array.from(files);
    return updatedFilesArray.filter(file => !stagingFiles.some(stagingFile => stagingFile.name === file.name));
};

export const StagingArea = forwardRef<HTMLInputElement, InputProps>(
    ({ className, ...props }, ref) => {
        const { toast } = useToast()
        const [dragActive, setDragActive] = useState<boolean>(false)
        const [input, dispatch] = useReducer((state: State, action: Action) => {
            switch (action.type) {
                case 'ADD_FILES_TO_INPUT': {
                    return [...state, ...action.payload]
                }
                case 'REMOVE_FILES_FROM_INPUT': {
                    return state.filter((file) => file.name !== action.payload)
                }
                case 'REMOVE_ALL_FILES_FROM_INPUT': {
                    return []
                }

                // You could extend this, for example to allow removing files
            }
        }, [])


        const noInput = input.length === 0

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
        const handleChange = async (e: ChangeEvent<HTMLInputElement>) => {
            e.preventDefault()
            try {
                if (e.target.files && e.target.files[0]) {
                    // at least one file has been selected
                    const files = Array.from(e.target.files)
                    // validate file type
                    const validFiles = files.filter((file) => validateFileType(file))
                    if (!validFiles) {
                        toast({
                            title: 'Invalid file type',
                            description: 'Please upload a valid file type.',
                        })
                        return
                    }

                    const alreadyPresent = addFileIfNotPresent(e.target.files, input)

                    if(alreadyPresent.length > 0){
                        toast({
                            variant: 'destructive',
                            title: 'file already present',
                            description: 'Please upload a different file.',
                        })
                    }
                    const validFilesWithoutAlreadyPresent = removeAlreadyPresentFiles(e.target.files, input);

                    console.log(e)
                    const filesWithUrl = await Promise.all(
                        validFilesWithoutAlreadyPresent.map(async (file) => {
                            const {name, size} = file
                            const getUrl = file.webkitRelativePath
                            const type = file.type
                            return {name, size, getUrl, type}
                        })
                    )
                    addFilesToState(filesWithUrl)
                }
            } catch (error) {
                // already handled
            }
        }

        const addFilesToState = (files: FileWithUrl[]) => {
            dispatch({type: 'ADD_FILES_TO_INPUT', payload: files})
        }

        // triggers when file is dropped
        const handleDrop = async (e: DragEvent<HTMLDivElement>) => {
            e.preventDefault()
            e.stopPropagation()

            // validate file type
            if (e.dataTransfer.files && e.dataTransfer.files[0]) {
                const files = Array.from(e.dataTransfer.files)
                const validFiles = files.filter((file) => validateFileType(file))

                if (files.length !== validFiles.length) {
                    toast({
                        title: 'Invalid file type',
                        description: 'Only image files are allowed.',
                    })
                }
                if(addFileIfNotPresent(e.dataTransfer.files, input).length > 0){
                    toast({
                        variant: 'destructive',
                        title: 'File already present',
                        description: 'Please upload a different file.',
                    })
                }
                const validFilesWithoutAlreadyPresent = removeAlreadyPresentFiles(e.dataTransfer.files, input);
                try {
                    console.log(e)
                    const filesWithUrl = await Promise.all(
                        validFilesWithoutAlreadyPresent.map(async (file) => {
                            const {name, size} = file
                            const getUrl = e.dataTransfer.files[0].webkitRelativePath
                            const type = e.dataTransfer.files[0].type
                            return {name, size, getUrl, type}
                        })
                    )

                    setDragActive(false)

                    // at least one file has been selected
                    addFilesToState(filesWithUrl)

                    e.dataTransfer.clearData()
                } catch (error) {
                    // already handled
                }
            }
        }

        return (
            <>
            <form
                onSubmit={(e) => e.preventDefault()}
                onDragEnter={handleDrag}
                className="flex h-96 items-center w-full justify-start"
            >
                
                <div className="sm:rounded-lg sm:flex-row w-full h-full flex flex-col-reverse gap-4">
                    {!noInput && (
                    <>
                    {/* Summary of documents */}
                    <div className="w-full h-full max-h-96 flex flex-col">
                        <ScrollArea className= "rounded-lg">
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
                            <tbody className="relative divide-y dark:divide-slate-600">
                                {input.map((file, index) => (
                                    <FileUpload
                                        key={index}
                                        error={file.error}
                                        type={file.type}
                                        getUrl={file.getUrl}
                                        name={file.name}
                                        size={file.size}
                                        deleteAction={() => {
                                            dispatch(removeFilesFromInput(file.name))
                                        }}
                                    />
                                ))}
                            </tbody>
                        </table>
                        </ScrollArea>
                    </div>
                    </>)} 

                    {/* Drag and drop area */}
                    <div className="w-full h-full min-w-1/2">
                        <label
                            htmlFor="dropzone-file"
                            className={cn(
                                'h-full flex flex-col items-center justify-center w-full border-2 border-muted-300 border-dashed rounded-lg',
                                { 'dark:border-slate-400 dark:bg-slate-800': dragActive },
                            )}
                        >
                            <div
                                className={cn(
                                    'relative w-full h-full flex flex-col items-center justify-center',
                                    { 'items-start': !noInput }
                                )}
                            >

                            <div
                                className="h-full cursor-pointer flex flex-col items-center justify-center w-full"
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
                                {(MAX_FILE_SIZE / 1000000).toFixed(0)}MB per file
                            </p>
                            <input
                                {...props}
                                ref={ref}
                                multiple
                                onChange={handleChange}
                                accept="application/pdf, application/msword"
                                id="dropzone-file"
                                type="file"
                                className="hidden"
                            />
                            </div>
                            </div>
                        </label>
                    </div>
                </div>
            </form>
            {!noInput && (
            <>
            <div className="space-x-2 pr-4 w-full flex justify-center">
            <Button 
            variant="secondary" 
            className="space-x-4 md:w-1/4 w-1/2" 
            onClick={
                () => {
                    dispatch(removeAllFilesFromInput())
                }
            }>
                <div className="font-bold">
                    Cancel upload
                </div>
                <CircleSlashIcon className="w-5 h-5" />
            </Button>
            <Button variant="info" className="space-x-4 md:w-1/4 w-1/2">
                <div className="font-bold">
                    Upload documents
                </div>
                <FolderUpIcon className="w-5 h-5" />
            </Button>
            </div>
            </>
            )}
            </> 
        )
    }
)