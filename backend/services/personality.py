def generate_personality(predictions):

    personality = []

    # Head Line
    if predictions["head"]["present"]:
        if predictions["head"]["confidence"] > 0.75:
            personality.append("Strong analytical and logical thinker.")
        else:
            personality.append("Practical thinker with balanced reasoning.")

    # Heart Line
    if predictions["heart"]["present"]:
        if predictions["heart"]["confidence"] > 0.75:
            personality.append("Emotionally expressive and compassionate.")
        else:
            personality.append("Emotionally balanced and calm.")

    # Fate Line
    if predictions["fate"]["present"]:
        if predictions["fate"]["confidence"] > 0.75:
            personality.append("Career-oriented and ambitious.")
        else:
            personality.append("Focused on steady personal growth.")

    # Life Line
    if predictions["life"]["present"]:
        if predictions["life"]["confidence"] > 0.75:
            personality.append("Energetic and resilient.")
        else:
            personality.append("Maintains a balanced lifestyle.")

    # Palm Width
    if predictions["palm_width"]["present"]:
        if predictions["palm_width"]["confidence"] > 0.75:
            personality.append("Confident and action-oriented.")
        else:
            personality.append("Thoughtful before taking action.")

    # Line Density
    if predictions["line_density"]["present"]:
        if predictions["line_density"]["confidence"] > 0.75:
            personality.append("Highly observant and detail-focused.")
        else:
            personality.append("Simple and straightforward personality.")

    return {
        "personality": personality
    }