import type { Metadata } from "next";
import { Poppins } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/components/theme-provider"
import { Toaster } from "@/components/ui/toaster";
import { cn } from "@/lib/utils"

import { ResizableLayout } from "@/components/resizable-layout"

import { cookies } from "next/headers"
import { ModeToggle } from "@/components/ui/toggle-mode";

const poppins = Poppins({ weight: "400", subsets: ["devanagari"] });

export const metadata: Metadata = {
  title: "Kmai",
  description: "Knowledge Management AI",
  authors: [{ name: "SWEetCode", url: "https://sweetcode-team.github.io/" }]
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

  const layout = cookies().get("react-resizable-panels:layout")
  const collapsed = cookies().get("react-resizable-panels:collapsed")

  const defaultLayout = layout ? JSON.parse(layout.value) : undefined
  const defaultCollapsed = collapsed ? JSON.parse(collapsed.value) : undefined

  return (
    <html lang="it">
      <body className={cn("h-screen", poppins.className)}>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <ResizableLayout
            navCollapsedSize={4}
            defaultLayout={defaultLayout}
            defaultCollapsed={defaultCollapsed}
          >
            {children}
          </ResizableLayout>
        </ThemeProvider>
        <Toaster />
      </body>
    </html>
  );
}
