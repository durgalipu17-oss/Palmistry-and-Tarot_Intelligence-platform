import { useState } from "react";
import api from "../api/api";
import "./PalmReading.css";

function PalmReading() {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleAnalyze = async () => {

        if (!file) {
            alert("Please upload a palm image.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        try {

            setLoading(true);

            const response = await api.post(
                "/predict",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            setResult(response.data);

        } catch (error) {

            console.log(error);
            alert("Prediction Failed");

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="palm-page">

            <h1>Upload Palm Image</h1>

            <p>
                Upload a clear image of your palm to receive AI-powered palmistry analysis.
            </p>

            <div className="upload-box">

                <div className="icon">✋</div>

                <input
                    type="file"
                    accept="image/*"
                    onChange={handleFileChange}
                />

                <br /><br />

                <button
                    className="upload-btn"
                    onClick={handleAnalyze}
                >
                    {loading ? "Analyzing..." : "Analyze Palm"}
                </button>

            </div>

            {result && (

                <div className="result-box">

                    <h2>Palm Analysis Result</h2>

                    {/* Personality */}

                    <div className="result-card">

                        <h3>🧠 Personality</h3>

                        <ul>

                            {result.Personality?.personality?.length > 0 ?

                                result.Personality.personality.map((item, index) => (

                                    <li key={index}>{item}</li>

                                ))

                                :

                                <li>No personality insights available.</li>

                            }

                        </ul>

                    </div>

                    {/* Recommendation */}

                    <div className="result-card">

                        <h3>⭐ Recommendations</h3>

                        <ul>

                            {result.Recommendation?.recommendations?.length > 0 ?

                                result.Recommendation.recommendations.map((item, index) => (

                                    <li key={index}>{item}</li>

                                ))

                                :

                                <li>No recommendations available.</li>

                            }

                        </ul>

                    </div>

                    {/* Life Trend */}

                    <div className="result-card">

                        <h3>📈 Life Trend</h3>

                        <p><b>💼 Career:</b> {result["Life Trend"]?.career || "Not Available"}</p>

                        <p><b>❤️ Relationships:</b> {result["Life Trend"]?.relationships || "Not Available"}</p>

                        <p><b>💰 Finance:</b> {result["Life Trend"]?.finance || "Not Available"}</p>

                        <p><b>🏥 Health:</b> {result["Life Trend"]?.health_wellness || "Not Available"}</p>

                        <p><b>🌱 Personal Growth:</b> {result["Life Trend"]?.personal_growth || "Not Available"}</p>

                        <p><b>✨ Overall:</b> {result["Life Trend"]?.overall || "Not Available"}</p>

                    </div>

                </div>

            )}

        </div>

    );

}

export default PalmReading;