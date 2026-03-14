import logging
from sqlalchemy.orm import Session
from opentelemetry import trace

from app.repository import user_repo
from app.metrics.metrics import USER_CREATED

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


def create_user(db: Session, email: str, password: str):

    with tracer.start_as_current_span("user_service.create_user"):

        logger.info(f"Creating user {email}")

        user = user_repo.create_user(db, email, password)

        # business metric
        USER_CREATED.inc()

        logger.info(f"User created successfully {user.id}")

        return user


def list_users(db: Session):

    with tracer.start_as_current_span("user_service.list_users"):

        logger.info("Fetching users")

        return user_repo.get_users(db)