"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { SubmitHandler, useFieldArray, useForm } from "react-hook-form"
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
import { toast } from "sonner"

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
  ConfigurationOptions,
  LLMConfigurationFormValues,
  configurationFormSchema
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
import { changeConfiguration } from "@/lib/actions"

interface SettingsConfigurationFormProps {
  currentConfiguration: Configuration
  configurationOptions: ConfigurationOptions
}

export function SettingsConfigurationForm({ currentConfiguration, configurationOptions }: SettingsConfigurationFormProps) {

  const defaultValues: Partial<LLMConfigurationFormValues> = {
    LLMModel: currentConfiguration.LLMModel.name,
  }

  const form = useForm<LLMConfigurationFormValues>({
    resolver: zodResolver(configurationFormSchema),
    mode: "onChange",
    defaultValues
  })


  const onSubmit: SubmitHandler<LLMConfigurationFormValues> = async (data) => {
    const toastId = toast.loading("Loading...", {
      description: "Updating your configuration.",
    })

    let result: ConfigurationOperationResponse | null = null
    try {
      result = await changeConfiguration(data)
    } catch (e) {
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
  }

  const LLMModelOptions: LLMModel[] = configurationOptions.LLMModels

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
              ].map((option, index) => (
                <CarouselItem key={index} className="max-w-72">
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
                        LLMModelOptions.map((option, index) => (
                          <CarouselItem key={index} className="max-w-72 min-h-full">
                            <FormItem className="h-full">
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
            <Button
              className="w-full sm:w-5/12 py-6"
              type="submit"
              disabled={form.formState.isSubmitting}
            >
              Confirm configuration
            </Button>
          </div>
        </form>
      </Form>
    </>
  )
}
