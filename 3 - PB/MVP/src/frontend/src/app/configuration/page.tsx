import { getConfigurationOptions } from "@/lib/actions";
import { ConfigurationForm } from "./configuration-form";

export default async function Configuration() {

    const configurationOptions = await getConfigurationOptions()

    return (
        <ConfigurationForm configurationOptions={configurationOptions} />
    )
}