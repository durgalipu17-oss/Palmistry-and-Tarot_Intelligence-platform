import { useState } from "react";
import api from "../api/api";
import "./PalmReading.css";

function PalmReading() {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [llmReading, setLlmReading] = useState('');
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
            const llmResponse = await api.get('/llm-reading');
            setLlmReading(llmResponse.data.llm_reading);
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

                    {/* Normal image upload */}
                    <input
                        type="file"
                        accept="image/*"
                        onChange={handleFileChange}
                    />

                    <br />

                    {/* Camera button */}
                    <label htmlFor="camera-input" className="camera-btn">
                        📷 Take Photo
                    </label>

                    <input
                        id="camera-input"
                        type="file"
                        accept="image/*"
                        capture="environment"
                        onChange={handleFileChange}
                        style={{ display: "none" }}
                    />

                    <br /><br />

                    <button
                        className="upload-btn"
                        onClick={handleAnalyze}
                    >
                        {loading ? "Analyzing..." : "Analyze Palm"}
                    </button>
            
                    {llmReading && (
                        <div className='result-card'>
                            <h3>🔮 AI Personalized Reading</h3>

                            <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.8' }}>
                                 {llmReading 
                                 .replaceAll('### ', ' 🔹 ') 
                                 .replaceAll('## ', ' ✨ ') 
                                 .replaceAll('**', '') 
                                 .replaceAll('* ', '• ') }
                             </div>
                        </div>
                    )}
                </div>
            
        </div>
    );
}
export default PalmReading;