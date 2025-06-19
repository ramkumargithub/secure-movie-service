from fastapi import FastAPI
from app.database import get_movie_details

app = FastAPI()

@app.get("/movie")
def movie_lookup(name: str, year: int = None, language: str = None):
    return get_movie_details(name, year, language)
