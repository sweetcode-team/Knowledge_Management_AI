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
import { NavItem } from "@/types/navItem"

interface NavProps {
  isCollapsed: boolean
  links: NavItem[]
}

export function Nav({ links, isCollapsed }: NavProps) {
  const pathname = "/" + usePathname().split("/")[1];

  const label = "Prova"

  return (
    <div
      data-collapsed={isCollapsed}
      className="group flex flex-col gap-4 py-2 data-[collapsed=true]:py-2"
    >
      <nav className="grid gap-1 px-2 group-[[data-collapsed=true]]:justify-center group-[[data-collapsed=true]]:px-2">
        {links.map((link, index) =>
          isCollapsed ? (
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
                  <link.icon className="h-4 w-4" />
                  <span className="sr-only">{link.title}</span>
                </Link>
              </TooltipTrigger>
              <TooltipContent side="right" className="flex items-center gap-4">
                {link.title}
                {/* {label && (
                  <span className="ml-auto text-muted-foreground">
                    {label}
                  </span>
                )} */}
              </TooltipContent>
            </Tooltip>
          ) : (
            <Link
              key={index}
              href={link.path}
              className={cn(
                buttonVariants({ variant: pathname === link.path ? "default" : "ghost" as any, size: "sm" }),
                pathname === link.path &&
                "dark:bg-muted dark:text-white dark:hover:bg-muted dark:hover:text-white",
                "justify-start"
              )}
            >
              <link.icon className="mr-2 h-4 w-4" />
              {link.title}
              {/* {label && (
                <span
                  className={cn(
                    "ml-auto",
                    pathname === link.path &&
                    "text-background dark:text-white"
                  )}
                >
                  {label}
                </span>
              )} */}
            </Link>
          )
        )}
      </nav>
    </div>
  )
}
