import { ArrowRightIcon, LucideIcon } from "lucide-react";
import { Button } from "./ui/button";
import Link from "next/link";

interface ActionButtonProps {
    text: string,
    children: React.ReactNode
    path: string
}

export function ActionButton({
    text,
    children,
    path
}: ActionButtonProps) {
    return (
        <Button asChild variant={"outline"} className="rounded-lg h-12 p-0">
            <Link href={path}
                className="flex h-full items-center space-x-4 p-2 [&>svg]:hover:text-foreground [&>svg]:focus:text-foreground"
            >
                <div className="bg-info text-info-foreground p-1.5 rounded-md">
                    {children}
                </div>
                <div className="font-bold">
                    {text}
                </div>
                <ArrowRightIcon className="h-4 w-4 text-border" />
            </Link>
        </Button>
    );
}