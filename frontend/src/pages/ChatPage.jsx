import { useEffect, useState } from "react";
import api from "../api/axios";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";

import "../styles/Chat.css";


function ChatPage() {
     console.log("CHAT PAGE LOADED");



    const [selectedThread, setSelectedThread] = useState(
        localStorage.getItem("selectedThread")
    );


    const [messages, setMessages] = useState([]);



    // Load messages whenever a thread is selected
    useEffect(() => {

        if (selectedThread) {

            loadMessages(selectedThread);

        }

    }, [selectedThread]);



    // Get chat history from Django
    const loadMessages = async (threadId) => {
         console.log("LOADING THREAD:", threadId); 
        try {

            const response = await api.get(
                `threads/${threadId}/messages/`
            );
             console.log("API MESSAGES:", response.data);

        
            setMessages(response.data);


        } catch (error) {

            console.error(
                "Failed to load messages:",
                error
            );


            setMessages([]);

        }

    };



    // Called when clicking a thread
    const handleSelectThread = (threadId) => {

        setSelectedThread(threadId);


        localStorage.setItem(
            "selectedThread",
            threadId
        );

    };



    return (

        <div className="chat-container">


            <Sidebar

                selectedThread={selectedThread}

                setSelectedThread={handleSelectThread}

            />



            <ChatWindow

                threadId={selectedThread}

                messages={messages}

                setMessages={setMessages}

            />


        </div>

    );

}


export default ChatPage;