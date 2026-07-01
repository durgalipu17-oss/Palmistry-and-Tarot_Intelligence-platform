from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Palmistry & Tarot API is running"}