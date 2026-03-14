import time
from app.observability.metrics import DB_QUERY_COUNT, DB_QUERY_LATENCY

async def get_products(db):

    start_time = time.time()

    result = await db.fetch("SELECT * FROM products")

    DB_QUERY_COUNT.labels(query_type="select").inc()

    DB_QUERY_LATENCY.labels(
        query_type="select"
    ).observe(time.time() - start_time)

    return result