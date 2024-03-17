"use client"

import * as React from "react"

import { cn } from "@/lib/utils"
import { SparklesIcon } from "lucide-react"

interface LogoProps {
  isCollapsed: boolean
}

export function Logo({
  isCollapsed,
}: LogoProps) {
  return (
    <div
      className={cn(
        "flex items-center gap-2 [&>span]:line-clamp-1 [&>span]:items-center",
        isCollapsed &&
        "flex h-9 w-9 shrink-0 items-center justify-center p-0 [&>span]:w-auto [&>h1]:hidden"
      )}
    >
      <span><SparklesIcon className="w-6 h-6 fill-current" /></span>
      <h1 className="p-0 border-0 text-2xl">kmai</h1>
    </div>
  )
}
