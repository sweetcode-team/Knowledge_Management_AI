import { z } from "zod"

export const documentSchema = z.object({
  id: z.string(),
  dimension: z.number(),
  status: z.string(),
  type: z.string(),
  uploadTime: z.string(),
})

export type Document = z.infer<typeof documentSchema>
