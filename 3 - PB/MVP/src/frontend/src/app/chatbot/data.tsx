export type Chat = {
  id: string
  title: string
  messages: Message[]
}

export type Message = {
  role: string
  content: string
  timestamp: string
  relevantDocuments: string[]
}