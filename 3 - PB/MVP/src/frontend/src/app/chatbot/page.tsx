import { cookies } from "next/headers"

import { Chatbot } from "@/app/chatbot/components/chatbot"
import { chats } from "@/app/chatbot/data"

export default function ChatPage() {
  const chatLayout = cookies().get("react-resizable-panels:chat-layout")

  const defaultLayout = chatLayout ? JSON.parse(chatLayout.value) : undefined

  return (
    <Chatbot
      defaultLayout={defaultLayout}
      chats={chats}
      
    />
  )
}
