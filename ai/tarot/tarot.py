import json
import os
import random

BASE_DIR = os.path.dirname(__file__)

JSON_PATH = os.path.join(BASE_DIR, "tarot-images.json")
print(JSON_PATH)
with open(JSON_PATH, "r", encoding="utf-8") as f:
    tarot_data = json.load(f)

SPREADS = {
    "single": [
        "Today's Guidance"
    ],

    "three": [
        "Past",
        "Present",
        "Future"
    ],

    "relationship": [
        "You",
        "Partner",
        "Relationship"
    ],

    "career": [
        "Current Situation",
        "Challenge",
        "Advice"
    ]
}

cards = tarot_data["cards"]

def draw_spread(spread_type="three"):
    if spread_type not in SPREADS:
        raise ValueError("Invalid spread type.")
    positions = SPREADS[spread_type]
    selected_cards = random.sample(cards, len(positions))
    result = []
    for position, card in zip(positions, selected_cards):
        result.append({
            "position": position,
            "name": card["name"],
            "number": card["number"],
            "arcana": card["arcana"],
            "suit": card["suit"],
            "image": card["img"],
            "keywords": card["keywords"],
            "fortune_telling": card["fortune_telling"],
            "light_meanings": card["meanings"]["light"],
            "shadow_meanings": card["meanings"]["shadow"]
        })
    return {
        "spread": spread_type,
        "cards": result
    }
   
if __name__ == "__main__":
    result = draw_spread("three")
    print(json.dumps(result, indent=4))