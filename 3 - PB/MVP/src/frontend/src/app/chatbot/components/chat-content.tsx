"use client"
import * as React from "react"

import { Message } from "@/types/types"
import { MessageCard } from "./message-card";
import { useEffect, useRef } from 'react';

interface ChatContentProps {
  messages?: Message[];
}

export function ChatContent({ messages }: ChatContentProps) {
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ block: "end", behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom()
  }, [messages]);

  return (
    <>
      <div className="h-full w-full space-y-4 pb-4">
        {
          messages===undefined || messages?.length === 0 ?
            <div className="flex text-sm h-full items-center justify-center pt-8">
              No messages yet.
            </div>
            :
            messages?.map((message, index) => (
              <MessageCard key={index} message={message} />
            ))
        }
      </div>
      <div ref={messagesEndRef} />
    </>
  )
}


