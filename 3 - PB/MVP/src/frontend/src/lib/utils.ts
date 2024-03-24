import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"
import { ALLOWED_FILE_TYPES } from "@/constants/constants"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function validateFileType(file: File) {
  return ALLOWED_FILE_TYPES.some((allowedFileType) => allowedFileType.type === file.type)
}
