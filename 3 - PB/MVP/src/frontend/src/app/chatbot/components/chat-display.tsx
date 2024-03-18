import {
  SquarePenIcon,
  TrashIcon,
} from "lucide-react"
import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import { Separator } from "@/components/ui/separator"
import { Switch } from "@/components/ui/switch"
import { Textarea } from "@/components/ui/textarea"
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import { Chat } from "@/app/chatbot/data"
import { ScrollArea } from '@/components/ui/scroll-area';

interface ChatDisplayProps {
  chat: Chat | null
}

export function ChatDisplay({ chat }: ChatDisplayProps) {
  const today = new Date()

  return (
    <div className="flex h-full flex-col">
      <div className="flex items-center py-2 px-4">
        <div className="flex items-center">
          <h3 className="border-0 p-0 line-clamp-1 text-xl font-bold mr-2">Titolo chat</h3>
        </div>
        <div className="ml-auto flex items-center gap-2">
          <Tooltip>
            <TooltipTrigger asChild>
              <Button variant="secondary" size="icon" disabled={!chat}>
                <SquarePenIcon className="h-4 w-4" />
                <span className="sr-only">Rename chat</span>
              </Button>
            </TooltipTrigger>
            <TooltipContent>Rename chat</TooltipContent>
          </Tooltip>
          <Tooltip>
            <TooltipTrigger asChild>
              <Button variant="danger" size="icon" disabled={!chat}>
                <TrashIcon className="h-4 w-4" />
                <span className="sr-only">Delete chat</span>
              </Button>
            </TooltipTrigger>
            <TooltipContent>Delete chat</TooltipContent>
          </Tooltip>
        </div>
      </div>
      <Separator />
      {chat ? (
        <div className="h-full flex flex-1 flex-col justify-between overflow-auto">
          <div className="flex-1 whitespace-pre-wrap text-sm overflow-auto">
            <ScrollArea className="h-full">
              <div className="p-4">
                {chat.text}
              </div>
            </ScrollArea>
          </div>
          <div>
            <Separator className="mt-auto" />
            <form className="p-4">
              <div className="grid gap-4 max-h-full">
                <div className="flex items-center">
                  <Label
                    htmlFor="mute"
                    className="flex items-center gap-2 text-xs font-normal"
                  >
                    <Switch id="mute" aria-label="Mute thread" /> Mute this
                    thread
                  </Label>
                  <Button
                    onClick={(e) => e.preventDefault()}
                    size="sm"
                    className="ml-auto"
                  >
                    Send
                  </Button>
                </div>
                <Textarea
                  className="p-4"
                  placeholder={`Reply ${chat.name}...`}
                />
              </div>
            </form>
          </div>
        </div>
      ) : (
        <div className="p-12 text-center text-muted-foreground">
          No chat selected.
        </div>
      )}
    </div>
  )
}
