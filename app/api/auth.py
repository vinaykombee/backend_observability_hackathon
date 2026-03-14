from fastapi import APIRouter
import logging

router = APIRouter(prefix="/auth")

logger = logging.getLogger(__name__)


@router.get("/login")
def login():

    logger.info("Login endpoint accessed")

    return {"message": "login success"}