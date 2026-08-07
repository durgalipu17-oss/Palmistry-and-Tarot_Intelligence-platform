from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    reading_type = Column(String)


    palm_interpretation = Column(Text)
    personality = Column(Text)
    recommendation = Column(Text)
    life_trends = Column(Text)
    tarot_interpretation = Column(Text)
    final_reading = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")