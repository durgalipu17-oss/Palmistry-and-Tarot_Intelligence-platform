from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from database import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin, UserUpdate, PasswordUpdate
from security import hash_password, verify_password, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
import sys
import os
import shutil
# Adding the project root (Palmistry_Tarot) to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ai.predict import predict_palm
from ai.tarot.tarot import draw_spread
from services.interpretation import interpret_palm, interpret_tarot
from services.personality import generate_personality
from services.recommendation import generate_recommendations
from services.trends import generate_life_trends
from services.synthesize import synthesize_reading
from models.reading import Reading

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Registered Successfully",
        "user_id": new_user.id
    }



@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    #print("USERNAME RECEIVED:", form_data.username)

    db_user = db.query(User).filter(User.email == form_data.username).first()

    print("USER FOUND:", db_user)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )
    access_token = create_access_token(
        data={"sub": db_user.email}
        )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@router.put("/profile")
def update_profile(
    user: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    current_user.username = user.username
    current_user.email = user.email

    current_user.age = user.age
    current_user.occupation = user.occupation
    current_user.goals = user.goals
    current_user.interests = user.interests
    current_user.reading_style = user.reading_style
    current_user.zodiac = user.zodiac
    current_user.bio = user.bio

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Profile updated successfully",
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "age": current_user.age,
        "occupation": current_user.occupation,
        "goals": current_user.goals,
        "interests": current_user.interests,
        "reading_style": current_user.reading_style,
        "zodiac": current_user.zodiac,
        "bio": current_user.bio
    }

@router.put("/change-password")
def change_password(
    password_data: PasswordUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not verify_password(password_data.old_password, current_user.password):
        return {
            "message": "Old password is incorrect"
        }
    current_user.password = hash_password(password_data.new_password)

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Password updated successfully"
    }

@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction = predict_palm(file_path)

    interpretation = interpret_palm(prediction)
    personality = generate_personality(prediction)
    recommendation = generate_recommendations(prediction)
    life_trends = generate_life_trends(prediction)

   

    palm_text = ""

    for line_name, details in interpretation.items():
        palm_text += (
            f"{line_name.title()}\n"
            f"Meaning : {details['meaning']}\n"
            f"Confidence : {details['confidence']}%\n\n"
        )

    personality_text = "\n".join(personality["personality"])

    recommendation_text = "\n".join(
        recommendation["recommendations"]
    )

    life_trends_text = ""

    for key, value in life_trends.items():
        life_trends_text += f"{key.title()} : {value}\n"


    new_reading = Reading(
        user_id=current_user.id,
        reading_type="palm",
        palm_interpretation=palm_text,
        personality=personality_text,
        recommendation=recommendation_text,
        life_trends=life_trends_text
    )

    db.add(new_reading)
    db.commit()
    db.refresh(new_reading)

    return {
        "interpretation": interpretation,
        "Personality": personality,
        "Recommendation": recommendation,
        "Life Trend": life_trends
    }

@router.get("/tarot/draw")
def tarot_draw(spread: str = "three"):

    spread_data = draw_spread(spread)
    cards = spread_data["cards"]

    tarot_interpretation = interpret_tarot(cards)

    return {
        "message": "Tarot cards drawn successfully.",
        "spread": spread,
        "cards": cards,
        "interpretation": tarot_interpretation
    }

@router.post("/tarot/generate-reading")
def generate_reading(
    spread: str = "three",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    spread_data = draw_spread(spread)
    cards = spread_data["cards"]

    tarot_interpretation = interpret_tarot(cards)

    reading = ""

    for card in cards:
        reading += (
            f"{card['position']}: {card['name']}\n"
            f"{card['fortune_telling'][0]}\n"
            f"{card['light_meanings'][0]}\n\n"
        )

    # Save tarot reading to database
    new_reading = Reading(
        user_id=current_user.id,
        reading_type="tarot",
        tarot_interpretation=str(tarot_interpretation),
        final_reading=reading
    )

    db.add(new_reading)
    db.commit()
    db.refresh(new_reading)

    return {
        "message": "Reading generated successfully.",
        "spread": spread,
        "cards": cards,
        "interpretation": tarot_interpretation,
        "reading": reading
    }

@router.post("/complete-reading")
async def complete_reading(
    file: UploadFile = File(...),
    spread: str = "three",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction = predict_palm(file_path)
    palm_interpretation = interpret_palm(prediction)
    personality = generate_personality(prediction)
    recommendation = generate_recommendations(prediction)
    life_trends = generate_life_trends(prediction)

    tarot_result = draw_spread(spread)
    cards = tarot_result["cards"]    
    tarot_interpretation = interpret_tarot(cards)
    final_reading = synthesize_reading(
        palm_interpretation,
        tarot_interpretation,
        life_trends,
        recommendation
    )

    new_reading = Reading(
    user_id=current_user.id,
    palm_interpretation=str(palm_interpretation),
    personality=str(personality),
    recommendation=str(recommendation),
    life_trends=str(life_trends),
    tarot_interpretation=str(tarot_interpretation),
    final_reading=final_reading
)

    db.add(new_reading)
    db.commit()
    db.refresh(new_reading)


    return {
        "message": "Complete reading generated successfully.",
        "prediction": prediction,
        "palm_interpretation": palm_interpretation,
        "personality": personality,
        "recommendation": recommendation,
        "life_trends": life_trends,
        "tarot_cards": cards,
        "tarot_interpretation": tarot_interpretation,
        "final_reading": final_reading

    }

@router.get("/reading-history")
def get_reading_history(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    readings = (
        db.query(Reading)
        .filter(Reading.user_id == current_user.id)
        .order_by(Reading.created_at.desc())
        .all()
    )
    history = []

    for reading in readings:
        history.append({
            "id": reading.id,
            "created_at": reading.created_at,
            "palm_interpretation": reading.palm_interpretation,
            "personality": reading.personality,
            "recommendation": reading.recommendation,
            "life_trends": reading.life_trends,
            "tarot_interpretation": reading.tarot_interpretation,
            "final_reading": reading.final_reading

        })

    return history