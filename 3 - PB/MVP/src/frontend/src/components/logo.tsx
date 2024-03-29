"use client"

import * as React from "react"

import { cn } from "@/lib/utils"
import { SWEetCodeLogo } from "@/components/sweetcode-logo"

interface LogoProps {
  isCollapsed: boolean
}

export function Logo({
  isCollapsed,
}: LogoProps) {
  return (
    <div
      className={cn(
        "flex w-full items-center justify-center gap-2 [&>span]:line-clamp-1 [&>span]:items-center [&>h1]:hidden sm:[&>h1]:block",
        isCollapsed &&
        "flex h-9 w-9 shrink-0 items-center justify-center p-0 [&>span]:w-auto [&>h1]:hidden sm:[&>h1]:hidden"
      )}
    >
      <span>
        <SWEetCodeLogo />
      </span>
      {/* <span><SparklesIcon className="w-6 h-6 fill-current" /></span> */}
      <h1 className="p-0 border-0 text-2xl">kmai</h1>
    </div>
  )
}
