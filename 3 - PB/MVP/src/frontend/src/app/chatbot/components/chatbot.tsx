
import { Separator } from "@/components/ui/separator"
import { ScrollArea } from '@/components/ui/scroll-area';
import { ChatContent } from "@/app/chatbot/components/chat-content"
import { ChatHeader } from "./chat-header"
import { SWEetCodeLogo } from "@/components/sweetcode-logo"

import { Chat } from "@/types/types"

import { getChatMessages } from "@/lib/actions"
import ChatFooter from "./chat-footer";

interface ChatbotProps {
    chatId?: number
}

export default async function Chatbot({ chatId }: ChatbotProps) {

    let chat = null as Chat | null
    if (chatId !== undefined) {
        chat = await getChatMessages(chatId)
    }

    return (
        <div className="flex h-full flex-col">
            <ChatHeader chatTitle={chat?.title} chatId={chatId} isChatSelected={!!chat} />
            <Separator />
            <div className="h-full flex flex-1 flex-col justify-between overflow-auto">
                {chat ? (
                    <div className="flex-1 whitespace-pre-wrap text-sm overflow-auto">
                        <ScrollArea className="h-full">
                            <div className="p-4 pb-0">
                                <ChatContent messages={chat?.messages} />
                            </div>
                        </ScrollArea>
                    </div>
                ) : (
                    <div className="h-full flex flex-col items-center justify-center select-none animate-show-in" >
                        <SWEetCodeLogo className="w-20 h-20" />
                        <h4 className="text-lg font-bold" >Hey, how can I help you?</h4>
                    </div>
                )}
            </div>
            <ChatFooter chatId={chatId} />
        </div>
    )
}
