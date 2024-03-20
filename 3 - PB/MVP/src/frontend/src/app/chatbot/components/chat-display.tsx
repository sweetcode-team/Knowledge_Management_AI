import * as React from "react"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { Textarea } from "@/components/ui/textarea"
import { Chat } from "@/app/chatbot/data"
import { ScrollArea, ScrollBar } from '@/components/ui/scroll-area';
import { ChatContent } from "@/app/chatbot/components/chat-content"
import { ChatHeader } from "./chat-header"
import Image from "next/image"
import { EraserIcon, MicIcon, PauseIcon, PlayIcon, SendIcon, StopCircleIcon, XCircleIcon } from "lucide-react"
import { Toggle } from "@/components/ui/toggle"
import { useState, useRef, useEffect } from 'react';
import { Message } from '../data';

interface ChatDisplayProps {
  chat?: Chat
}

export function ChatDisplay({ chat }: ChatDisplayProps) {
  // const [messages, setMessages] = useState(chat?.messages)
  const [input, setInput] = useState("")
  const [isRecording, setIsRecording] = useState(false)
  const [isPaused, setIsPaused] = useState(false)
  const recognitionRef = useRef<any>(null)

  // useEffect(() => {
  //   setMessages(chat?.messages)
  // }, [chat])

  const handleMessageSubmit = () => {
    if (input.trim().length === 0) return
    const timestamp = new Date().toLocaleTimeString();
    // setMessages([
    //   ...messages || [],
    //   {
    //     role: "user",
    //     content: input,
    //     timestamp: timestamp,
    //   } as Message,
    // ])
    setInput("")
    setIsRecording(false)
    setIsPaused(false)
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
            <Image src="sweetcode-logo.svg" width={70} height={70} className="dark:invert" alt="SWEetCode logo" />
            <h4 className="text-lg font-bold" >Hey, how can I help you?</h4>
          </div>
        )}
        <div>
          <Separator className="mt-auto" />
          <form className="p-4" onSubmit={(e) => {
            e.preventDefault()
            handleMessageSubmit()
          }}>
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
              <Textarea
                className="flex-1 min-h-28"
                placeholder={`Type your message...`}
                value={input}
                onChange={(e) => setInput(e.target.value.trimStart())}
              />
              <div className="flex flex-col space-y-2">
                <Button
                  type="submit"
                  size="icon"
                  disabled={input.trim().length === 0}
                >
                  <SendIcon
                    className="w-4 h-4"
                    onClick={() => {
                      handleMessageSubmit()
                    }}
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
        </div>
      </div >
    </div >
  )
}
