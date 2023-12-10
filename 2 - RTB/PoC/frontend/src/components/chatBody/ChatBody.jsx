import React, { Component } from "react";
import "./chatBody.css";
import ChatList from "../chatList/ChatList";
import ChatContent from "../chatContent/ChatContent";
import FileUploader from "../fileUploader/FileUploader";

export default class ChatBody extends Component {
  render() {
    return (
      <div className="main__chatbody">
        <ChatList/>
        <ChatContent/>
        <FileUploader/>
      </div>
    );
  }
}
