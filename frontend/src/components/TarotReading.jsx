import { useState } from "react";
import "./TarotReading.css";

import deck from "../assets/images/tarot-deck.png";
import cardBack from "../assets/images/card-back.png";
import api from "../api/api";

function TarotReading() {

    const [shuffling, setShuffling] = useState(false);
    const [showCards, setShowCards] = useState(false);
    const [selectedCards, setSelectedCards] = useState([]);
    const [loading, setLoading] = useState(false);
    const [reading, setReading] = useState(null);

    const cards = Array.from({ length: 12 }, (_, i) => i);

    const handleShuffle = () => {

        setShuffling(true);

        setTimeout(() => {

            setShuffling(false);
            setShowCards(true);

        }, 2000);

    };

    const handleSelect = (index) => {

        if (selectedCards.includes(index)) return;

        if (selectedCards.length === 3) return;

        setSelectedCards([...selectedCards, index]);

    };

    const handleReveal = async () => {

    try {

        setLoading(true);

        const response = await api.post("/tarot/generate-reading");

        setReading(response.data);

    }

    catch (error) {

        console.log(error);

        alert("Unable to generate reading.");

    }

    finally {

        setLoading(false);

    }

};

    return (

        <div className="tarot-page">

            <div className="tarot-card">

                <h1>🔮 Tarot Reading</h1>

                <p>
                    Shuffle the mystical deck and let the universe guide your cards.
                </p>

                {!showCards && (

                    <>

                        <img
                            src={deck}
                            alt="Tarot Deck"
                            className={shuffling ? "deck-image shake" : "deck-image"}
                        />

                        <button
                            className="shuffle-btn"
                            onClick={handleShuffle}
                            disabled={shuffling}
                        >
                            {shuffling ? "Shuffling..." : "Shuffle Deck"}
                        </button>

                    </>

                )}

                {showCards && (

                    <>

                        <h2 className="choose-text">
                            Choose Any 3 Cards
                        </h2>

                        <div className="cards-grid">

                            {cards.map((card, index) => (

                                <div
                                    key={index}
                                    className={`card-wrapper ${selectedCards.includes(index) ? "selected" : ""}`}
                                    onClick={() => handleSelect(index)}
                                >

                                    <img
                                        src={
                                            reading && selectedCards.includes(index)
                                                ? `https://palmistry-and-tarotintelligence-platform-production.up.railway.app/tarot-cards/${reading.cards[selectedCards.indexOf(index)].image}`
                                                : cardBack
                                        }
                                        alt="card"
                                        className="tarot-back"
                                    />

                                    {reading && selectedCards.includes(index) && (
                                        <>
                                            <h3 className="card-name">
                                                {reading.cards[selectedCards.indexOf(index)].name}
                                            </h3>

                                            <p className="card-position">
                                                {reading.cards[selectedCards.indexOf(index)].position}
                                            </p>
                                        </>
                                    )}

                                    {selectedCards.includes(index) && (

                                        <span className="position-tag">

                                            {
                                                selectedCards.indexOf(index) === 0
                                                    ? "Past"
                                                    : selectedCards.indexOf(index) === 1
                                                        ? "Present"
                                                        : "Future"
                                            }

                                        </span>

                                    )}

                                </div>

                            ))}

                        </div>

                        {selectedCards.length === 3 && (

                            <button
                                className="shuffle-btn reveal-btn"
                                onClick={handleReveal}
                                disabled={loading}
                            >

                                {loading ? "Generating..." : "Reveal Reading"}

                            </button>

                        )}

                        {reading && (

                        <div className="reading-box">

                            <h2>🔮 Your Tarot Reading</h2>

                            {reading.cards.map((card,index)=>(

                                <div
                                    className="reading-card"
                                    key={index}
                                >

                                    <h3>

                                        {card.position} • {card.name}

                                    </h3>

                                    <p>

                                        <strong>Fortune</strong>

                                    </p>

                                    <ul>

                                        {card.fortune_telling.map((item,i)=>(

                                            <li key={i}>{item}</li>

                                        ))}

                                    </ul>

                                    <p>

                                        <strong>Meaning</strong>

                                    </p>

                                    <ul>

                                        {card.light_meanings.map((item,i)=>(

                                            <li key={i}>{item}</li>

                                        ))}

                                    </ul>

                                </div>

                            ))}

                        </div>

                        )}

                    </>

                )}

            </div>

        </div>

    );

}

export default TarotReading;