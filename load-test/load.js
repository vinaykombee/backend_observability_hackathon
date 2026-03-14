import http from "k6/http";
import { sleep, check } from "k6";

export const options = {
  vus: 1000,
  duration: "60s",
};

const BASE_URL = "http://localhost:8000";

const endpoints = [
  "/products",
  "/users",
  "/orders",
  "/slow-api",
  "/latency-test",
  "/db-test",
  "/error-test",
];

export default function () {

  // Pick random endpoint
  const endpoint = endpoints[Math.floor(Math.random() * endpoints.length)];

  const res = http.get(`${BASE_URL}${endpoint}`);

  check(res, {
    "status is valid": (r) => r.status === 200 || r.status === 500,
  });

  sleep(1);
}