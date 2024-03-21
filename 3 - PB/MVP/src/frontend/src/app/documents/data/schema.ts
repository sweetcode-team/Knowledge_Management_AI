import { z } from "zod"

export const documentSchema = z.object({
  id: z.string(),
  size: z.number(),
  status: z.string(),
  type: z.string(),
  uploadDate: z.string(),
})

export type Document = z.infer<typeof documentSchema>
