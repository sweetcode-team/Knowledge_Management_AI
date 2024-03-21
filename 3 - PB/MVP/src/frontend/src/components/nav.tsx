"use client"

import Link from "next/link"
import { LucideIcon } from "lucide-react"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"

import { usePathname } from 'next/navigation';
import { Types } from "@/types/types"

interface NavProps {
  isCollapsed: boolean
  links: Types[]
}

export function Nav({ links, isCollapsed }: NavProps) {
  const pathname = "/" + usePathname().split("/")[1];

  return (
    <div
      data-collapsed={isCollapsed}
      className="group grow flex flex-col gap-4 py-2 data-[collapsed=true]:py-2"
    >
      <nav className="h-full flex flex-col gap-1.5 px-2 group-[[data-collapsed=true]]:justify-center group-[[data-collapsed=true]]:px-2">
        {links.map((link, index) =>
          isCollapsed ? (
            <div key={index} className="last:mt-auto mx-auto">
              <Tooltip key={index} delayDuration={0}>
                <TooltipTrigger asChild>
                  <Link
                    href={link.path}
                    className={cn(
                      buttonVariants({ variant: pathname === link.path ? "default" : "ghost" as any, size: "icon" }),
                      "h-9 w-9",
                      pathname === link.path &&
                      "dark:bg-muted dark:text-muted-foreground dark:hover:bg-muted dark:hover:text-white"
                    )}
                  >
                    <link.icon className="h-5 w-5" />
                    <span className="sr-only">{link.title}</span>
                  </Link>
                </TooltipTrigger>
                <TooltipContent side="right" className="flex items-center gap-4">
                  {link.title}
                </TooltipContent>
              </Tooltip>
            </div>
          ) : (
            <Link
              key={index}
              href={link.path}
              className={cn(
                buttonVariants({ variant: pathname === link.path ? "default" : "ghost" as any, size: "sm" }),
                pathname === link.path &&
                "dark:bg-muted dark:text-white dark:hover:bg-muted dark:hover:text-white",
                "justify-start last:mt-auto"
              )}
            >
              <link.icon className="mr-2 h-5 w-5" />
              {link.title}
            </Link>
          )
        )}
      </nav>
    </div>
  )
}
