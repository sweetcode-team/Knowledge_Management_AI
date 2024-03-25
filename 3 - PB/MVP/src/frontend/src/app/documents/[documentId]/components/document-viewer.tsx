"use client"
import React, {useEffect, useRef, useState} from 'react';

import {DocumentWithContent} from "@/types/types";
import {getDocumentContent} from "@/lib/actions";
import mammoth from "mammoth";
interface DocumentViewerProps{
  document : DocumentWithContent
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
                mammoth.convertToHtml({ arrayBuffer })
                    .then(function (result) {
                        var html = result.value; // L'HTML generato
                        console.log(html)
                        var messages = result.messages; // Eventuali messaggi, come avvisi durante la conversione
                        setHtmlContent(html); // Imposta l'HTML generato nello stato per renderizzarlo successivamente
                    })
                    .catch((error) => console.error(error)); // Gestisci eventuali errori
            });
        }
    }, [document.content]);


    return (
        document.type.toUpperCase() === "PDF" ?
            <iframe id={document.id} src={src} className="h-full"> </iframe>
            :
            <div>
                <div dangerouslySetInnerHTML={{ __html: htmlContent }} />
            </div>
    );
};