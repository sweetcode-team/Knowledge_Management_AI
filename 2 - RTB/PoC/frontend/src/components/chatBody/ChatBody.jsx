import React, { Component } from "react";
import "./chatBody.css";
import ChatInfo from "../chatInfo/ChatInfo";
import ChatContent from "../chatContent/ChatContent";
import FileUploader from "../fileUploader/FileUploader";

export default class ChatBody extends Component {
  render() {
    return (
      <div className="main__chatbody">
        <ChatInfo/>
        <ChatContent/>
        <FileUploader/>
      </div>
    );
  }
}
