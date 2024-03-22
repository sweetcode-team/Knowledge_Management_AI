import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

const ALLOWED_FILE_TYPES = ['application/pdf', 'application/msword']
export function validateFileType(file: File) {
  return ALLOWED_FILE_TYPES.includes(file.type)
}
