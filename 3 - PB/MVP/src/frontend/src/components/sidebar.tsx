"use client"
import * as React from "react"
import {
    FolderOpenIcon,
    LayoutDashboardIcon,
    MessageSquareTextIcon,
    SettingsIcon,
} from "lucide-react"

import { Nav } from "@/app/chatbot/components/nav"
import { useMail } from "@/app/chatbot/use-chat"
import { cn } from "@/lib/utils"
import { Separator } from "@/components/ui/separator"
import { ResizablePanel } from "@/components/ui/resizable"


interface MailProps {
    defaultLayout: number[] | undefined
    defaultCollapsed?: boolean
    navCollapsedSize: number
}

export function Sidebar({
    defaultLayout = [265, 440, 655],
    defaultCollapsed = false,
    navCollapsedSize,
}: MailProps) {

    const [isCollapsed, setIsCollapsed] = React.useState(defaultCollapsed)
    const [mail] = useMail()

    return (
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
            {/* <div className={cn("flex h-[52px] items-center justify-center", isCollapsed ? 'h-[52px]' : 'px-2')}>
                <AccountSwitcher isCollapsed={isCollapsed} accounts={accounts} />
            </div> */}
            <Separator />
            <Nav
                isCollapsed={isCollapsed}
                links={[
                    {
                        title: "Dashboard",
                        label: "",
                        icon: LayoutDashboardIcon,
                        variant: "default",
                    },
                    {
                        title: "Chatbot",
                        label: "",
                        icon: MessageSquareTextIcon,
                        variant: "ghost",
                    },
                    {
                        title: "Documents",
                        label: "",
                        icon: FolderOpenIcon,
                        variant: "ghost",
                    },
                ]}
            />
            <div className="last:mt-0">
                <Nav
                    isCollapsed={isCollapsed}
                    links={[
                        {
                            title: "Settings",
                            label: "",
                            icon: SettingsIcon,
                            variant: "secondary",
                        },
                    ]}
                />
            </div>
        </ResizablePanel>
    )
}