"use client"
import React, { useEffect, useRef, useState } from 'react';

import { DocumentWithContent } from "@/types/types";
import { getDocumentContent } from "@/lib/actions";
import mammoth from "mammoth";
import { ScrollArea } from '@/components/ui/scroll-area';
interface DocumentViewerProps {
    document: DocumentWithContent
}


export const DocumentViewer = ({ document }: DocumentViewerProps) => {
    const [src, setSrc] = useState('');
    const [htmlContent, setHtmlContent] = useState('');
    const documentRef = useRef<HTMLInputElement>(null);

    useEffect(() => {
        if (document.type.toUpperCase() === "PDF") {
            const prova = Buffer.from(document.content, 'hex');
            const blob = new Blob([prova], { type: 'application/pdf' });
            const pdfUrl = URL.createObjectURL(blob);
            setSrc(pdfUrl);
        } else {
            const prova = Buffer.from(document.content, 'hex');
            const blob = new Blob([prova], { type: 'application/msdoc' });

            blob.arrayBuffer().then(arrayBuffer => {
                mammoth.convertToHtml(
                    { arrayBuffer },
                    {
                        includeDefaultStyleMap: true
                    }
                )
                    .then(function (result) {
                        var html = result.value;
                        console.log(html)
                        var messages = result.messages;
                        setHtmlContent(html);
                    })
                    .catch((error) => console.error(error));
            });
        }
    }, [document.content]);


    return (
        document.type.toUpperCase() === "PDF" ?
            <iframe id={document.id} src={src} className="h-full"> </iframe>
            :
            <ScrollArea className='w-full h-full text-black bg-white'>
                <div
                    className='px-8 [&>img]:max-w-60 [&>img]:max-h-60 [&>img]:flex [&>img]:justify-center [&>img]:m-auto [&>img]:my-4 '
                    dangerouslySetInnerHTML={{ __html: htmlContent }} />
            </ScrollArea>
    );
};