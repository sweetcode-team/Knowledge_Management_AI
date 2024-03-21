"use client"
import * as React from "react"

import { Message } from "@/app/chatbot/data"
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
      <div className="space-y-4 w-full pb-4">
        {
          messages?.length === 0 ?
            "Nessun messaggio presente."
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


