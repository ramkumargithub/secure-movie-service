from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from .database import get_movie_by_details
from .security import add_security_headers
from pydantic import BaseModel, constr
from fastapi import FastAPI

app = FastAPI()

# Security Middleware
@app.middleware("http")
async def security_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    return add_security_headers(response)

# Force HTTPS (optional, remove if testing locally)
# app.add_middleware(HTTPSRedirectMiddleware)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MovieQuery(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    year: int
    language: constr(strip_whitespace=True, min_length=2)

@app.post("/movie")
async def get_movie(query: MovieQuery):
    movie = get_movie_by_details(query.name, query.year, query.language)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return JSONResponse(content=movie)

@app.get("/health")
async def healthcheck():
    return {"status": "ok"}
