"use client"
import { Button, buttonVariants } from "@/components/ui/button"
import { Input } from "@/components/ui/input";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { toast } from "sonner"
import { SquarePenIcon, TrashIcon } from "lucide-react"
import { useState } from "react";

import { zodResolver } from "@hookform/resolvers/zod"
import { SubmitHandler, useForm } from "react-hook-form"
import { Form, FormControl, FormField, FormItem, FormMessage } from "@/components/ui/form";
import { ChatOperationResponse, RenameChatFormValues, renameChatFormSchema } from "@/types/types";
import { deleteChats, renameChat } from "@/lib/actions";
import { useRouter } from "next/navigation";
import { AlertDialog, AlertDialogAction, AlertDialogCancel, AlertDialogContent, AlertDialogDescription, AlertDialogFooter, AlertDialogHeader, AlertDialogTitle, AlertDialogTrigger } from "@/components/ui/alert-dialog";
import { cn } from "@/lib/utils";

interface ChatHeaderProps {
    chatTitle?: string,
    isChatSelected: boolean,
    chatId?: number
}

export function ChatHeader({ chatTitle, chatId, isChatSelected }: ChatHeaderProps) {
    const [isBeingRenamed, setIsBeingRenamed] = useState(false);

    const router = useRouter()

    const form = useForm<RenameChatFormValues>({
        resolver: zodResolver(renameChatFormSchema),
        defaultValues: {
            title: chatTitle,
            chatId: chatId
        }
    })

    const onRenameSubmit: SubmitHandler<RenameChatFormValues> = async (data) => {
        const toastId = toast.loading("Loading...", {
            description: "Renaming the chat.",
        })

        let result: ChatOperationResponse
        try {
            result = await renameChat(data)
        } catch (e) {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }

        if (!result) {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }
        else if (result.status) {
            toast.success("Operation successful", {
                description: "Chat has been renamed.",
                id: toastId
            })
        }
        else {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }
        setIsBeingRenamed(false)
        form.reset({
            title: data.title,
            chatId: data.chatId
        })
    }

    const onDeleteSubmit = async (chatId: number) => {
        const toastId = toast.loading("Loading...", {
            description: "Deleting the chat.",
        })

        let results: ChatOperationResponse[]
        try {
            results = await deleteChats([chatId])
        } catch (e) {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }

        toast.dismiss(toastId);

        results.forEach(result => {
            if (!result || !result.status) {
                toast.error("An error occurred", {
                    description: "Error while deleting the chat:" + result.message,
                })
                return
            } else {
                toast.success("Operation successful", {
                    description: "Chat has been deleted.",
                })
            }
        })
        router.push(`/chatbot`)
    }

    const watchMessage = form.watch("title")

    return (
        <div className="flex w-full items-center py-2 px-4">
            {
                !chatId ?
                    (
                        <h3 className="h-[40px] w-full flex items-center border-0 p-0 line-clamp-1 text-xl font-bold pl-2">New chat</h3>
                    ) :
                    (
                        <div className="flex w-full items-center space-x-2">
                            {isBeingRenamed ? (
                                <Form {...form}>
                                    <form onSubmit={form.handleSubmit(onRenameSubmit)}
                                        onBlur={(e) => {
                                            if (e.relatedTarget?.id !== "rename-button" && e.relatedTarget?.id !== "rename-input") {
                                                setIsBeingRenamed(false)
                                                form.reset()
                                            }
                                        }}
                                        className="flex space-x-2 w-full"
                                    >
                                        <FormField
                                            control={form.control}
                                            name="chatId"
                                            render={({ field }) => (
                                                <FormItem>
                                                    <FormControl>
                                                        <Input
                                                            type="hidden"
                                                            {...field}
                                                        />
                                                    </FormControl>
                                                    <FormMessage />
                                                </FormItem>
                                            )}
                                        />
                                        <FormField
                                            control={form.control}
                                            name="title"
                                            render={({ field }) => (
                                                <FormItem className="w-full">
                                                    <FormControl className="w-full">
                                                        <Input
                                                            id="rename-input"
                                                            type="text"
                                                            className="p-0 line-clamp-1 text-xl font-bold mr-2 pl-2"
                                                            autoFocus
                                                            {...field}
                                                        />
                                                    </FormControl>
                                                    <FormMessage />
                                                </FormItem>
                                            )}
                                        />
                                        <Tooltip>
                                            <TooltipTrigger asChild>
                                                <Button
                                                    id="rename-button"
                                                    variant={isBeingRenamed ? "safe" : "secondary"}
                                                    size="icon"
                                                    type="submit"
                                                    disabled={watchMessage === "" || watchMessage === chatTitle || form.formState.isSubmitting}
                                                    className="min-w-[40px]"
                                                >
                                                    <SquarePenIcon className="h-4 w-4" />
                                                    <span className="sr-only">Rename chat</span>
                                                </Button>
                                            </TooltipTrigger>
                                            <TooltipContent>Rename chat</TooltipContent>
                                        </Tooltip>
                                    </form>
                                </Form>
                            ) : (
                                <h3 className="w-full border-0 p-0 line-clamp-1 text-xl font-bold pl-2">{chatTitle}</h3>
                            )}
                            <div className="inline-flex ml-auto space-x-2">
                                {
                                    !isBeingRenamed ?
                                        <Tooltip>
                                            <TooltipTrigger asChild>
                                                <Button
                                                    variant="secondary"
                                                    size="icon"
                                                    onClick={() => {
                                                        setIsBeingRenamed(true)
                                                    }}
                                                >
                                                    <SquarePenIcon className="h-4 w-4" />
                                                    <span className="sr-only">Rename chat</span>
                                                </Button>
                                            </TooltipTrigger>
                                            <TooltipContent>Rename chat</TooltipContent>
                                        </Tooltip> :
                                        null
                                }
                                <AlertDialog>
                                    <AlertDialogTrigger asChild>
                                        <Button
                                            variant="danger"
                                            size="icon"
                                            disabled={!isChatSelected || isBeingRenamed}
                                        >
                                            <TrashIcon className="h-4 w-4" />
                                            <span className="sr-only">Delete chat</span>
                                        </Button>
                                    </AlertDialogTrigger>
                                    <AlertDialogContent>
                                        <AlertDialogHeader>
                                            <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                                            <AlertDialogDescription>
                                                This action cannot be undone. This will permanently delete the selected chat.
                                            </AlertDialogDescription>
                                        </AlertDialogHeader>
                                        <AlertDialogFooter>
                                            <AlertDialogCancel id="dialog-cancel">Abort</AlertDialogCancel>
                                            <AlertDialogAction id="dialog-action"
                                                className={cn(buttonVariants({ variant: "destructive" }), "mt-2 sm:mt-0")}
                                                onClick={() => onDeleteSubmit(chatId)}
                                            >Delete
                                            </AlertDialogAction>
                                        </AlertDialogFooter>
                                    </AlertDialogContent>
                                </AlertDialog>
                            </div>
                        </div>
                    )
            }
        </div>
    )
}