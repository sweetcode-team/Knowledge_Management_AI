"use client"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { useToast } from "@/components/ui/use-toast";
import { SquarePenIcon, TrashIcon } from "lucide-react"
import { useEffect, useState } from "react";

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Form, FormControl, FormField, FormItem, FormMessage } from "@/components/ui/form";

const RenameChatFormSchema = z.object({
    title: z.string().min(1).max(70),
})

interface ChatHeaderProps {
    chatTitle?: string,
    isChatSelected: boolean,
}

export function ChatHeader({ chatTitle, isChatSelected }: ChatHeaderProps) {
    const [isBeingRenamed, setIsBeingRenamed] = useState(false);

    const { toast } = useToast()

    const form = useForm<z.infer<typeof RenameChatFormSchema>>({
        resolver: zodResolver(RenameChatFormSchema),
        defaultValues: {
            title: chatTitle,
        },
    })

    useEffect(() => {
        form.reset({
            title: chatTitle,
        })
    }, [chatTitle])

    function onSubmit(data: z.infer<typeof RenameChatFormSchema>) {
        if (data.title !== "" && data.title !== chatTitle) {
            // Rename chat
            toast({
                title: "Operation successful",
                description: "Chat renamed.",
            })
            // toast({
            //     variant: "destructive",
            //     title: "Operation failed",
            //     description: "Chat rename failed.",
            // })
        }
        setIsBeingRenamed(false)
        form.reset()
    }



    return (
        <div className="flex w-full items-center py-2 px-4">
            {
                !chatTitle ?
                    (
                        <h3 className="h-[40px] w-full flex items-center border-0 p-0 line-clamp-1 text-xl font-bold pl-2">New chat</h3>
                    ) :
                    (
                        <div className="flex w-full items-center space-x-2">
                            {isBeingRenamed ? (
                                <Form {...form}>
                                    <form
                                        onSubmit={form.handleSubmit(onSubmit)}
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
                                                    disabled={!form.formState.isValid}
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
                                        <Tooltip >
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
                                <Tooltip>
                                    <TooltipTrigger asChild>
                                        <Button variant="danger" size="icon" disabled={!isChatSelected || isBeingRenamed} onClick={() => { }}>
                                            <TrashIcon className="h-4 w-4" />
                                            <span className="sr-only">Delete chat</span>
                                        </Button>
                                    </TooltipTrigger>
                                    <TooltipContent>Delete chat</TooltipContent>
                                </Tooltip>
                            </div>
                        </div>
                    )
            }
        </div>
    )
}