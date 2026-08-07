from models.reading import Reading
import ast


def get_user_dashboard(db, user_id):

    readings = (
        db.query(Reading)
        .filter(Reading.user_id == user_id)
        .order_by(Reading.created_at.desc())
        .all()
    )

    recent_readings = []

    for reading in readings[:5]:
        recent_readings.append({
            "id": reading.id,
            "created_at": reading.created_at,

            "palm_interpretation": ast.literal_eval(reading.palm_interpretation),
            "personality": ast.literal_eval(reading.personality),
            "recommendation": ast.literal_eval(reading.recommendation),
            "life_trends": ast.literal_eval(reading.life_trends),
            "tarot_interpretation": ast.literal_eval(reading.tarot_interpretation),
            "final_reading": reading.final_reading
        })

    return {
        "total_readings": len(readings),
        "recent_readings": recent_readings
    }