import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    console.log("USERNAME SENT:", username);
    console.log("PASSWORD SENT:", password);

    try {

        const response = await api.post(
            "login/",
            {
                username: username.trim(),
                password: password.trim(),
            }
        );

        console.log("LOGIN RESPONSE:", response.data);

        localStorage.setItem(
            "access",
            response.data.access
        );

        localStorage.setItem(
            "refresh",
            response.data.refresh
        );

        navigate("/chat");

    } catch(error) {

        console.error(
            "LOGIN ERROR:",
            error.response?.data
        );

    }
};
  return (
    <div style={{ width: "350px", margin: "100px auto" }}>
      <h2>Login</h2>

      <form onSubmit={handleLogin}>

        <div>
          <label>Username</label>
          <br />

          <input
            type="text"
            value={username}
            onChange={(e) =>
              setUsername(e.target.value)
            }
            required
          />
        </div>


        <br />


        <div>
          <label>Password</label>
          <br />

          <input
            type="password"
            value={password}
            onChange={(e) =>
              setPassword(e.target.value)
            }
            required
          />
        </div>


        <br />


        <button type="submit">
          Login
        </button>

      </form>


      <br />


      {message && (
        <p>{message}</p>
      )}

    </div>
  );
}

export default Login;