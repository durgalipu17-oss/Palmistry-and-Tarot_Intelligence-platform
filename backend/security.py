from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    print("TOKEN:", token)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("PAYLOAD:", payload)

        email = payload.get("sub")
        print("EMAIL:", email)

        if email is None:
            raise credentials_exception

    except Exception as e:
        print("JWT ERROR:", e)
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()

    print("USER FOUND:", user)

    if user is None:
        raise credentials_exception

    return user
# def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials")

#     try:
#         payload = jwt.decode(
#             token,
#             SECRET_KEY,
#             algorithms=[ALGORITHM]
#         )

#         email = payload.get("sub")

#         if email is None:
#             raise credentials_exception

#     except JWTError:
#         raise credentials_exception
#     user = db.query(User).filter(User.email == email).first()

#     if user is None:
#         raise credentials_exception

#     return user




def hash_password(password: str):
    
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt