"use client"

import { Button } from "@/components/ui/button";
import { Form, FormField, FormItem } from "@/components/ui/form";
import { Separator } from "@/components/ui/separator";
import { Textarea } from "@/components/ui/textarea";
import { Toggle } from "@/components/ui/toggle";
import { askChatbot } from "@/lib/actions";
import { AskChatbotFormValues, MessageResponse, askChatbotFormSchema } from "@/types/types";
import { zodResolver } from "@hookform/resolvers/zod";
import { EraserIcon, MicIcon, PauseIcon, PlayIcon, SendIcon, StopCircleIcon } from "lucide-react";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { toast } from "sonner";

interface ChatFooterProps {
    chatId?: number
}

export default function ChatFooter({ chatId }: ChatFooterProps) {
    const [isRecording, setIsRecording] = useState(false)
    const [isPaused, setIsPaused] = useState(false)
    const recognitionRef = useRef<any>(null)

    const router = useRouter()

    const form = useForm<AskChatbotFormValues>({
        resolver: zodResolver(askChatbotFormSchema),
        defaultValues: {
            message: ""
        },
        mode: "onChange",
    })

    const watchMessage = form.watch("message")

    const onSubmit: SubmitHandler<AskChatbotFormValues> = async (data) => {
        setIsRecording(false)
        setIsPaused(false)

        if (chatId !== undefined) {
            data.chatId = chatId
        }

        const toastId = toast.loading("Loading...", {
            description: "Sending message.",
        })

        let result: MessageResponse
        try {
            result = await askChatbot(data)
        } catch (e) {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }

        if (!result || !result.status) {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }
        if (chatId === undefined)
            router.push(`/chatbot/${result.chatId}`)
        form.reset({ message: "" })
    }

    useEffect(() => {
        if (!("webkitSpeechRecognition" in window)) {
            console.log("Speech recognition not supported")
            return
        }

        recognitionRef.current = new (window as any).webkitSpeechRecognition()
        const recognition = recognitionRef.current;
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.lang = "it-IT";

        recognition.onresult = (event: any) => {
            console.log("onresult")
            let interTranscript = '';
            for (let i = event.resultIndex; i < event.results.length; i++) {
                const transcript = event.results[i][0].transcript;
                if (event.results[i].isFinal) {
                    if (isRecording) {
                        form.setValue("message", transcript.trim());
                    }
                    else {
                        const prevInput = form.getValues().message;
                        const trimmedPrevInput = prevInput ? prevInput.trim() : '';
                        const trimmedTranscript = transcript.trim();
                        form.setValue("message", trimmedPrevInput ? trimmedPrevInput + ' ' + trimmedTranscript : trimmedTranscript)
                    }
                }
                else {
                    interTranscript += transcript;
                }
                console.log(interTranscript)
            }
        }

        recognition.onend = () => {
            console.log("onend")
            pauseRecording()
        }

        recognition.onerror = () => {
            console.log("onerror")
            pauseRecording()
        }

        return () => {
            if (recognition) {
                recognition.stop()
            }
        }
    }, [])

    const startRecording = () => {
        console.log("startRecording")
        if (recognitionRef.current) {
            recognitionRef.current.start()
        }
        setIsRecording(true)
        setIsPaused(false)
    }

    const stopRecording = () => {
        console.log("stopRecording")
        if (recognitionRef.current) {
            recognitionRef.current.stop();
        }
        setIsRecording(false)
        setIsPaused(false)
    }

    const pauseRecording = () => {
        console.log("pauseRecording")
        if (recognitionRef.current) {
            recognitionRef.current.stop();
        }
        setIsPaused(true)
    }

    const resumeRecording = () => {
        console.log("resumeRecording")
        if (recognitionRef.current) {
            recognitionRef.current.start();
        }
        setIsPaused(false)
    }

    return (
        <Form {...form}>
            <Separator className="mt-auto" />
            <form className="p-4" onSubmit={form.handleSubmit(onSubmit)}>
                <div className="flex max-h-full justify-between space-x-2">
                    <div className="flex flex-col space-y-2">
                        <Button
                            onClick={
                                (e) => {
                                    e.preventDefault()
                                    if (isRecording) {
                                        stopRecording();
                                    } else {
                                        startRecording();
                                    }
                                }
                            }
                            variant={isRecording ? isPaused ? "danger" : "destructive" : "default"}
                            size="icon"
                            disabled={form.formState.isSubmitting}
                        >
                            {!isRecording ? <MicIcon className="w-4 h-4" /> : <StopCircleIcon className="w-4 h-4" />}
                        </Button>
                        {
                            isRecording ? (
                                <Toggle
                                    aria-label="Toggle audio register"
                                    onClick={
                                        (e) => {
                                            e.preventDefault()
                                            if (isPaused) {
                                                resumeRecording();
                                            } else {
                                                pauseRecording();
                                            }
                                        }
                                    }
                                >
                                    {isPaused ? <PlayIcon className="h-4 w-4" /> : <PauseIcon className="h-4 w-4" />}
                                </Toggle>
                            ) : null
                        }
                    </div>
                    <FormField
                        control={form.control}
                        name="message"
                        render={({ field }) => (
                            <FormItem className="flex-1">
                                <Textarea
                                    className="flex-1 min-h-28 max-h-60"
                                    placeholder={`Type your message...`}
                                    {...field}
                                    disabled={form.formState.isSubmitting}
                                />
                            </FormItem>
                        )}
                    />
                    <div className="flex flex-col space-y-2">
                        <Button
                            type="submit"
                            size="icon"
                            disabled={watchMessage === "" || form.formState.isSubmitting}
                        >
                            <SendIcon
                                className="w-4 h-4"
                            />
                        </Button>
                        {
                            watchMessage !== "" &&
                            <Button
                                variant={"warning"}
                                size="icon"
                                onClick={(e) => {
                                    e.preventDefault()
                                    form.reset({ message: "" })
                                }}
                                disabled={form.formState.isSubmitting}
                            >
                                <EraserIcon className="w-4 h-4" />
                            </Button>
                        }
                    </div>
                </div>
            </form>
        </Form>
    )
}
