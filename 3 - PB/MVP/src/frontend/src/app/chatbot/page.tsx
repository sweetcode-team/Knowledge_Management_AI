import { cookies } from "next/headers"

import { Chatbot } from "@/app/chatbot/components/chatbot"
import { getChats } from "@/lib/actions";

export default async function ChatPage() {
    const chatLayout = cookies().get("react-resizable-panels:chat-layout")
    const chatsPreview = await getChats()

    const defaultLayout = chatLayout ? JSON.parse(chatLayout.value) : undefined

    return (
        <Chatbot
            defaultLayout={defaultLayout}
            chats={chatsPreview}
        />
    )
}
