import { useEffect, useState } from "react";
import api from "../api/api";
import "./ReadingHistory.css";

function ReadingHistory() {

    const [history, setHistory] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {

        fetchHistory();

    }, []);

    const fetchHistory = async () => {

        try {

            const token = localStorage.getItem("token");

            const response = await api.get("/reading-history", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            setHistory(response.data);

        }

        catch (error) {

            console.log(error);

        }

        finally {

            setLoading(false);

        }

    };

    if (loading) {

        return <h2>Loading...</h2>;

    }

    return (

        <div className="history-page">

            <h1>📜 Reading History</h1>

            {

                history.length === 0 ?

                    (

                        <p>No readings found.</p>

                    )

                    :

                    (

                        history.map((item) => (

                            <div
                                className="history-card"
                                key={item.id}
                            >

                                <h3>

                                    Reading #{item.id}

                                </h3>

                                <p>

                                    <b>Date:</b>

                                    {" "}

                                    {new Date(item.created_at).toLocaleString()}

                                </p>

                                {

                                    item.final_reading && (

                                        <>

                                            <h4>🔮 Tarot Reading</h4>

                                            <p>{item.final_reading}</p>

                                        </>

                                    )

                                }

                                {item.personality && (
                                    <>
                                        <h4>🖐 Palm Reading</h4>

                                        <b>Palm Interpretation</b>
                                        <p style={{ whiteSpace: "pre-line" }}>
                                            {item.palm_interpretation}
                                        </p>

                                        <b>Personality</b>
                                        <p style={{ whiteSpace: "pre-line" }}>
                                            {item.personality}
                                        </p>

                                        <b>Recommendations</b>
                                        <p style={{ whiteSpace: "pre-line" }}>
                                            {item.recommendation}
                                        </p>

                                        <b>Life Trends</b>
                                        <p style={{ whiteSpace: "pre-line" }}>
                                            {item.life_trends}
                                        </p>
                                    </>
                                )}

                            </div>

                        ))

                    )

            }

        </div>

    );

}

export default ReadingHistory;