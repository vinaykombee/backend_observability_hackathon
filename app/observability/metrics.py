from prometheus_client import Counter, Histogram

# -----------------------------
# API Metrics
# -----------------------------

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Request latency",
    ["endpoint"]
)

# -----------------------------
# DB Metrics
# -----------------------------

DB_QUERY_COUNT = Counter(
    "db_queries_total",
    "Total DB Queries",
    ["query_type"]
)

DB_QUERY_LATENCY = Histogram(
    "db_query_latency_seconds",
    "DB query latency",
    ["query_type"]
)

# -----------------------------
# Error Metrics
# -----------------------------

ERROR_COUNT = Counter(
    "http_errors_total",
    "Total HTTP Errors",
    ["endpoint", "status"]
)