import { useEffect, useState } from "react";
import api from "../api/axios";
import "../styles/Chat.css";

function Sidebar({ selectedThread, setSelectedThread }) {
    const [threads, setThreads] = useState([]);

    useEffect(() => {
        loadThreads();
    }, []);

    const loadThreads = async () => {
        try {
            const response = await api.get("threads/");
            setThreads(response.data);
        } catch (error) {
            console.error("Error loading threads:", error);
        }
    };

    const createThread = async () => {
        try {
            const response = await api.post("threads/create/", {
                title: "New Chat",
            });

            const newThread = response.data;

            setThreads((prev) => [newThread, ...prev]);
            setSelectedThread(newThread.id);
        } catch (error) {
            console.error("Error creating thread:", error);
        }
    };

    return (
        <div className="sidebar">
            <h2>ChatGPT Clone</h2>

            <button
                className="new-chat-btn"
                onClick={createThread}
            >
                + New Chat
            </button>

            <div className="thread-list">
                {threads.length === 0 ? (
                    <p>No chats yet.</p>
                ) : (
                    threads.map((thread) => (
                        <div
                            key={thread.id}
                            className={`thread-item ${
                                selectedThread === thread.id ? "active" : ""
                            }`}
                            onClick={() => {
    console.log("CLICKED THREAD:", thread.id);
    setSelectedThread(thread.id);
}}
                        >
                            {thread.title}
                        </div>
                    ))
                )}
            </div>
        </div>
    );
}

export default Sidebar;