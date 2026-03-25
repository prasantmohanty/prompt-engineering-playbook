Task: Write OpenAPI-compatible endpoint docs with concise summaries, clear descriptions, and strong examples.

Examples:
Endpoint:
POST /v1/payments
Summary: Create a payment.
Description: Creates a payment with the specified amount and currency.
Request Example:
{ "amount": 120.5, "currency": "INR", "customerId": "u-100" }
Response Example 201:
{ "paymentId": "p-001", "status": "SUCCESS", "amount": 120.5, "currency": "INR" }
Error Example 400:
{ "code": "INVALID_AMOUNT", "message": "Amount must be positive" }

Endpoint:
GET /v1/users/{id}
Summary: Get user by ID.
Description: Retrieves a user resource by identifier.
Path Params:
- id: string (required)
Response Example 200:
{ "userId": "u-42", "name": "Alice", "active": true }

Now document:
Endpoint: POST /v2/reports
Summary: Submit a report generation request
Description: Accepts a report name and date range; returns an asynchronous job id.
Request body fields: reportName (string), fromDate (RFC3339), toDate (RFC3339)
Success 202: jobId (string), status ("QUEUED")
Errors: 400 invalid_date_range, 429 rate_limited
Provide request/response examples for 202 and 400, plus a 429 error example.