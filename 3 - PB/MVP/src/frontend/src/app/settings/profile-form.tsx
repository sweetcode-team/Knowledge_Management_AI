"use client"

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
  Alert,
  AlertDescription,
  AlertTitle,
} from "@/components/ui/alert"

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
import { InfoIcon } from "lucide-react"
import { Separator } from "@/components/ui/separator"

const configurationFormSchema = z.object({
  LLMModel: z.string()
})

type ConfigurationFormValues = z.infer<typeof configurationFormSchema>

const defaultValues: Partial<ConfigurationFormValues> = {}

export function ConfigurationForm() {
  const form = useForm<ConfigurationFormValues>({
    resolver: zodResolver(configurationFormSchema),
    defaultValues,
    mode: "onChange",
  })

  function onSubmit(data: ConfigurationFormValues) {
    // TODO: changeConfiguration(data)
    toast({
      title: "You submitted the following values:",
      description: (
        <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4">
          <code className="text-white">{JSON.stringify(data, null, 2)}</code>
        </pre>
      ),
    })
  }

  const currentConfiguration: Configuration = {
    LLMModel: {
      name: "GPT-3.5-turbo",
      type: "Language Model",
      costIndicator: "Paid",
      description: "The GPT-3.5-turbo model is a language model that is capable of answering questions and generating text based on the input it receives.",
      organization: "OpenAI"
    },
    vectorStore: {
      name: "VectorStore",
      type: "Vector Store",
      costIndicator: "Free",
      description: "The Vector Store is a store that is capable of storing vectors.",
      organization: "Meta"
    },
    documentStore: {
      name: "DocumentStore",
      type: "Document Store",
      costIndicator: "Free",
      description: "The Document Store is a store that is capable of storing documents.",
      organization: "Meta"
    },
    embeddingModel: {
      name: "EmbeddingsModel",
      type: "Embeddings Model",
      costIndicator: "Free",
      description: "The Embeddings Model is a model that is capable of generating embeddings.",
      organization: "Meta"
    }
  }

  const configurationOptions = {
    LLMModel: [{
      name: "GPT-3.5-turbo",
      type: "Language Model",
      costIndicator: "Paid",
      description: "The GPT-3.5-turbo model is a language model that is capable of answering questions and generating text based on the input it receives.",
      organization: "OpenAI"
    },
    {
      name: "LLama",
      type: "Language Model",
      costIndicator: "Free",
      description: "The LLama model is a language model that is capable of answering questions and generating text based on the input it receives.",
      organization: "Meta"
    },
    {
      name: "GPT 4",
      type: "Language Model",
      costIndicator: "Free",
      description: "The LLama model is a language model that is capable of answering questions and generating text based on the input it receives.",
      organization: "Meta"
    },
    {
      name: "HGMod",
      type: "Language Model",
      costIndicator: "Free",
      description: "The LLama model is a language model that is capable of answering questions and generating text based on the input it receives.",
      organization: "Meta"
    }
    ],
    VectorStore: [],
    DocumentStore: [],
    EmbeddingModel: []
  }

  const LLMModelOptions: LLMModel[] = configurationOptions.LLMModel

  return (
    <>
      <div className="space-y-2">
        <p className="text-lg">Current Configuration</p>
        <Carousel className="w-[calc(100%-100px)] mx-auto">
          <CarouselContent>
            {
              [
                currentConfiguration.LLMModel,
                currentConfiguration.documentStore,
                currentConfiguration.vectorStore,
                currentConfiguration.embeddingModel
              ].map((option) => (
                <CarouselItem key={option.name} className="max-w-72">
                  <Card className="w-fit text-sm font-medium leading-none h-full flex flex-col justify-between">
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
                </CarouselItem>
              ))}
          </CarouselContent>
          <CarouselPrevious />
          <CarouselNext />
        </Carousel>
      </div>
      <Separator />
      <Alert variant="info" className="w-full sm:w-fit">
        <InfoIcon className="w-5 h-5" />
        <AlertTitle>Only the LLM model is configurable</AlertTitle>
        <AlertDescription>
          Contact the software maintainer to manage other choices.
        </AlertDescription>
      </Alert>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="w-full space-y-8">
          <FormField
            control={form.control}
            name="LLMModel"
            render={({ field }) => (
              <FormItem>
                <FormLabel>
                  <p className="text-lg">LLM Models</p>
                </FormLabel>
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
                                <Card className="w-fit text-sm font-medium leading-none h-full flex flex-col justify-between">
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
          <div className="py-8 flex justify-center">
            <Button className="w-full sm:w-5/12 py-6" type="submit">Confirm configuration</Button>
          </div>
        </form>
      </Form>
    </>
  )
}
