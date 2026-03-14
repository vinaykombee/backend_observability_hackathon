from fastapi import APIRouter

router = APIRouter()

@router.get("/logs")
async def get_logs():

    with open("logs/app.log") as f:
        lines = f.readlines()[-100:]

    return {"logs": lines}