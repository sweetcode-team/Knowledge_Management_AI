import { Separator } from "@/components/ui/separator"
import { ConfigurationForm } from "@/app/settings/configuration-form"

export default function SettingsProfilePage() {
  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-medium">Configuration</h3>
        <p className="text-sm text-muted-foreground">
          Choose your configuration.
        </p>
      </div>
      <Separator />
      <ConfigurationForm />
    </div>
  )
}
