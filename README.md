# Observability Hackathon

FastAPI sample app instrumented with Prometheus metrics and OpenTelemetry tracing, plus a local observability stack (Prometheus, Grafana, Loki, Tempo, Promtail) via Docker Compose.

![Grafana Dashboard](grafana.png)

**Stack**
- App: FastAPI + SQLAlchemy + PostgreSQL
- Metrics: Prometheus + `prometheus-client`
- Tracing: OpenTelemetry + Tempo
- Logs: Promtail + Loki
- Dashboards: Grafana provisioning in `grafana/`

**Quickstart**
```bash
docker compose up --build
```

**Service Ports**
- `app` (FastAPI): `http://localhost:8000`
- `prometheus`: `http://localhost:9090`
- `grafana`: `http://localhost:3000` (user: `admin`, password: `admin`)
- `loki`: `http://localhost:3100`
- `tempo`: `http://localhost:3200`
- `postgres`: `localhost:5432`

**API Endpoints (currently wired in app startup)**
- `GET /latency-test` (simulated latency)
- `GET /db-test` (simulated DB query + metrics)
- `GET /error-test` (500 error generator)
- `GET /health`
- `GET /metrics` (Prometheus scrape)

**Additional Routers (present but not wired in startup)**
To enable these, include their routers in `app/main.py`.
- `app/api/auth.py` (`/auth/login`)
- `app/api/users.py` (`/users`)
- `app/api/products.py` (`/products`)
- `app/api/orders.py` (`/orders`)
- `app/api/logs.py` (`/logs`)
- `app/anomaly/anomaly_routes.py` (`/slow-api`, `/cpu-spike`)
- `app/routes/*` (alternative auth/users/health samples)

**Observability**
- Prometheus scrapes `GET /metrics` from the app.
- Grafana datasources are pre-provisioned in `grafana/provisioning/`.
- Dashboards live in `grafana/dashboards/`.
- Tempo is configured for OTLP on ports `4317` (gRPC) and `4318` (HTTP).
- Promtail ships Docker container logs to Loki.

**Load Testing**
The `load-test/load.js` script uses k6 to hit a mix of endpoints.
```bash
k6 run load-test/load.js
```

**Notes**
- The container uses `DATABASE_URL=postgresql://postgres:postgres@postgres:5432/hackathon` from `docker-compose.yml`.
- If you run the app outside Docker, set `DATABASE_URL` accordingly.
