from fastapi import FastAPI
from database import engine, Base
from models.user import User
from routers.user import router as user_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "Palmistry & Tarot API is running"}
