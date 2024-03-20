import { cookies } from "next/headers"

import { Chatbot } from "@/app/chatbot/components/chatbot"
import { Chat, Message } from "./data"
// import { chats } from "@/app/chatbot/data"

export default function ChatPage() {
  const chatLayout = cookies().get("react-resizable-panels:chat-layout")

  const defaultLayout = chatLayout ? JSON.parse(chatLayout.value) : undefined

  const chats: Chat[] = [
    {
      id: "6c84fb90-12c4-11eqrhqee1-840d-7b25c5ee775a",
      title: "William Smith",
      messages: [
        {
          role: "user",
          content: "Hello",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "bot",
          content: "Hello, how can I help you?",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Documenfssf.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "user",
          content: "I would like to book an appointment",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx1gr463.docx"
          ]
        },
        {
          role: "bot",
          content: "Sure, when would you like to book the appointment?",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Docxvf3425.docx",
            "Docccc99.pdf"
          ]
        },
        {
          role: "user",
          content: "Tomorrow",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "bot",
          content: "What time?",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "user",
          content: "9am",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
      ] as Message[],
    },
    {
      id: "6c84f2562b90-12c4-11eqrhqee1-840d-7b25c5ee775a",
      title: "Alice Smith",
      messages: [
        {
          role: "user",
          content: "Hello",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "bot",
          content: "Hello, how can I help you?",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Documenfssf.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "user",
          content: "I would like to book an appointment",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx1gr463.docx"
          ]
        },
        {
          role: "bot",
          content: "Sure, when would you like to book the appointment?",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Docxvf3425.docx",
            "Docccc99.pdf"
          ]
        },
        {
          role: "user",
          content: "Tomorrow",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "bot",
          content: "What time?",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
        {
          role: "user",
          content: "11am",
          timestamp: "2023-10-22T09:00:00",
          relevantDocuments: [
            "Document1.pdf",
            "Docx123.docx"
          ]
        },
      ] as Message[],
    }
  ]

  return (
    <Chatbot
      defaultLayout={defaultLayout}
      chats={chats}
    />
  )
}
