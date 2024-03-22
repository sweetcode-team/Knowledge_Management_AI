import { useState, useRef, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { Textarea } from "@/components/ui/textarea"
import { ScrollArea, ScrollBar } from '@/components/ui/scroll-area';
import { ChatContent } from "@/app/chatbot/components/chat-content"
import { ChatHeader } from "./chat-header"
import { EraserIcon, MicIcon, PauseIcon, PlayIcon, SendIcon, StopCircleIcon } from "lucide-react"
import { Toggle } from "@/components/ui/toggle"
import { SWEetCodeLogo } from "@/components/sweetcode-logo"

import {
  askChatbotFormSchema,
  AskChatbotFormValues,
  Chat,
  configurationFormSchema,
  ConfigurationFormValues,
  Message,
  MessageResponse,
  MessageSender
} from "@/types/types"

import {getChatMessages, askChatbot, changeConfiguration} from "@/lib/actions"
import {SubmitHandler, useForm} from "react-hook-form";
import {zodResolver} from "@hookform/resolvers/zod";
import {toast} from "@/components/ui/use-toast";
import {Form, FormField, FormItem} from "@/components/ui/form";

interface ChatDisplayProps {
  chatId: Chat["id"] | null
}

export function ChatDisplay({ chatId }: ChatDisplayProps) {
  const [input, setInput] = useState("")
  const [isRecording, setIsRecording] = useState(false)
  const [isPaused, setIsPaused] = useState(false)
  const recognitionRef = useRef<any>(null)
  const [chat, setChat] = useState<Chat | null>(null);

  const form = useForm<AskChatbotFormValues>({
    resolver: zodResolver(askChatbotFormSchema),
    defaultValues: {chatId: chatId},
    mode: "onChange",
  })

  const onSubmit: SubmitHandler<AskChatbotFormValues> = async (data) => {
    const result = await askChatbot(data);
    // setChat(prevChat => {
    //   if (!prevChat) {
    //     return null
    //   } return {
    //     ...prevChat,
    //     messages: [
    //       ...prevChat.messages,
    //       {
    //         sender: MessageSender.CHATBOT,
    //         content: response.messageResponse.content,
    //         timestamp: response.messageResponse.timestamp,
    //         relevantDocuments: response.messageResponse.relevantDocuments
    //       }
    //     ]
    //   }
    // })
    if (!result) {
      toast({
        variant: "destructive",
        title: "An error occurred",
        description: "Please try again later.",
      })
      return
    }

    if (!result.status) {
      toast({
        variant: "destructive",
        title: "An error occurred",
      })
    }
  }

  useEffect(() => {
    const fetchMessages = async () => {
      try {
        if (chatId) {
          const chat = await getChatMessages(chatId)
          setChat(chat)
        }
      } catch (error) {
        toast({
        variant: "destructive",
        title: "An error occurred while fetching messages",
      })
      }
    }
    fetchMessages()
  }, [chatId])

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
            setInput(transcript.trim());
          } else {
            setInput(prevInput => {
              const trimmedPrevInput = prevInput ? prevInput.trim() : '';
              const trimmedTranscript = transcript.trim();
              return trimmedPrevInput ? trimmedPrevInput + ' ' + trimmedTranscript : trimmedTranscript;
            });
          }
        } else {
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
  }, [isRecording, isPaused])

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
    <div className="flex h-full flex-col">
      <ChatHeader chatTitle={chat?.title} isChatSelected={!!chat} />
      <Separator />
      <div className="h-full flex flex-1 flex-col justify-between overflow-auto">
        {chat ? (
          <div className="flex-1 whitespace-pre-wrap text-sm overflow-auto">
            <ScrollArea className="h-full">
              <div className="p-4 pb-0">
                <ChatContent messages={chat?.messages} />
              </div>
            </ScrollArea>
          </div>
        ) : (
          <div className="h-full flex flex-col items-center justify-center select-none animate-show-in" >
            <SWEetCodeLogo className="w-20 h-20" />
            <h4 className="text-lg font-bold" >Hey, how can I help you?</h4>
          </div>
        )}
        <div>
          <Separator className="mt-auto" />
          <Form {...form}>
            <form className="p-4" onSubmit={form.handleSubmit(onSubmit)}>
              <div className="flex max-h-full justify-between space-x-2">
                <div className="flex flex-col space-y-2">
                  <Button
                    onClick={
                      () => {
                        if (isRecording) {
                          stopRecording();
                        } else {
                          startRecording();
                        }
                      }
                    }
                    variant={isRecording ? isPaused ? "danger" : "destructive" : "default"}
                    size="icon"
                  >
                    {!isRecording ? <MicIcon className="w-4 h-4" /> : <StopCircleIcon className="w-4 h-4" />}
                  </Button>
                  {
                    isRecording ? (
                      <Toggle
                        aria-label="Toggle audio register"
                        onClick={
                          () => {
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
                <FormField name="chatId" render={({field}) => {
                  <FormItem defaultValue={field.value}></FormItem>
                }}>
                </FormField>
                <FormField
                  control={form.control}
                  name="message"
                  render={({ field }) => (
                    <FormItem>
                    <Textarea
                      className="flex-1 min-h-28 max-h-60"
                      placeholder={`Type your message...`}
                      onChange={field.onChange}
                      defaultValue={field.value}
                    />
                    </FormItem>
                  )}
                    />
                    <div className="flex flex-col space-y-2">
                      <Button
                        type="submit"
                        size="icon"
                      >
                        <SendIcon
                          className="w-4 h-4"
                        />
                      </Button>
                      {
                        input !== "" ? (
                          <Button
                            variant={"warning"}
                            onClick={() => setInput("")}
                            size="icon"
                          >
                            <EraserIcon className="w-4 h-4" />
                          </Button>
                        ) : null
                      }
                </div>
              </div>
            </form>
          </Form>
        </div>
      </div >
    </div >
  )
}
