import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api/api";
import "./Login.css";


function Login() {

    const navigate = useNavigate();

    const [form, setForm] = useState({
        username: "",
        password: "",
    });

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {

            const data = new URLSearchParams();

            data.append("username", form.username);
            data.append("password", form.password);

            const response = await api.post(
                "/login",
                data,
                {
                    headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    },
                }
        );
            console.log("LOGIN RESPONSE:", response.data);

            localStorage.setItem(
                "token",
                response.data.access_token
            );
            console.log("ACCESS TOKEN:", response.data.access_token);
            console.log("STORED TOKEN:", localStorage.getItem("token"));
            alert("Login Successful");

            navigate("/dashboard");

        }

        // catch (error) {

        //     alert("Invalid Username or Password");
        //     console.error(error);

        // }

        catch (error) {
            console.error("LOGIN ERROR:", error);

            if (error.response) {
                if (error.response.status === 401) {
                    alert("Invalid Username or Password");
                } else {
                    alert(`Login failed. Server returned ${error.response.status}`);
                }
            } else if (error.request) {
                alert("Unable to reach the server. Please check your internet connection.");
            } else {
                alert("Something went wrong. Please try again.");
            }
}

    };

    return (

        <div className="login-page">

            <div className="login-card">

                <h1>Welcome Back</h1>

                <p>Login to continue your journey</p>

                <form onSubmit={handleSubmit}>

                    <input
                        type="text"
                        name="username"
                        placeholder="Email"
                        value={form.username}
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        value={form.password}
                        onChange={handleChange}
                        required
                    />

                    <button type="submit">
                        Login
                    </button>

                </form>

                <div className="register-link">

                    Don't have an account?

                    <br />

                    <Link to="/register">
                        Register
                    </Link>

                </div>

            </div>

        </div>

    );

}

export default Login;