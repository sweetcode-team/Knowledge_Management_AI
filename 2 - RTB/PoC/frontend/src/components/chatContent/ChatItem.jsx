import React from "react";
import Avatar from "../chatInfo/Avatar";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMicrochip, faUser } from "@fortawesome/free-solid-svg-icons";


export default function ChatItem(props) {
    return (
      <div
        style={{ animationDelay: `${props.animationDelay}s` }}
        className={`chat__item ${props.user ? props.user : ""}`}
      >
        <div className="chat__item__content">
          <div className="chat__msg">{props.msg}</div>
          {/* <div className="chat__meta">
            <span>16 mins ago</span>
            <span>Seen 1.03PM</span>
          </div> */}
        </div>
        <Avatar
          isOnline="active"
          image={props.user === 'me' ?
            <FontAwesomeIcon icon={faUser} /> :
            <FontAwesomeIcon icon={faMicrochip} />} />
      </div>
    )
}
