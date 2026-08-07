
LINE_MEANINGS = {

    "head": {
        "Strong": "Strong analytical thinking and excellent decision-making ability.",
        "Moderate": "Balanced reasoning with practical problem-solving skills.",
        "Weak": "May benefit from improving focus and planning abilities."
    },

    "heart": {
        "Strong": "Emotionally balanced, compassionate, and empathetic.",
        "Moderate": "Stable emotional nature with good interpersonal skills.",
        "Weak": "May need to improve emotional communication and self-expression."
    },

    "life": {
        "Strong": "Good vitality, resilience, and adaptability.",
        "Moderate": "Average energy levels with room for healthy lifestyle improvements.",
        "Weak": "Focus on maintaining physical and mental well-being."
    },

    "fate": {
        "Strong": "Clear career direction with consistent progress.",
        "Moderate": "Career growth through continuous effort and learning.",
        "Weak": "Career path may involve changes and exploration."
    },

    "palm_width": {
        "Strong": "Broad palm suggests practicality and adaptability.",
        "Moderate": "Balanced palm proportions indicating a well-rounded personality.",
        "Weak": "Narrow palm may indicate careful planning and attention to detail."
    },

    "line_density": {
        "Strong": "Many visible palm lines indicate an active and expressive personality.",
        "Moderate": "Balanced line density reflects emotional stability and flexibility.",
        "Weak": "Fewer palm lines suggest a calm and straightforward personality."
    }

}


def get_visibility(score):
    
    if score >= 0.80:
        return "Strong"

    elif score >= 0.50:
        return "Moderate"

    else:
        return "Weak"


def interpret_palm(predictions):   
    interpreted = {}
    for feature, value in predictions.items():
        confidence = value["confidence"]
        visibility = get_visibility(confidence)
        interpreted[feature] = {
            "present": value["present"],
            "confidence": round(confidence * 100, 2),
            "visibility": visibility,
            "meaning": LINE_MEANINGS[feature][visibility]
        }

    return interpreted


def interpret_tarot(cards):
    
    tarot_interpretation = {}
    for card in cards:
        position = card["position"].lower()
        interpretation = ""
        if card.get("fortune_telling"):
            interpretation += card["fortune_telling"][0]
        if card.get("light_meanings"):
            interpretation += " " + card["light_meanings"][0]
        tarot_interpretation[position] = {
            "card": card["name"],
            "meaning": interpretation.strip()
        }
    return tarot_interpretation