from fastapi import APIRouter, Response

from app.external.metrics.prometheus import metrics as prom_metrics

base_router = APIRouter()
base_tags = ["base"]


@base_router.get("/health", tags=base_tags)
async def health():
    return {"status": "OK"}


@base_router.get("/metrics", tags=base_tags)
async def metrics():
    body, media_type = prom_metrics()
    return Response(body, media_type=media_type)
