def generate_life_trends(predictions):

    trends = {}

    # Personality
    if predictions["head"]["confidence"] >= 0.70:
        trends["personality"] = (
            "You have a logical and analytical personality with good decision-making abilities."
        )
    else:
        trends["personality"] = (
            "You are creative and adaptable, but strengthening planning skills will help you grow."
        )

    # Career
    if predictions["fate"]["confidence"] >= 0.70:
        trends["career"] = (
            "Your career path appears stable with strong long-term growth potential."
        )
    else:
        trends["career"] = (
            "Career progress may take time, but persistence and continuous learning will help."
        )

    # Relationships
    if predictions["heart"]["confidence"] >= 0.70:
        trends["relationships"] = (
            "You are capable of building meaningful and emotionally balanced relationships."
        )
    else:
        trends["relationships"] = (
            "Open communication and patience will strengthen your relationships."
        )

    # Finance
    if predictions["fate"]["confidence"] >= 0.70:
        trends["finance"] = (
            "Your financial future appears stable with disciplined decision-making."
        )
    else:
        trends["finance"] = (
            "Careful planning and consistent saving will improve financial stability."
        )

    # Health & Wellness
    if predictions["life"]["confidence"] >= 0.70:
        trends["health_wellness"] = (
            "Your palm suggests good vitality and overall well-being."
        )
    else:
        trends["health_wellness"] = (
            "Maintaining healthy daily habits and managing stress will support your well-being."
        )

    # Personal Growth
    if predictions["head"]["confidence"] >= 0.70:
        trends["personal_growth"] = (
            "You have strong potential for continuous learning and leadership."
        )
    else:
        trends["personal_growth"] = (
            "Developing confidence and improving decision-making will accelerate your growth."
        )

    # Life Opportunities
    confidence = (
        predictions["head"]["confidence"] +
        predictions["heart"]["confidence"] +
        predictions["life"]["confidence"] +
        predictions["fate"]["confidence"]
    ) / 4

    if confidence >= 0.70:
        trends["life_opportunities"] = (
            "Your overall palm analysis indicates positive opportunities in multiple areas of life."
        )
    else:
        trends["life_opportunities"] = (
            "Future opportunities will arise gradually as you continue developing your skills and experience."
        )

    # Overall Summary
    trends["overall"] = (
        "This analysis is generated from detected palm features and is intended for educational and entertainment purposes."
    )

    return trends