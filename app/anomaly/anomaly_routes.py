from fastapi import APIRouter
import time

router = APIRouter()

@router.get("/slow-api")
def slow_api():
    time.sleep(3)
    return {"message": "slow endpoint"}

@router.get("/cpu-spike")
def cpu_spike():
    for i in range(10**7):
        pass
    return {"message": "cpu spike triggered"}