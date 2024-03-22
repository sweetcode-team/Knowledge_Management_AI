import { Metadata } from "next"

import { SidebarNav } from "@/app/settings/components/sidebar-nav"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Configuration } from "@/types/types"

export const metadata: Metadata = {
  title: "KMAI - Settings",
  description: "Settings page for KMAI.",
}

const sidebarNavItems = [
  {
    title: "Configuration",
    href: "/settings",
  },
  {
    title: "Appearance",
    href: "/settings/appearance",
  }
]

interface SettingsLayoutProps {
  children: React.ReactNode
}

export default function SettingsLayout({ children }: SettingsLayoutProps) {

  return (
    <div className="px-4 h-full pt-4">
      <div className="flex flex-col h-full space-y-8 lg:flex-row lg:space-x-12 lg:space-y-0">
        <aside className="lg:w-1/5">
          <SidebarNav items={sidebarNavItems} />
        </aside>
        <ScrollArea className="h-full w-full">
          <div className="w-full h-full flex-1 px-4 pb-8">{children}</div>
        </ScrollArea>
      </div>
    </div>
  )
}
