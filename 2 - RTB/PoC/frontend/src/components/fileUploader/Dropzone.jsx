import { useCallback, useEffect, useState } from 'react'
import { useDropzone } from 'react-dropzone'
import './fileUploader.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFileCirclePlus } from '@fortawesome/free-solid-svg-icons'

export default function Dropzone(props) {

  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    props.handleFiles(acceptedFiles, rejectedFiles)
  }, [])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      'application/pdf': []
    },
    // maxSize: 1024 * 1000,
    onDrop
  })

  // useEffect(() => {
  //   // Revoke the data uris to avoid memory leaks
  //   return () => files.forEach(file => URL.revokeObjectURL(file.preview))
  // }, [files])

  return (
    <form style={{ width: "100%" }} onSubmit={props.handleSubmit}>
      <div
        {...getRootProps({
          className: props.className
        })}
      >
        <h3>Carica pdf</h3>
        <FontAwesomeIcon icon={faFileCirclePlus} style={{ padding: "10px 0px", fontSize: "25px"}}/>
        <input {...getInputProps()} />
        <div className=''>
          {/* <ArrowUpTrayIcon className='w-5 h-5 fill-current' /> */}
          {isDragActive ? (
            <p>Rilascia qui...</p>
          ) : (
            <p>Drag & drop, click per selezionare file</p>
          )}
        </div>
      </div>
    </form>
  )
}