from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import generate_latest
from app.middleware.metrics_middleware import MetricsMiddleware
from app.api.test_api import router
import logging


app = FastAPI()

app.add_middleware(MetricsMiddleware)

app.include_router(router)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi")

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")