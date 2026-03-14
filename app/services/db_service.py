import time
import random
from app.observability.metrics import DB_QUERY_COUNT, DB_QUERY_LATENCY

async def run_sample_query():

    start = time.time()

    # simulate DB query
    time.sleep(random.uniform(0.05, 0.3))

    DB_QUERY_COUNT.labels(query_type="select").inc()

    DB_QUERY_LATENCY.labels(
        query_type="select"
    ).observe(time.time() - start)

    return {"status": "query executed"}