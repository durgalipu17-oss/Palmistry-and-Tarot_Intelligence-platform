import "./Landing.css";
import { Link } from "react-router-dom";

function Landing() {

    return (

        <div className="landing">

            <div className="content">

                <h1>Palmistry & Tarot</h1>

                <h3>
                    Put your hand and know your future
                </h3>

                <div className="buttons">

                    <Link to="/login">
                        <button className="login-btn">
                            Login
                        </button>
                    </Link>

                    <Link to="/register">
                        <button className="register-btn">
                            Register
                        </button>
                    </Link>

                </div>

            </div>

        </div>

    );

}

export default Landing;