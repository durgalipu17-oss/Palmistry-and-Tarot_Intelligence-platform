import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_personalized_reading(profile, palm, tarot):
    palm= palm or {}
    
    prompt = f"""
You are an AI life-insight assistant.

Generate a personalized palmistry and tarot interpretation.

User Profile:
- Age: {profile.age if profile else 'Unknown'}
- Occupation: {profile.occupation if profile else 'Unknown'}
- Goals: {profile.goals if profile else 'Unknown'}
- Interests: {profile.interests if profile else 'Unknown'}
- Zodiac: {profile.zodiac if profile else 'Unknown'}
- Bio: {profile.bio if profile else 'Unknown'}

Palm analysis:
{palm if isinstance(palm, str) else f'''
- Life line: {palm.get('life', 'Unknown')}
- Head line: {palm.get('head', 'Unknown')}
- Heart line: {palm.get('heart', 'Unknown')}
- Fate line: {palm.get('fate', 'Unknown')}
'''}


Tarot Reading:
{tarot}

Generate a personalized reading section:
1. Personality summary(3-4 points)
2. Career guidance(3-4 points)
3. Relationship guidance(3-4 points)
4. Health and wellness advice(3-4 points)
5. Growth opportunities(3-4 points)
6. 5 practical recommendations point wise

Keep it positive, realistic, and concise.
"""



    response = client.models.generate_content(
    model="models/gemini-flash-lite-latest",
    contents=prompt,
)

    return response.text.replace("\\\\n", "\\n")