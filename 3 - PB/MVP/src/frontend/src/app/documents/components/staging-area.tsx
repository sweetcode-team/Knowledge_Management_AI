import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { CircleSlashIcon, FolderUpIcon } from "lucide-react"

export function StagingArea() {
    return (
        <>
            {/* TODO: Staging area */}
            <div className="h-32">

            </div>
            <div className="space-x-2">
                <Button variant="secondary" className="space-x-4">
                    <div className="font-bold">
                        Cancel upload
                    </div>
                    <CircleSlashIcon className="w-5 h-5" />
                </Button>
                <Button variant="info" className="space-x-4">
                    <div className="font-bold">
                        Upload documents
                    </div>
                    <FolderUpIcon className="w-5 h-5" />
                </Button>
            </div>
        </>
    )
}