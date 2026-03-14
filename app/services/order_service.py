from opentelemetry import trace
import time
from app.repository import order_repo

tracer = trace.get_tracer(__name__)


def create_order(db, user_id, product_id):

    with tracer.start_as_current_span("order_service.create_order"):

        # simulate heavy processing
        time.sleep(0.3)

        return order_repo.create_order(db, user_id, product_id)