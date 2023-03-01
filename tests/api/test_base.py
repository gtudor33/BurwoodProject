import pytest


@pytest.mark.asyncio
async def test_health(client):
    async with client as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


@pytest.mark.asyncio
async def test_metrics(client):
    async with client as ac:
        response = await ac.get("/metrics")
    assert response.status_code == 200
    assert response.text.startswith("# HELP python_gc_objects_collected_total")
