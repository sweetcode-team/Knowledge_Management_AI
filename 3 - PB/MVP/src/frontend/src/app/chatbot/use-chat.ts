import { atom, useAtom } from "jotai"

import { Chat } from "@/types/types"

type Config = {
  selected: Chat["id"] | null
}

const configAtom = atom<Config>({
  selected: null,
})

export function useChat() {
  return useAtom(configAtom)
}
