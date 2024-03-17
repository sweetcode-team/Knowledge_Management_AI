import { formatDistanceToNow } from "date-fns";

import { cn } from "@/lib/utils"
import { ScrollArea } from "@/components/ui/scroll-area"

import { useChat } from "../use-chat";
import { Chat } from "../data";

interface ChatListProps {
  items: Chat[]
}

export function ChatList({ items }: ChatListProps) {
  const [chat, setChat] = useChat()

  return (
    <ScrollArea>
      <div className="flex flex-col gap-2 p-4 pt-0">
        {items.map((item) => (
          <button
            key={item.id}
            className={cn(
              "flex flex-col items-start gap-2 rounded-lg border p-3 text-left text-sm transition-all hover:bg-accent",
              chat.selected === item.id && "bg-muted"
            )}
            onClick={() =>
              setChat({
                ...chat,
                selected: item.id,
              })
            }
          >
            <div className="flex w-full flex-col gap-1">
              <div className="flex items-center gap-x-2">
                <div className="flex items-center gap-x-2">
                  {!item.read && (
                    <span className="flex h-2 w-2 rounded-full bg-blue-600" />
                  )}
                  <div className="font-semibold line-clamp-1">{item.name}</div>
                </div>
                <div
                  className={cn(
                    "ml-auto text-xs line-clamp-1",
                    chat.selected === item.id
                      ? "text-foreground"
                      : "text-muted-foreground"
                  )}
                >
                  {formatDistanceToNow(new Date(item.date), {
                    addSuffix: true,
                  })}
                </div>
              </div>
            </div>
            <div className="line-clamp-2 text-xs text-muted-foreground">
              {item.text.substring(0, 300)}
            </div>
          </button>
        ))}
      </div>
    </ScrollArea>
  )
}