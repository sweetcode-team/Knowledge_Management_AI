"use client"

import React from "react";
import DocViewer, { DocViewerRenderers } from "@cyntler/react-doc-viewer";

export function DocumentViewer() {
    const docs = [
        {
            uri: "", fileType: 'pdf',
        }
    ];
    return (
        <div>
            <DocViewer
                documents={docs}
                pluginRenderers={DocViewerRenderers}
            // style={{ width: "50%" }} //custom style
            // config={{
            //   loadingRenderer: {
            //     overrideComponent: MyLoadingRenderer,
            //   },
            // }}
            />
        </div>
    );
}