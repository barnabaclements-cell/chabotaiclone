import { Routes, Route, Navigate } from "react-router-dom";

import Login from "./components/Login";
import Signup from "./components/Signup";
import ChatPage from "./pages/ChatPage";


function App() {
  return (
    <Routes>

      <Route 
        path="/" 
        element={<Navigate to="/login" />} 
      />

      <Route 
        path="/login" 
        element={<Login />} 
      />

      <Route 
        path="/signup" 
        element={<Signup />} 
      />

      <Route 
        path="/chat" 
        element={<ChatPage />} 
      />

    </Routes>
  );
}

export default App;