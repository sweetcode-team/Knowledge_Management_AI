import React from 'react'
import prettyBytes from 'pretty-bytes';
import { faRemove } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

export default function FileListItem(props) {

    return (
        <div className={'filelist__item'}>
            <div className="fileInfo">
                <a href={props.linkPreview} target="_blank" >{props.name}</a>
                <span>{prettyBytes(props.size)}</span>
            </div>
            <button
                type='button'
                className="fileDeleteBtn"
                onClick={() => props.onDelete(props.name)}
            >
                <FontAwesomeIcon icon={faRemove} style={{ display: "block", padding: "10px 0px"}}/>
            </button>
        </div>
    )
}
