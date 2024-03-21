"use client"

import { Separator } from "@/components/ui/separator";

import { zodResolver } from "@hookform/resolvers/zod"
import { useFieldArray, useForm } from "react-hook-form"
import { z } from "zod"

import { Button } from "@/components/ui/button"
import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { toast } from "@/components/ui/use-toast"

import {
    Configuration,
    ConfigurationOperationResponse,
    LLMModel,
    VectorStore,
    DocumentStore,
    EmbeddingsModel,
    ConfigurationOptions
} from "@/types/types"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Card, CardContent, CardDescription, CardFooter, CardHeader } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableRow } from "@/components/ui/table"

import {
    Carousel,
    CarouselContent,
    CarouselItem,
    CarouselNext,
    CarouselPrevious,
} from "@/components/ui/carousel"
import { ScrollArea } from "@/components/ui/scroll-area";

const configurationFormSchema = z.object({
    LLMModel: z.string(),
    vectorStore: z.string(),
    embeddingModel: z.string(),
    documentStore: z.string()
})

type ConfigurationFormValues = z.infer<typeof configurationFormSchema>

export default function Configuration() {
    // const configurationOptions = getConfigurationOptions()

    const configurationOptions = {
        "LLMModel": [{
            "name": "GPT-3.5-turbo",
            "type": "Language Model",
            "costIndicator": "Paid",
            "description": "The GPT-3.5-turbo model is a language model that is capable of answering questions and generating text based on the input it receives.",
            "organization": "OpenAI"
        },
        {
            "name": "LLama",
            "type": "Language Model",
            "costIndicator": "Free",
            "description": "The LLama model is a language model that is capable of answering questions and generating text based on the input it receives.",
            "organization": "Meta"
        },
        {
            "name": "GPT 4",
            "type": "Language Model",
            "costIndicator": "Free",
            "description": "The LLama model is a language model that is capable of answering questions and generating text based on the input it receives.",
            "organization": "Meta"
        },
        {
            "name": "HGMod",
            "type": "Language Model",
            "costIndicator": "Free",
            "description": "The LLama model is a language model that is capable of answering questions and generating text based on the input it receives.",
            "organization": "Meta"
        }
        ],
        "VectorStore": [],
        "DocumentStore": [],
        "EmbeddingsModel": []
    }

    const form = useForm<ConfigurationFormValues>({
        resolver: zodResolver(configurationFormSchema),
        mode: "onChange",
    })

    function onSubmit(data: ConfigurationFormValues) {
        // TODO: setConfiguration(data)
        toast({
            title: "You submitted the following values:",
            description: (
                <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
                    <code className="text-white">{JSON.stringify(data, null, 2)}</code>
                </pre>
            ),
        })
    }

    const LLMModelOptions: LLMModel[] = configurationOptions.LLMModel
    const vectorStoreOptions: VectorStore[] = configurationOptions.VectorStore
    const documentStoreOptions: DocumentStore[] = configurationOptions.DocumentStore
    const embeddingsModelOptions: EmbeddingsModel[] = configurationOptions.EmbeddingsModel

    return (
        <div className="h-full">
            <ScrollArea className="h-full">
                <div className="p-6">
                    <h2 className="border-none">Configuration</h2>
                    <p className="text-muted-foreground">
                        Choose your configuration.
                    </p>
                </div>
                <Separator />
                <Form {...form}>
                    <form onSubmit={form.handleSubmit(onSubmit)} className="w-full space-y-8 p-6">
                        <FormField
                            control={form.control}
                            name="LLMModel"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>LLM Models</FormLabel>
                                    <FormDescription className="pb-4">
                                        Choose the LLM Model that will answer your questions.
                                    </FormDescription>
                                    <FormMessage />
                                    <RadioGroup
                                        asChild
                                        onValueChange={field.onChange}
                                        defaultValue={field.value}
                                    >
                                        <Carousel className="w-[calc(100%-100px)] mx-auto">
                                            <CarouselContent>
                                                {
                                                    LLMModelOptions.map((option) => (
                                                        <CarouselItem key={option.name} className="max-w-72">
                                                            <FormItem>
                                                                <FormLabel className="[&:has([data-state=checked])>div]:border-primary [&:has([data-state=checked])>div]:bg-accent hover:cursor-pointer">
                                                                    <FormControl>
                                                                        <RadioGroupItem value={option.name} className="sr-only" />
                                                                    </FormControl>
                                                                    <Card className="w-fit">
                                                                        <CardHeader>
                                                                            <h2 className="text-xl">{option.name}</h2>
                                                                            <CardDescription>
                                                                                {option.type}
                                                                            </CardDescription>
                                                                        </CardHeader>
                                                                        <CardContent className="py-2 text-pretty">
                                                                            {option.description}
                                                                        </CardContent>
                                                                        <CardFooter className="pt-2">
                                                                            <Table>
                                                                                <TableBody>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Cost</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.costIndicator}</TableCell>
                                                                                    </TableRow>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Organization</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.organization}</TableCell>
                                                                                    </TableRow>
                                                                                </TableBody>
                                                                            </Table>
                                                                        </CardFooter>
                                                                    </Card>
                                                                </FormLabel>
                                                            </FormItem>
                                                        </CarouselItem>
                                                    ))}
                                            </CarouselContent>
                                            <CarouselPrevious />
                                            <CarouselNext />
                                        </Carousel>
                                    </RadioGroup>
                                </FormItem>
                            )}
                        />
                        <Separator />
                        <FormField
                            control={form.control}
                            name="vectorStore"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Vector Stores</FormLabel>
                                    <FormDescription className="pb-4">
                                        Choose the vector store that will store your documents embeddings.
                                    </FormDescription>
                                    <FormMessage />
                                    <RadioGroup
                                        asChild
                                        onValueChange={field.onChange}
                                        defaultValue={field.value}
                                    >
                                        <Carousel className="w-[calc(100%-100px)] mx-auto">
                                            <CarouselContent>
                                                {
                                                    vectorStoreOptions.map((option) => (
                                                        <CarouselItem key={option.name} className="max-w-72">
                                                            <FormItem>
                                                                <FormLabel className="[&:has([data-state=checked])>div]:border-primary [&:has([data-state=checked])>div]:bg-accent hover:cursor-pointer">
                                                                    <FormControl>
                                                                        <RadioGroupItem value={option.name} className="sr-only" />
                                                                    </FormControl>
                                                                    <Card className="w-fit">
                                                                        <CardHeader>
                                                                            <h2 className="text-xl">{option.name}</h2>
                                                                            <CardDescription>
                                                                                {option.type}
                                                                            </CardDescription>
                                                                        </CardHeader>
                                                                        <CardContent className="py-2 text-pretty">
                                                                            {option.description}
                                                                        </CardContent>
                                                                        <CardFooter className="pt-2">
                                                                            <Table>
                                                                                <TableBody>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Cost</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.costIndicator}</TableCell>
                                                                                    </TableRow>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Organization</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.organization}</TableCell>
                                                                                    </TableRow>
                                                                                </TableBody>
                                                                            </Table>
                                                                        </CardFooter>
                                                                    </Card>
                                                                </FormLabel>
                                                            </FormItem>
                                                        </CarouselItem>
                                                    ))}
                                            </CarouselContent>
                                            <CarouselPrevious />
                                            <CarouselNext />
                                        </Carousel>
                                    </RadioGroup>
                                </FormItem>
                            )}
                        />
                        <Separator />
                        <FormField
                            control={form.control}
                            name="documentStore"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Document Stores</FormLabel>
                                    <FormDescription className="pb-4">
                                        Choose the document store that will store your documents.
                                    </FormDescription>
                                    <FormMessage />
                                    <RadioGroup
                                        asChild
                                        onValueChange={field.onChange}
                                        defaultValue={field.value}
                                    >
                                        <Carousel className="w-[calc(100%-100px)] mx-auto">
                                            <CarouselContent>
                                                {
                                                    documentStoreOptions.map((option) => (
                                                        <CarouselItem key={option.name} className="max-w-72">
                                                            <FormItem>
                                                                <FormLabel className="[&:has([data-state=checked])>div]:border-primary [&:has([data-state=checked])>div]:bg-accent hover:cursor-pointer">
                                                                    <FormControl>
                                                                        <RadioGroupItem value={option.name} className="sr-only" />
                                                                    </FormControl>
                                                                    <Card className="w-fit">
                                                                        <CardHeader>
                                                                            <h2 className="text-xl">{option.name}</h2>
                                                                            <CardDescription>
                                                                                {option.type}
                                                                            </CardDescription>
                                                                        </CardHeader>
                                                                        <CardContent className="py-2 text-pretty">
                                                                            {option.description}
                                                                        </CardContent>
                                                                        <CardFooter className="pt-2">
                                                                            <Table>
                                                                                <TableBody>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Cost</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.costIndicator}</TableCell>
                                                                                    </TableRow>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Organization</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.organization}</TableCell>
                                                                                    </TableRow>
                                                                                </TableBody>
                                                                            </Table>
                                                                        </CardFooter>
                                                                    </Card>
                                                                </FormLabel>
                                                            </FormItem>
                                                        </CarouselItem>
                                                    ))}
                                            </CarouselContent>
                                            <CarouselPrevious />
                                            <CarouselNext />
                                        </Carousel>
                                    </RadioGroup>
                                </FormItem>
                            )}
                        />
                        <Separator />
                        <FormField
                            control={form.control}
                            name="embeddingModel"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Embedding Models</FormLabel>
                                    <FormDescription className="pb-4">
                                        Choose the embedding model that will transform your documents in embeddings.
                                    </FormDescription>
                                    <FormMessage />
                                    <RadioGroup
                                        asChild
                                        onValueChange={field.onChange}
                                        defaultValue={field.value}
                                    >
                                        <Carousel className="w-[calc(100%-100px)] mx-auto">
                                            <CarouselContent>
                                                {
                                                    embeddingsModelOptions.map((option) => (
                                                        <CarouselItem key={option.name} className="max-w-72">
                                                            <FormItem>
                                                                <FormLabel className="[&:has([data-state=checked])>div]:border-primary [&:has([data-state=checked])>div]:bg-accent hover:cursor-pointer">
                                                                    <FormControl>
                                                                        <RadioGroupItem value={option.name} className="sr-only" />
                                                                    </FormControl>
                                                                    <Card className="w-fit">
                                                                        <CardHeader>
                                                                            <h2 className="text-xl">{option.name}</h2>
                                                                            <CardDescription>
                                                                                {option.type}
                                                                            </CardDescription>
                                                                        </CardHeader>
                                                                        <CardContent className="py-2 text-pretty">
                                                                            {option.description}
                                                                        </CardContent>
                                                                        <CardFooter className="pt-2">
                                                                            <Table>
                                                                                <TableBody>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Cost</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.costIndicator}</TableCell>
                                                                                    </TableRow>
                                                                                    <TableRow>
                                                                                        <TableCell className="p-2">Organization</TableCell>
                                                                                        <TableCell className="p-2 font-bold">{option.organization}</TableCell>
                                                                                    </TableRow>
                                                                                </TableBody>
                                                                            </Table>
                                                                        </CardFooter>
                                                                    </Card>
                                                                </FormLabel>
                                                            </FormItem>
                                                        </CarouselItem>
                                                    ))}
                                            </CarouselContent>
                                            <CarouselPrevious />
                                            <CarouselNext />
                                        </Carousel>
                                    </RadioGroup>
                                </FormItem>
                            )}
                        />
                        <Separator />
                        <div className="py-8 flex justify-center">
                            <Button className="w-full sm:w-5/12 py-6" type="submit">Confirm configuration</Button>
                        </div>
                    </form>
                </Form>
            </ScrollArea>
        </div>
    )
}



export function ConfigurationForm() {

}
