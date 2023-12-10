import React, { Component } from 'react'
import './nav.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCog } from '@fortawesome/free-solid-svg-icons'

export default class Nav extends Component {
    render() {
        return (
            <div className="nav">
                <div className="nav__blocks">
                    <FontAwesomeIcon icon={faCog} style={{ color: "black", fontSize: "25px", padding: "0", cursor: "pointer"}}/>
                </div>
                <div className="nav__blocks"></div>
                <div className="nav__blocks"></div>
            </div>
        )
    }
}
