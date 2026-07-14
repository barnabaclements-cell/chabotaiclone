import "../styles/Chat.css";
function Message({ role, content }) {
  const isUser = role === "user";

  return (
    <div
      style={{
        display: "flex",
        justifyContent: isUser ? "flex-end" : "flex-start",
        marginBottom: "15px",
      }}
    >
      <div
        style={{
          maxWidth: "70%",
          padding: "12px 16px",
          borderRadius: "12px",
          backgroundColor: isUser ? "#10a37f" : "#f1f1f1",
          color: isUser ? "#ffffff" : "#000000",
          boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
        }}
      >
        <div
          style={{
            fontWeight: "bold",
            marginBottom: "6px",
          }}
        >
          {isUser ? "You" : "AI"}
        </div>

        <div
          style={{
            whiteSpace: "pre-wrap",
            wordBreak: "break-word",
            lineHeight: "1.5",
          }}
        >
          {content}
        </div>
      </div>
    </div>
  );
}

export default Message;