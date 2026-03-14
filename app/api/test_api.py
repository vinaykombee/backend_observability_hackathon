from fastapi import APIRouter, HTTPException
import random
import time
from app.services.db_service import run_sample_query

router = APIRouter()


@router.get("/latency-test")
async def latency_test():
    time.sleep(random.uniform(0.1, 0.5))
    return {"message": "latency generated"}


@router.get("/db-test")
async def db_test():
    return await run_sample_query()


@router.get("/error-test")
async def error_test():
    raise HTTPException(status_code=500, detail="Simulated error")


@router.get("/health")
async def health():
    return {"status": "ok"}