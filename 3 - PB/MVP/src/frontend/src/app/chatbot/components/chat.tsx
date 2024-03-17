"use client"
import * as React from "react"
import MessageContent, { MessageContentProps } from '@/app/chatbot/components/message-content';
import {
  Card,
} from "@/components/ui/card"
import { CardContent } from '@/app/chatbot/components/card-content';
import { CardFooter } from '@/app/chatbot/components/card-footer';

export function CardsChat() {
  const showDocument = () => {
    console.log("Show Document");
  }

  const [messages, setMessages] = React.useState([
    {
      role: "agent",
      content: <MessageContent text="Hi, how can i help you today?" onButtonClick={showDocument} role = "agent"/>,
      timestamp: new Date().toLocaleTimeString(),
    },
    {
      role: "user",
      content: <MessageContent text="Hey, I'm having trouble with my account." onButtonClick={showDocument} role ="user"/>,
      timestamp: new Date().toLocaleTimeString(),
    },
    {
      role: "agent",
      content: <MessageContent text="Hi, how can i help you today?" onButtonClick={showDocument} role = "agent"/>,
      timestamp: new Date().toLocaleTimeString(),
    },
  ])

  const [input, setInput] = React.useState("")
  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text)
  }

  const [isRecording, setIsRecording] = React.useState(false);
  const [isButtonDisabled, setIsButtonDisabled] = React.useState(false);
  const [isPaused, setIsPaused] = React.useState(false);
  const [isMicClicked, setIsMicClicked] = React.useState(false);
  const recognition = React.useRef<any>(null); 

  const startRecording = () => {

    if(isRecording) {
      return
    }

    setIsRecording(true); 

    recognition.current = new (window as any).webkitSpeechRecognition();
    recognition.current.continuous = true; 
    recognition.current.interimResults = true; 
    recognition.current.lang = "it-IT";
  
    recognition.current.onresult = (event: any) => {
      let interimTranscript = '';
      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          if (isMicClicked) {
            setInput(transcript.trim());
          } else {
            setInput(prevInput => {
              const trimmedPrevInput = prevInput ? prevInput.trim() : '';
              const trimmedTranscript = transcript.trim();
              return trimmedPrevInput ? trimmedPrevInput + ' ' + trimmedTranscript : trimmedTranscript;
            });
          }
        } else {
          interimTranscript += transcript;
        }
      }
    };
      
    recognition.current.onend = () => {
      recognition.current.stop(); 
      setIsRecording(false); 
    };
  
    recognition.current.onerror = (event: any) => {
      setIsRecording(false); 
    };

    recognition.current.start(); 
    setIsPaused(false);
    return () => {
      if (recognition.current) {
        recognition.current.stop();
      }
    };
  };
  
  const stopRecording = () => {
    if (recognition) {
      recognition.current.stop();
      setIsRecording(false); 
      setIsButtonDisabled(true);

      setTimeout(() => {
        setIsButtonDisabled(false);
      }, 1500);
    }
    setIsMicClicked(false);
    setIsPaused(false);
  };

  
  return (
    <>
      <Card>
        <CardContent messages={messages} copyToClipboard={copyToClipboard} />
        <CardFooter input={input} setInput={setInput} isRecording={isRecording} setIsRecording={setIsRecording} startRecording={startRecording} stopRecording={stopRecording} isPaused={isPaused} setIsPaused={setIsPaused} isMicClicked={isMicClicked} setIsMicClicked={setIsMicClicked} isButtonDisabled={isButtonDisabled} setIsButtonDisabled={setIsButtonDisabled} showDocument={showDocument} messages={messages} setMessages={setMessages} />
      </Card>
    </>
  )
}


