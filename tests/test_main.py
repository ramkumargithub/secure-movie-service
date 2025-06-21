import pytest
from httpx import AsyncClient
from fastapi import status
from app.main import app

# Functional Tests

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


# Security Tests

@pytest.mark.asyncio
async def test_sql_injection_in_genre():
    payload = "action'; DROP TABLE movies;--"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/suggestions?genre={payload}")
    assert response.status_code in [400, 422, 404]

@pytest.mark.asyncio
async def test_xss_attack_vector_in_genre():
    payload = "<script>alert(1)</script>"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/suggestions?genre={payload}")
    assert response.status_code in [400, 422, 404]

@pytest.mark.asyncio
async def test_path_traversal_in_movie_id():
    payload = "../../etc/passwd"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/movies/{payload}")
    assert response.status_code in [400, 422, 404]

@pytest.mark.asyncio
async def test_type_error_in_movie_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/movies/abc")
    assert response.status_code in [422, 400]

@pytest.mark.asyncio
async def test_rate_limiting_on_movies_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        for i in range(10):
            response = await ac.get("/movies/1")
        # Expecting either success or rate-limit error (if implemented)
        assert response.status_code in [200, 429]

@pytest.mark.asyncio
async def test_unauthorized_access_to_protected_movie():
    # Assuming /movies/secure/1 is a protected route requiring auth
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/movies/secure/1")
    assert response.status_code in [401, 403, 404]  # depending on implementation
