'use client'

import { Separator } from "@/components/ui/separator";

import { zodResolver } from "@hookform/resolvers/zod"
import { SubmitHandler, useForm } from "react-hook-form"

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
import { toast } from "sonner"

import {
    LLMModel,
    VectorStore,
    DocumentStore,
    EmbeddingsModel,
    ConfigurationOptions,
    configurationFormSchema,
    ConfigurationFormValues,
    ConfigurationOperationResponse
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
import { setConfiguration } from "@/lib/actions";
import { useRouter } from "next/navigation";

interface ConfigurationFormProps {
    configurationOptions: ConfigurationOptions
}

export function ConfigurationForm({ configurationOptions }: ConfigurationFormProps) {

    const form = useForm<ConfigurationFormValues>({
        resolver: zodResolver(configurationFormSchema),
        mode: "onChange",
    })

    const onSubmit: SubmitHandler<ConfigurationFormValues> = async (data) => {
        const toastId = toast.loading("Loading...",
            { description: "Setting configuration." }
        )

        let result: ConfigurationOperationResponse | null
        try {
            result = await setConfiguration(data)
        } catch (error) {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }

        if (!result) {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }
        else if (result.status) {
            toast.success("Operation successful", {
                description: "The configuration has been set.",
                id: toastId
            })
        }
        else {
            toast.error("An error occurred", {
                description: "Please try again later.",
                id: toastId
            })
            return
        }
        form.reset()
        useRouter().push('/')
    }

    const LLMModelOptions: LLMModel[] = configurationOptions.LLMModels
    const vectorStoreOptions: VectorStore[] = configurationOptions.vectorStores
    const documentStoreOptions: DocumentStore[] = configurationOptions.documentStores
    const embeddingsModelOptions: EmbeddingsModel[] = configurationOptions.embeddingModels

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