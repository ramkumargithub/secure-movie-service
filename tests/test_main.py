import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app

@pytest.mark.asyncio
async def test_healthcheck():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_get_suggestions_valid_genre():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/suggestions?genre=action")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all("title" in movie for movie in response.json())

@pytest.mark.asyncio
async def test_get_suggestions_invalid_genre():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/suggestions?genre=invalid_genre")
    assert response.status_code in [400, 404]

@pytest.mark.asyncio
async def test_get_movie_by_id_success():
    # This assumes you have a movie with ID "1"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/movies/1")
    assert response.status_code == 200
    assert "title" in response.json()

@pytest.mark.asyncio
async def test_get_movie_by_id_not_found():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/movies/9999")
    assert response.status_code == 404
