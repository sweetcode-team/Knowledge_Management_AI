import {
    MessageSquarePlusIcon,
} from "lucide-react"

import { ChatList } from "@/app/chatbot/components/chat-list"
import { Separator } from "@/components/ui/separator"
import { TooltipProvider } from "@/components/ui/tooltip"
import { Button } from "@/components/ui/button"
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable"

import {
    Tooltip,
    TooltipContent,
    TooltipTrigger,
} from "@/components/ui/tooltip"
import { getChats } from "@/lib/actions"
import Link from "next/link"

export default async function ChatbotLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    const chatPreviews = await getChats()

    const defaultLayout = [30, 70]

    return (
        <TooltipProvider delayDuration={0}>
            <ResizablePanelGroup
                direction="horizontal"
                className="items-stretch"
            >
                <ResizablePanel
                    defaultSize={defaultLayout[0]}
                    minSize={25}
                    maxSize={40}
                    className="flex flex-col"
                >
                    <div className="flex items-center px-4 py-2">
                        <h3 className="text-xl font-bold">Chat list</h3>
                        <Tooltip>
                            <TooltipTrigger asChild>
                                <Button asChild
                                    variant="info"
                                    className="ml-auto"
                                    size="icon"
                                >
                                    <Link
                                        href="/chatbot"
                                    >
                                        <MessageSquarePlusIcon className="h-4 w-4" />
                                        <span className="sr-only">New Chat</span>
                                    </Link>
                                </Button>
                            </TooltipTrigger>
                            <TooltipContent>New Chat</TooltipContent>
                        </Tooltip>
                    </div>
                    <Separator />
                    <ChatList chatPreviews={chatPreviews} />
                </ResizablePanel>
                <ResizableHandle withHandle />
                <ResizablePanel
                    defaultSize={defaultLayout[1]}
                >
                    {children}
                </ResizablePanel>
            </ResizablePanelGroup>
        </TooltipProvider>
    )
}
