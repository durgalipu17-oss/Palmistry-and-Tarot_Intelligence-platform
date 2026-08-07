def synthesize_reading(
    palm_interpretation,
    tarot_interpretation,
    life_trends,
    recommendations
):
    reading = []

    # Palm Summary
    reading.append(" Palm Analysis")
    for feature, value in palm_interpretation.items():
        reading.append(f"- {feature.capitalize()}: {value['meaning']}")

    # Tarot Summary
    reading.append("\n Tarot Reading")
    for position, card in tarot_interpretation.items():
        reading.append(
            f"- {position.capitalize()}: {card['card']} - {card['meaning']}"
        )

    # Life Trends
    reading.append("\n Life Trend Analysis")
    for category, text in life_trends.items():

        if category == "overall":
            continue

        reading.append(
            f"- {category.replace('_',' ').title()}: {text}"
        )

    # Recommendations
    reading.append("\n Personalized Guidance")

    for tip in recommendations:
        reading.append(f"- {tip}")

    return "\n".join(reading)