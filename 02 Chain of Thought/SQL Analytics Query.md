B — Begin:
Write a SQL query to compute daily unique active users and 7‑day rolling average from events(user_id, occurred_at). We need performance‑aware windowing.

R — Reason:
Use DATE(occurred_at) grouping + window function AVG over 6 preceding rows; ensure correct ordering and partitioning.

E — Execute:
1) CTE daily DAU by date.
2) Apply window AVG(dau) over rows between 6 preceding and current.
3) Ensure index usage on occurred_at if relevant.
4) Provide constraints (NULL handling/timezones).

A — Answer:
Return JSON:
{"steps": string[], "sql": "<query>"}

K — Know:
Include a short "explain" checklist and test data snippet to verify the window math on 8–10 days.
