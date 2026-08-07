def generate_recommendations(predictions):
    recommendations = []
    # Head Line
    if predictions["head"]["confidence"] >= 0.75:
        recommendations.append(
            "Your analytical abilities are strong. Consider careers involving research, engineering, or technology."
        )
    else:
        recommendations.append(
            "Practice problem-solving and critical thinking to strengthen your analytical skills."
        )
    # Heart Line
    if predictions["heart"]["confidence"] >= 0.75:
        recommendations.append(
            "Your emotional intelligence is a strength. Build meaningful relationships and mentor others."
        )
    else:
        recommendations.append(
            "Improve communication and emotional awareness through teamwork and active listening."
        )
    # Fate Line
    if predictions["fate"]["confidence"] >= 0.75:
        recommendations.append(
            "Focus on long-term career goals and leadership opportunities."
        )
    else:
        recommendations.append(
            "Explore different career paths before making long-term commitments."
        )

    # Life Line
    if predictions["life"]["confidence"] >= 0.75:
        recommendations.append(
            "Maintain your healthy lifestyle and continue regular physical activity."
        )
    else:
        recommendations.append(
            "Prioritize rest, exercise, and stress management."
        )
    # Palm Width
    if predictions["palm_width"]["confidence"] >= 0.75:
        recommendations.append(
            "Take initiative in challenging situations and leadership roles."
        )
    else:
        recommendations.append(
            "Build confidence by taking small, consistent leadership responsibilities."
        )
    # Line Density
    if predictions["line_density"]["confidence"] >= 0.75:
        recommendations.append(
            "Your attention to detail is valuable. Consider roles requiring precision."
        )
    else:
        recommendations.append(
            "Develop planning and organizational habits to improve productivity."
        )
    return {
        "recommendations": recommendations
    }