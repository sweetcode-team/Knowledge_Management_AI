import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip"
import { SquarePenIcon, TrashIcon } from "lucide-react"
import { useState } from "react";

interface ChatHeaderProps {
    chatTitle?: string,
    isChatSelected: boolean,
}

export function ChatHeader({ chatTitle, isChatSelected }: ChatHeaderProps) {
    const [isBeingRenamed, setIsBeingRenamed] = useState(false);
    const [newChatTitle, setNewChatTitle] = useState(chatTitle || "");

    const switchRenameMode = () => {
        console.log(isBeingRenamed)
        setIsBeingRenamed(!isBeingRenamed)
    }

    const handleRename = () => {
        if (newChatTitle === "" || newChatTitle === chatTitle) {
            return;
        }
        setIsBeingRenamed(false)
        console.log(newChatTitle)
    };

    return (
        <div className="flex items-center py-2 px-4">
            {isBeingRenamed ? (
                <Input
                    type="text"
                    className="p-0 line-clamp-1 text-xl font-bold mr-2 pl-2"
                    value={newChatTitle}
                    onChange={(e) => setNewChatTitle(e.target.value)}
                    autoFocus
                    onBlur={() => {
                        setIsBeingRenamed(false)
                    }}
                />
            ) : (
                <h3 className="border-0 p-0 line-clamp-1 text-xl font-bold mr-2 pl-2">{chatTitle ? chatTitle : "New Chat"}</h3>
            )}
            <div className="ml-auto flex gap-2">
                <Tooltip>
                    <TooltipTrigger asChild>
                        <Button
                            variant={isBeingRenamed ? "safe" : "secondary"}
                            size="icon"
                            disabled={!isChatSelected || chatTitle === ""}
                            onClick={() => {
                                if (isBeingRenamed) {
                                    handleRename();
                                } else {
                                    setIsBeingRenamed(true);
                                }
                            }}
                        >
                            <SquarePenIcon className="h-4 w-4" />
                            <span className="sr-only">Rename chat</span>
                        </Button>
                    </TooltipTrigger>
                    <TooltipContent>Rename chat</TooltipContent>
                </Tooltip>
                <Tooltip>
                    <TooltipTrigger asChild>
                        <Button variant="danger" size="icon" disabled={!isChatSelected} onClick={() => { }}>
                            <TrashIcon className="h-4 w-4" />
                            <span className="sr-only">Delete chat</span>
                        </Button>
                    </TooltipTrigger>
                    <TooltipContent>Delete chat</TooltipContent>
                </Tooltip>
            </div>
        </div>
    )
}