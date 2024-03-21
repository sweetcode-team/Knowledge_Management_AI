"use client"
import * as React from "react"
import { ReactNode } from 'react';

import { NAV_ITEMS } from '@/constants/constants';

import { Logo } from "@/components/logo"
import { Nav } from "@/components/nav"
import { cn } from "@/lib/utils"
import { Separator } from "@/components/ui/separator"
import { TooltipProvider } from "@/components/ui/tooltip"
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable"

import Header from "@/components/header"
import { usePathname } from "next/navigation";
import { NavItem } from "@/types/navItem";

interface ResizableLayoutProps {
    defaultLayout: number[] | undefined
    defaultCollapsed?: boolean
    navCollapsedSize: number,
    children: ReactNode
}

export function ResizableLayout({
    defaultLayout = [15, 85],
    defaultCollapsed = false,
    navCollapsedSize,
    children,
}: ResizableLayoutProps) {
    const [isCollapsed, setIsCollapsed] = React.useState(defaultCollapsed)

    const pathname = "/" + usePathname().split("/")[1];

    const navItems: NavItem[] = NAV_ITEMS

    const title = navItems.find((item) => item.path === pathname)?.title

    return (
        <TooltipProvider delayDuration={0}>
            <ResizablePanelGroup
                direction="horizontal"
                onLayout={(sizes: number[]) => {
                    document.cookie = `react-resizable-panels:layout=${JSON.stringify(
                        sizes
                    )}`
                }}
                className="items-stretch"
            >
                <ResizablePanel
                    defaultSize={defaultLayout[0]}
                    collapsedSize={navCollapsedSize}
                    collapsible={true}
                    minSize={15}
                    maxSize={20}
                    onCollapse={(collapsed) => {
                        setIsCollapsed(collapsed)
                        document.cookie = `react-resizable-panels:collapsed=${JSON.stringify(
                            collapsed
                        )}`
                    }}
                    className={cn("flex flex-col", isCollapsed && "min-w-[50px] transition-all duration-300 ease-in-out overflow-hidden")}
                >
                    <div className={cn("flex h-[52px] items-center justify-center", isCollapsed ? 'h-[52px]' : 'px-2')}>
                        <Logo isCollapsed={isCollapsed} />
                    </div>
                    <Separator />
                    <Nav
                        isCollapsed={isCollapsed}
                        links={navItems} />
                </ResizablePanel>
                <ResizableHandle withHandle />
                <ResizablePanel defaultSize={defaultLayout[1]}>
                    <Header title={title} />
                    <main className="h-[calc(100vh-52px)] w-[100%] relative overflow-hidden">
                        {children}
                    </main>
                </ResizablePanel>
            </ResizablePanelGroup>
        </TooltipProvider>
    )
}
