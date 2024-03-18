import React, { SetStateAction, Dispatch } from 'react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input"
import { Mic, Square, Play, Pause } from "lucide-react"
import { Send } from "lucide-react"
import MessageContent from '@/app/chatbot/components/message-content';

type Message = {
  role: string;
  content: JSX.Element;
  timestamp: string;
};

type CardFooterProps = {
  input: string;
  setInput: Dispatch<SetStateAction<string>>;
  isRecording: boolean;
  setIsRecording: Dispatch<SetStateAction<boolean>>;
  startRecording: () => void;
  stopRecording: () => void;
  isPaused: boolean;
  setIsPaused: Dispatch<SetStateAction<boolean>>;
  isMicClicked: boolean;
  setIsMicClicked: Dispatch<SetStateAction<boolean>>;
  isButtonDisabled: boolean;
  setIsButtonDisabled: Dispatch<SetStateAction<boolean>>;
  showDocument: () => void;
  messages: Message[];
  setMessages: Dispatch<SetStateAction<Message[]>>;
};

export const CardFooter: React.FC<CardFooterProps> = ({ input, setInput, isRecording, setIsRecording, startRecording, stopRecording, isPaused, setIsPaused, isMicClicked, setIsMicClicked, isButtonDisabled, setIsButtonDisabled, showDocument, messages, setMessages }) => {
  return (
    <form
      onSubmit={(event) => {
        event.preventDefault()
        if (input.trim().length === 0) return
        const timestamp = new Date().toLocaleTimeString();
        setMessages([
          ...messages,
          {
            role: "user",
            content: <MessageContent text={input} onButtonClick={showDocument} role="user"></MessageContent>,
            timestamp: timestamp,
          },
        ])
        setInput("")
      }}
      className="flex w-full items-center space-x-2"
    >
      <Button 
        type="button"
        size="icon"
        variant={!isRecording ? "default" : "destructive"}
        onClick={() => {
          setIsMicClicked(false);
          if (isRecording && !isPaused) {
            stopRecording();
          } else {
            startRecording();
          }
        }}
        disabled={input.trim().length === 0}
      >
        {!isRecording ? <Play className="h-4 w-4" /> : <Pause className="h-4 w-4" />}
        <span className="sr-only">{isRecording ? "Resume voice input" : "Pause voice input"}</span>
      </Button>
      <Button 
        type="button"
        size="icon"
        variant={isRecording && !isPaused ? "destructive" : "default"}
        onClick={() => {
          setIsMicClicked(true);
          if (isRecording && !isPaused) {
            stopRecording();
          } else {
            setInput("");
            startRecording();
          }
        }}
      >
        {isRecording && !isPaused ? <Square className="h-4 w-4" /> : <Mic className="h-4 w-4" />}
        <span className="sr-only">{isRecording ? "Stop voice input" : "Start voice input"}</span>
      </Button>
      <Input
        id="message"
        placeholder="Type your message..."
        className="flex-1"
        autoComplete="off"
        value={input}
        onChange={(event) => setInput(event.target.value)}
      />
        <Button type="submit" size="icon" disabled={input.trim().length === 0 || isRecording || isButtonDisabled}>
          <Send className="h-4 w-4" />
          <span className="sr-only">Send</span>
        </Button>
    </form>
  );
};
