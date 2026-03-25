Task:
Extract API request metadata from natural language instructions. Prioritize diverse scenarios:
- Normal cases, edge cases (missing fields), ambiguities (unclear endpoints), and noisy text.
When something is missing → set value to null.
When ambiguous → set value to null and add a precise warning.
Always return strict JSON using the schema below.

Output schema (JSON only):
{
  "method": "GET|POST|PUT|DELETE|null",
  "url": "string|null",
  "path_params": object,
  "query": object,
  "headers": object,
  "body": object|null,
  "warnings": string[]
}

Examples (diverse):

Example A — Straightforward creation (happy path)
Input:
"Create a payment of 120.5 INR for user u-100."
Output:
{
  "method": "POST",
  "url": "/v1/payments",
  "path_params": {},
  "query": {},
  "headers": { "Content-Type": "application/json" },
  "body": { "amount": 120.5, "currency": "INR", "customerId": "u-100" },
  "warnings": []
}

Example B — Retrieval with path param + query
Input:
"Get report alpha for date=2026-03-17 with details=true."
Output:
{
  "method": "GET",
  "url": "/v2/reports/alpha",
  "path_params": { "name": "alpha" },
  "query": { "date": "2026-03-17", "details": "true" },
  "headers": {},
  "body": null,
  "warnings": []
}

Example C — Ambiguous method and endpoint (ambiguity)
Input:
"Fetch the summary; I think it’s under the reports API somewhere."
Output:
{
  "method": "GET",
  "url": null,
  "path_params": {},
  "query": {},
  "headers": {},
  "body": null,
  "warnings": ["endpoint path ambiguous or unspecified"]
}

Example D — Update with partial body and custom header (edge case)
Input:
"Update user u-42 to active=true. Use header X-Trace-Id=t-77."
Output:
{
  "method": "PUT",
  "url": "/v2/users/u-42",
  "path_params": { "userId": "u-42" },
  "query": {},
  "headers": { "X-Trace-Id": "t-77", "Content-Type": "application/json" },
  "body": { "active": true },
  "warnings": []
}

Example E — Noisy text with extra chatter (robustness)
Input:
"(ASAP) pls make a payment—amount 50 USD for user u-9!! thx"
Output:
{
  "method": "POST",
  "url": "/v1/payments",
  "path_params": {},
  "query": {},
  "headers": { "Content-Type": "application/json" },
  "body": { "amount": 50, "currency": "USD", "customerId": "u-9" },
  "warnings": []
}

Example F — Conflicting info (ambiguity + warning)
Input:
"Delete user u-88 or maybe disable? Not sure which endpoint we use."
Output:
{
  "method": "DELETE",
  "url": "/v2/users/u-88",
  "path_params": { "userId": "u-88" },
  "query": {},
  "headers": {},
  "body": null,
  "warnings": ["instruction conflicted between delete vs disable; assumed DELETE /v2/users/{id}"]
}

Example G — Missing required field (edge case)
Input:
"Create a payment in EUR without specifying amount."
Output:
{
  "method": "POST",
  "url": "/v1/payments",
  "path_params": {},
  "query": {},
  "headers": { "Content-Type": "application/json" },
  "body": { "amount": null, "currency": "EUR", "customerId": null },
  "warnings": ["amount missing", "customerId missing"]
}

Now extract (JSON only):
Input:
"List users created since 2026-03-01, page size 50. Add header Accept: application/json."
Output:
``