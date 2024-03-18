import { cookies } from "next/headers"

import { Chatbot } from "@/app/chatbot/components/chatbot"
import { Chat } from "./data"
// import { chats } from "@/app/chatbot/data"

export default function ChatPage() {
  const chatLayout = cookies().get("react-resizable-panels:chat-layout")

  const defaultLayout = chatLayout ? JSON.parse(chatLayout.value) : undefined

  const chats: Chat[] = [
    {
      id: "6c84fb90-12c4-11e1-840d-7b25c5ee775a",
      name: "William Smith",
      email: "williamsmith@example.com",
      subject: "Meeting Tomorrow",
      text: "Hi, let's have a meeting tomorrow to discuss the project. I've been reviewing the project details and have some ideas I'd like to share. It's crucial that we align on our next steps to ensure the project's success.\n\nPlease come prepared with any questions or insights you may have. Looking forward to our meeting!\n\nBest regards, William",
      date: "2023-10-22T09:00:00",
      read: true,
      labels: ["meeting", "work", "important"],
    },
    {
      id: "110e8400-e29b-11d4-a716-446655440000",
      name: "Alice Smith",
      email: "alicesmith@example.com",
      subject: "Re: Project Update",
      text: "Thank you for the project update. It looks great! I've gone through the report, and the progress is impressive. The team has done a fantastic job, and I appreciate the hard work everyone has put in.\n\nI have a few minor suggestions that I'll include in the attached document.\n\nLet's discuss these during our next meeting. Keep up the excellent work!\n\nBest regards, Alice",
      date: "2023-10-22T10:30:00",
      read: true,
      labels: ["work", "important"],
    },
  ]

  return (
    <Chatbot
      defaultLayout={defaultLayout}
      chats={chats}
    />
  )
}
