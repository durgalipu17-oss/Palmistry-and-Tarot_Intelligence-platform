from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

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
    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user:
        return {"message": "User not found"}

    if not verify_password(form_data.password, db_user.password):
        return {"message": "Invalid password"}

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

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Profile updated successfully",
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
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
async def predict(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict_palm(file_path)

    return result

@router.get("/tarot/draw")
def tarot_draw(spread: str = "three"):

    cards = draw_spread(spread)

    return {
        "message": "Tarot cards drawn successfully.",
        "cards": cards
    }