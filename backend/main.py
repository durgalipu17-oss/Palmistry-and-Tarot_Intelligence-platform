from fastapi import FastAPI
from database import engine, Base
from models.user import User
from models.reading import Reading
from routers.user import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from routers.dashboard import router as dashboard_router
from fastapi.staticfiles import StaticFiles
from pathlib import Path
# from dotenv import load_dotenv
# load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://palmistry-and-tarot-intelligence-pl.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
app.include_router(dashboard_router)

cards_path = Path(__file__).parent / "ai" / "tarot" / "cards"

app.mount(
    "/tarot-cards",
    StaticFiles(directory=cards_path),
    name="tarot-cards"
)

@app.get("/")
def home():
    return {
        "message": "Palmistry & Tarot API is running successfully."
    }