import { cookies } from "next/headers"

import { Chatbot } from "@/app/chatbot/components/chatbot"
import {Chat, ChatPreview, Message} from "@/types/types";
// import { chats } from "@/app/chatbot/data"

async function getChats(id: string = ""):Promise<ChatPreview[]> {
    if (id === "") {
        const result = await fetch("http://localhost:4000/getChats", { cache: 'no-store' })
        return result.json()
    }
    const result = await fetch(`http://localhost:4000/getChats/${id}`, { cache: 'no-store' })
    return result.json()
}

export default async function ChatPage() {
    const chatLayout = cookies().get("react-resizable-panels:chat-layout")
    const chatsPreview: ChatPreview[] = await getChats()

    const defaultLayout = chatLayout ? JSON.parse(chatLayout.value) : undefined

    return (
        <Chatbot
            defaultLayout={defaultLayout}
            chats={chatsPreview}
        />
    )
}
