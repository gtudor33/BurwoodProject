import pytest


@pytest.mark.asyncio
async def test_fizzbuzz_less_than_1(client):
    async with client as ac:
        response = await ac.post("/fizzbuzz", data={"number": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Must submit a number greater than 0!"}


@pytest.mark.asyncio
async def test_fizzbuzz_non_int(client):
    async with client as ac:
        response = await ac.post("/fizzbuzz", data={"number": "a"})
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


@pytest.mark.asyncio
async def test_fizzbuzz(client):
    async with client as ac:
        response = await ac.post("/fizzbuzz", data={"number": 15})
    assert response.status_code == 200
    assert response.json() == {"result": "FizzBuzz"}


@pytest.mark.asyncio
async def test_fizz(client):
    async with client as ac:
        response = await ac.post("/fizzbuzz", data={"number": 3})
    assert response.status_code == 200
    assert response.json() == {"result": "Fizz"}


@pytest.mark.asyncio
async def test_buzz(client):
    async with client as ac:
        response = await ac.post("/fizzbuzz", data={"number": 5})
    assert response.status_code == 200
    assert response.json() == {"result": "Buzz"}


@pytest.mark.asyncio
async def test_most_common(client):
    async with client as ac:
        await ac.post("/fizzbuzz", data={"number": 3})
        response = await ac.get("/most_common")
    assert response.status_code == 200
    assert response.json() == {"result": [[3, 2], [15, 1], [5, 1]]}
