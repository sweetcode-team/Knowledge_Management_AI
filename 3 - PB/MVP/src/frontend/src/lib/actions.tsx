"use server"

import {
    AskChatbotFormValues,
    Chat,
    ChatOperationResponse,
    ChatPreview,
    Configuration,
    ConfigurationOperationResponse,
    ConfigurationOptions,
    DocumentWithContent,
    LightDocument,
    DocumentOperationResponse,
    LLMConfigurationFormValues,
    MessageResponse,
    RenameChatFormValues
} from "@/types/types"
import { revalidateTag } from "next/cache";
import { ConfigurationFormValues } from '../types/types';

const API_URL = process.env.API_URL

export async function askChatbot(formData: AskChatbotFormValues): Promise<MessageResponse> {
    try {
        const response = await fetch(`${API_URL}/askChatbot`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(formData as any).toString(),
        })
        revalidateTag("chat")
        return response.json()
    } catch (e) {
        throw new Error();
    }
}

export async function changeConfiguration(formData: LLMConfigurationFormValues): Promise<ConfigurationOperationResponse> {
    const response = await fetch(`${API_URL}/changeConfiguration`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(formData).toString()
    })
    revalidateTag("configuration")

    return response.json()
}

export async function concealDocuments(ids: string[]): Promise<DocumentOperationResponse[]> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`${API_URL}/concealDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function deleteChats(ids: number[]): Promise<ChatOperationResponse[]> {
    const formData = new URLSearchParams()
    ids.forEach(id => formData.append('chatIds', id.toString()))

    const result = await fetch(`${API_URL}/deleteChats`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("chat")

    return result.json()
}

export async function deleteDocuments(ids: string[]): Promise<DocumentOperationResponse[]> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`${API_URL}/deleteDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function embedDocuments(ids: string[]): Promise<DocumentOperationResponse[]> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`${API_URL}/embedDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function enableDocuments(ids: string[]): Promise<DocumentOperationResponse[]> {
    const formData = new URLSearchParams();
    ids.forEach(id => formData.append('documentIds', id));

    const result = await fetch(`${API_URL}/enableDocuments`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    revalidateTag("document")

    return result.json()
}

export async function getChatMessages(id: number): Promise<Chat> {
    const result = await fetch(`${API_URL}/getChatMessages/${id}`,
        {
            next: { tags: ["chat"] }
        }
    )
    return result.json()
}

export async function getChats(filter: string = ""): Promise<ChatPreview[]> {
    const result = await fetch(`${API_URL}/getChats` + (filter.trim() !== "" ? `/${filter.trim()}` : ""),
        {
            next: { tags: ["chat"] }
        }
    )
    return result.json()
}

export async function getConfigurationOptions(): Promise<ConfigurationOptions> {
    const result = await fetch(`${API_URL}/getConfigurationOptions`, {
        headers: {
            "Content-Type": "application/json"
        },
        next: { tags: ["configuration"] }
    })
    return result.json()
}

export async function getConfiguration(): Promise<Configuration | null> {
    const result = await fetch(`${API_URL}/getConfiguration`,
        {
            next: { tags: ["configuration"] }
        }
    )
    if (!result.ok) {
        if (result.status === 401)
            return null;
        throw new Error('Failed to fetch configuration');
    }
    return result.json();
}

export async function getDocumentContent(id: string): Promise<DocumentWithContent> {
    const result = await fetch(`${API_URL}/getDocumentContent/${id}`,
        {
            next: { tags: ["document"] }
        }
    )
    return result.json()
}

export async function getDocuments(filter: string = ""): Promise<LightDocument[]> {
    const result = await fetch(`${API_URL}/getDocuments` + (filter.trim() !== "" ? `/${filter.trim()}` : ""),
        {
            next: { tags: ["document"] }
        }
    )
    if (!result.ok) {
        return [];
    }
    return result.json()
}

export async function renameChat(formData: RenameChatFormValues): Promise<ChatOperationResponse> {
    const result = await fetch(`${API_URL}/renameChat`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(formData as any).toString(),
    })
    revalidateTag("chat")

    return result.json()
}

export async function setConfiguration(configuration: ConfigurationFormValues): Promise<ConfigurationOperationResponse> {
    const result = await fetch(`${API_URL}/setConfiguration`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(configuration).toString()
    })
    revalidateTag("configuration")

    return result.json()
}

export async function uploadDocuments(formData: FormData, forceUpload: boolean = false): Promise<DocumentOperationResponse[]> {
    if (forceUpload) {
        formData.append('forceUpload', 'true')
    }
    const result = await fetch(`${API_URL}/uploadDocuments`, {
        method: 'POST',
        body: formData
    })
    revalidateTag("document")

    return result.json()
}