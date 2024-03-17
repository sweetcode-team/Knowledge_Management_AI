import React from 'react';
import  { MessageContentProps } from '@/app/chatbot/components/message-content';
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils"
import { Copy } from "lucide-react"

type Message = {
    role: string;
    content: JSX.Element;
    timestamp: string;
  };
  
  type CardContentProps = {
    messages: Message[];
    copyToClipboard: (text: string) => void;
  };
  
  export const CardContent: React.FC<CardContentProps> = ({ messages, copyToClipboard }) => {
  return (
    <div className="space-y-4">
      {messages.map((message, index) => (
        <div key={index} className="flex flex-col items-start space-y-2">
          <div
            className={cn(
              "flex w-max max-w-[75%] flex-col rounded-lg px-3 py-2 text-sm relative",
              message.role === "user"
                ? "ml-auto bg-primary"
                : "bg-muted"
            )}
            style={{wordWrap: "break-word"}}
          >
            <p className={message.role === "user"
          ? "text-primary-foreground"
          : "text-muted-foreground"
          }> {message.content}</p>
            <div className={cn(
              "absolute top-0 mt-1",
              message.role === "user"
                ? "left-[-48px]"
                : "right-[-48px]"
            )}>
              <Button
                size="icon"
                variant="ghost"
                className="p-0.5 text- "
                onClick={() => {
                  let textToCopy = '';
                  if (React.isValidElement<MessageContentProps>(message.content)) {
                    textToCopy = message.content.props.text;
                  }
                  copyToClipboard(textToCopy);
                }}
              >
                <Copy className="h-3 w-3" />
                <span className="sr-only">Copy</span>
              </Button>
            </div>
          </div>
          <div className={cn(
            "flex items-center w-full mt-2 ml-1.5",
            message.role === "user"
              ? "justify-end ml-[-6px]"
              : "justify-start"
          )}>
            <p className="text-xs text-muted-foreground">{message.timestamp}</p>
          </div>
        </div>
      ))}
    </div>
  );
};
