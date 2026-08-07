import { useState } from "react";
import { Link } from "react-router-dom";
import api from "../api/api";
import "./Register.css";

function Register() {

    const [form, setForm] = useState({
        username: "",
        email: "",
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

            const response = await api.post("/register", form);

            alert(response.data.message);

            setForm({
                username: "",
                email: "",
                password: "",
            });

        } catch (error) {

            alert("Registration Failed");
            console.error(error);

        }
    };

    return (

        <div className="register-page">

            <div className="register-card">

                <h1>Create Account</h1>

                <p>Begin your journey into destiny</p>

                <form onSubmit={handleSubmit}>

                    <input
                        type="text"
                        name="username"
                        placeholder="Username"
                        value={form.username}
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={form.email}
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
                        Register
                    </button>

                </form>

                <div className="login-link">
                    Already have an account?
                    <br />
                    <Link to="/login">
                        Login
                    </Link>
                </div>

            </div>

        </div>

    );

}

export default Register;