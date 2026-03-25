B — Begin:
Implement a thread‑safe token‑bucket RateLimiter in Java with JUnit 5 tests. capacity=100, refillRate=50 tokens/sec, nanos for timing.

R — Reason:
Token bucket supports burst tolerance with average control; synchronized sections keep it thread‑safe; tests validate refill accuracy and burst respect.

E — Execute:
1) Track tokens, capacity, refillPerNanos, last Refill.
2) Refill on access using elapsed nanos; clamp to capacity.
3) Implement tryAcquire(permits) with validation; avoid busy‑wait.
4) Provide getAvailableTokens() with internal refill.
5) Write tests: burst (≤capacity), ~1s refill ~50±2%, negative/over‑capacity rejects.

A — Answer:
Return JSON only with:
{"steps": string[], "final_code": "<Java source>", "tests": "<JUnit 5 source>"}

K — Know:
Add a "self_check" JSON with:
- compile_notes (e.g., imports, JDK level),
- determinism hints (sleep margins),
- edge cases covered (0/negative permits, permits > capacity).
