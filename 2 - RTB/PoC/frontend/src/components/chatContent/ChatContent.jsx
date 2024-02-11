import React, { useState, createRef, useEffect } from "react";

import "./chatContent.css";
import ChatItem from "./ChatItem";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faRedo } from '@fortawesome/free-solid-svg-icons' 
import { faPaperPlane } from "@fortawesome/free-solid-svg-icons"
import sweetcodelogo from "../../images/sweetcode-logo.svg"
import { toast } from 'react-toastify';

export default function ChatContent() {
  const messagesEndRef = createRef(null);

  const [chatMessages, setchatMessages] = useState([])
  const [message, setMessage] = useState("")

  useEffect(() => {
    scrollToBottom()
  }, [chatMessages]);

  const scrollToBottom = () => {
    messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
  };

  const handleEnter = (e) => {
    if (e.key === "Enter") {
      insertChatMessage()
    }
  }

  const resetChat = () => {
    fetch('http://localhost:5050/resetChat', {
      method: 'POST',
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }
      // clear the chat messages in state
      setchatMessages([]);
    })
    .catch(error => {
      console.error('Error resetting chat:', error);
    });
  };

  const sendQuery = (query) => {
    const formData = new FormData();
    formData.append('query', query);

    toast.promise(
      fetch('http://localhost:5050/askChatbot', {
              method: 'POST',
              body: formData
          })
          .then((response) => {
            if (!response.ok) {
              throw new Error(`Errore HTTP ${response.status}`)
            }
            return response.json()
          })
          .then(data => {
            console.log(data.answer);
              setchatMessages(oldMessages => [
                ...oldMessages,
                {
                  key: chatMessages.length + 1,
                  type: "other",
                  msg: data.answer,
                  image: "",
                }
              ])
          }),
      {
        pending: 'Elaborando risposta...',
        error: 'Errore di elaborazione. Riprova'
      }
    )
  }

  const insertChatMessage = () => {
    if (message.trim() !== "") {
      setchatMessages(oldMessages => [
        ...oldMessages,
        {
          key: chatMessages.length,
          type: "",
          msg: message,
          image: "",
        }
      ])
      setMessage("")
      sendQuery(message.trim())
    }
  }

  return (
    <div className="main__chatcontent">
      <div className="content__header">
        <div className="blocks">
          <div className="current-chatting-user">
            <h1>Knowledge Management AI</h1>
          </div>
        </div>
      </div>
      
      <div className="content__body">
        <div className="chat_dialog">
          <div className="chat__items">
            {
              chatMessages.length !== 0 ?
              chatMessages.map((item, index) => {
              return (
                <ChatItem
                  animationDelay={index * 0.03}
                  key={item.key}
                  user={item.type ? item.type : "me"}
                  msg={item.msg}
                  image={item.image}
                />
              )
              }) :
                  <div className="welcome_message">
                    <img src={sweetcodelogo} alt="SWEetCode logo"/>
                    <h2>Hey, come posso aiutarti?</h2>
                  </div>
            }
            <div ref={messagesEndRef} />
          </div>
        </div>
        <div className="content__footer">
          <div className="sendNewMessage">
            <button id="resetChatBtn" onClick={() => document.getElementById('confirmModal').style.display = 'block'} disabled={chatMessages.length < 2}>
              <FontAwesomeIcon icon={faRedo} />
            </button>
            <input
              type="text"
              placeholder="Type a message here"
              onChange={(e) => {setMessage(e.target.value)}}
              value={message}
              onKeyUp={handleEnter}
            />
            <button
              id="sendMsgBtn"
              onClick={insertChatMessage}
              disabled={message === ""}
            >
              <FontAwesomeIcon icon={faPaperPlane} />
            </button>
          </div>
          <div id="confirmModal">
            <div id="confirmModalContent">
              <p>Sei sicuro di voler cancellare tutti i messaggi?</p>
              <button id="noButton" onClick={() => document.getElementById('confirmModal').style.display = 'none'}>No</button>
              <button id="siButton" onClick={() => { resetChat(); document.getElementById('confirmModal').style.display = 'none'; }}>Sì</button>             
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
