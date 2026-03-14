import time
from starlette.middleware.base import BaseHTTPMiddleware
from app.observability.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY,
    ERROR_COUNT
)

class MetricsMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.time()

        try:
            response = await call_next(request)
            status = response.status_code
        except Exception:
            status = 500
            ERROR_COUNT.labels(
                endpoint=request.url.path,
                status=status
            ).inc()
            raise

        duration = time.time() - start_time

        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=status
        ).inc()

        REQUEST_LATENCY.labels(
            endpoint=request.url.path
        ).observe(duration)

        if status >= 400:
            ERROR_COUNT.labels(
                endpoint=request.url.path,
                status=status
            ).inc()

        return response