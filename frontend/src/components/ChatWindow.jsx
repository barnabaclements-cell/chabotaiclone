import { useState } from "react";
import api from "../api/axios";
import Message from "./Message";

import "../styles/Chat.css";


function ChatWindow({
    threadId,
    messages,
    setMessages
}) {


    const [input, setInput] = useState("");

    const [loading, setLoading] = useState(false);



    const sendMessage = async () => {


        if (!threadId) {

            alert("Please select or create a chat first.");

            return;

        }


        if (!input.trim()) {

            return;

        }



        const currentMessage = input;



        // Show user message immediately
        setMessages((prev) => [

            ...prev,

            {
                role: "user",
                content: currentMessage
            }

        ]);



        setInput("");

        setLoading(true);



        try {


            console.log("Thread ID:", threadId);

            console.log("Message:", currentMessage);



            // Send message to backend
            await api.post(
                "chat/",
                {
                    thread_id: threadId,
                    message: currentMessage
                }
            );



            // Reload messages from database
            const response = await api.get(
                `threads/${threadId}/messages/`
            );



            setMessages(response.data);



        } catch (error) {


            console.error(
                "Chat Error:",
                error
            );



            if (error.response) {

                console.log(
                    error.response.data
                );

            }



            setMessages((prev) => [

                ...prev,

                {
                    role: "assistant",
                    content: "Something went wrong."
                }

            ]);



        } finally {


            setLoading(false);


        }

    };



    return (

        <div className="chat-window">


            <div className="messages">


                {
                    messages.map((message, index) => (

                        <Message

                            key={index}

                            role={message.role}

                            content={message.content}

                        />

                    ))
                }



                {
                    loading && (

                        <p>
                            Thinking...
                        </p>

                    )
                }


            </div>



            <div className="chat-input">


                <input

                    type="text"

                    placeholder="Type your message..."

                    value={input}


                    onChange={(e) =>
                        setInput(e.target.value)
                    }


                    onKeyDown={(e) => {

                        if (e.key === "Enter") {

                            sendMessage();

                        }

                    }}

                />



                <button

                    onClick={sendMessage}

                    disabled={loading}

                >

                    Send

                </button>


            </div>


        </div>

    );

}


export default ChatWindow;