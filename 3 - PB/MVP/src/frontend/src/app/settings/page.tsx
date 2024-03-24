import { Separator } from "@/components/ui/separator"
import { SettingsConfigurationForm } from "@/app/settings/configuration-form"
import { getConfiguration, getConfigurationOptions } from "@/lib/actions"
  

export default async function SettingsProfilePage() {
  const currentConfiguration = await getConfiguration()
  const configurationOptions = await getConfigurationOptions()

  return (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-medium">Configuration</h3>
        <p className="text-sm text-muted-foreground">
          Choose your configuration.
        </p>
      </div>
      <Separator />
      <SettingsConfigurationForm currentConfiguration={currentConfiguration} configurationOptions={configurationOptions} />
    </div>
  )
}
