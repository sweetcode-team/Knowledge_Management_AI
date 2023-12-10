import React, { useState } from 'react'
import './fileUploader.css'
import Dropzone from './Dropzone'
import FileListItem from './FileListItem'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCloudArrowUp, faTrash } from '@fortawesome/free-solid-svg-icons'
import { toast } from 'react-toastify';

export default function FileUploader() {

    const [files, setFiles] = useState([])
    const [rejected, setRejected] = useState([])

    const [isFileListOpen, setIsFileListOpen] = useState(true);
    
    const toggleFileList = () => {
        setIsFileListOpen((prevIsFileListOpen) => !prevIsFileListOpen);
    }

    const handleFiles = (acceptedFiles, rejectedFiles) => {
        if (acceptedFiles?.length) {
            setFiles(previousFiles => {
                const uniqueAcceptedFiles = acceptedFiles.filter(file => {
                    return !previousFiles.some(existingFile => existingFile.name === file.name);
                })

                return [
                    ...previousFiles,
                    ...uniqueAcceptedFiles.map(file =>
                        Object.assign(file, { preview: URL.createObjectURL(file) })
                    )
                ]
            })
        }

        if (rejectedFiles?.length) {
            setRejected(previousFiles => [...previousFiles, ...rejectedFiles])
        }

        setIsFileListOpen(true)
    }

    const uploadFiles = () => {
        console.log(files)
        const formData = new FormData();

        files.forEach(file => {
            formData.append('file', file);
        })

        toast.promise(
            fetch('http://localhost:5050/uploadFile', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            }),
            {
                pending: 'Uploading...',
                success: 'Upload avvenuto con successo',
                error: 'Upload fallito'
            }
        )
  
        removeAll()
    }

    const removeAll = () => {
        files.forEach(file => {
           URL.revokeObjectURL(file.preview)
        });
        rejected.forEach(file => {
           URL.revokeObjectURL(file.preview)
        });
        setFiles([])
        setRejected([])
    }
    
    const removeFile = name => {
        const filesToRemove = files.filter(file => file.name === name)
        // To prevent memory leaks
        filesToRemove.forEach(fileToRemove => {
            URL.revokeObjectURL(fileToRemove.preview)
        });

        setFiles(files => files.filter(file => file.name !== name))
    }

    const removeRejected = name => {
        const filesToRemove = rejected.filter(file => file.name === name)
        // To prevent memory leaks
        filesToRemove.forEach(fileToRemove => {
           URL.revokeObjectURL(fileToRemove.preview)
        });

        setRejected(rejected => rejected.filter(({ file }) => file.name !== name))
    }

    return (
        <div className="main__fileuploader">
            <div className="dropzone__card">
                <Dropzone className='dropZone' handleFiles={handleFiles} />
            </div>
            <div className='filelist__body'>
                <div className={`filelist__card ${isFileListOpen ? 'open' : ''}`}>
                    <div className='card__header' onClick={toggleFileList}>
                        <h4>Lista file</h4>
                        <i className="fa fa-angle-down"></i>
                    </div>
                    <div className="card__content">
                        {
                            files.length !== 0 ?
                            files.map((file) => {
                                return (
                                    <FileListItem
                                        name={file.name}
                                        key={file.name}
                                        onDelete={(name) => removeFile(name)}
                                        size={file.size}
                                        linkPreview={file.preview}
                                    />
                                )
                            }) : <p style={{ textAlign: 'center', paddingBottom: "20px" }}>Nessun file caricato.</p>
                        }
                    </div>
                </div>
                <div className="files_buttons">
                    <div className="submit_files">
                        <button onClick={uploadFiles} className="submit_files_button" disabled={files.length === 0}>
                            <span>Upload</span>
                            <FontAwesomeIcon icon={faCloudArrowUp} style={{ fontSize: "20px", flex: "1" }} />
                        </button>
                    </div>
                    <div className="delete_all_files">
                        <button onClick={removeAll} className="delete_all_files_button" disabled={files.length === 0}>
                            <span>Elimina</span>
                            <FontAwesomeIcon icon={faTrash} style={{ fontSize: "20px", flex: "1" }} />
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}