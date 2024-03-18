import { atom, useAtom } from "jotai"

import { Chat, chats } from "@/app/chatbot/data"

type Config = {
  selected: Chat["id"] | null
}

const configAtom = atom<Config>({
  selected: null,
})

export function useChat() {
  return useAtom(configAtom)
}
