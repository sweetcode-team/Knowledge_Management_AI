import Chatbot from "../components/chatbot";

export default async function ChatPage({ params }: { params: { chatId: number } }) {
    return (
        <div className="flex h-full flex-col">
            <Chatbot chatId={params.chatId} />
        </div >
    )
}
