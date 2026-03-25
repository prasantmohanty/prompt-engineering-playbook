Step 1 — Requirements Clarification + Assumptions

You are a senior Java + Spring Boot engineer.

Task: Build a Customer API.

Before coding, ask exactly 5 clarification questions that affect:
- endpoint shape
- validation rules
- error response format
- persistence choice (in-memory vs DB)
- testing expectations

After the questions, propose sensible defaults (assumptions) if I don’t answer.
Keep output under 200 words.

Step 2 — API Contract (OpenAPI-like)

Using the assumptions from Step 1, define the API contract.

Deliverables:
1) Endpoints (paths, methods)
2) Request/Response JSON schemas
3) Status codes (including validation errors)
4) Example payloads for success and failure
5) Error format must be consistent across endpoints

Output as a concise pseudo-OpenAPI format (not full YAML).

Step 3 — Design: Class & Package Structure

Based on the Step 2 contract, propose the Spring Boot design.

Include:
- package structure
- key classes (Controller, Service, Repository)
- DTOs and mapping approach
- exception handling approach (@ControllerAdvice)
- validation annotations to use

Output as bullet points + a short rationale (max 120 words).

Step 4 — Generate Code (Constrained)

Now generate the code based strictly on the design in Step 3.

Constraints:
- Java 17, Spring Boot 3.x
- Use Jakarta Validation annotations
- Use UUID for customer id
- Use in-memory repository (Map-based) for now
- Provide these files only:
  1) CustomerController
  2) CustomerService
  3) CustomerRepository (in-memory)
  4) DTOs (CustomerRequest, CustomerResponse)
  5) GlobalExceptionHandler (ControllerAdvice)
Do NOT include pom.xml or application.yml.
Keep code minimal but production-clean.

Step 5 — Tests

Write tests for the code from Step 4.

Requirements:
- Use JUnit 5 + Spring Boot Test
- Use MockMvc
- Include at least:
  1) GET returns list
  2) POST with invalid email returns 400 with error format
  3) POST valid returns 201 with expected fields
Provide only the test classes.

Step 6 — Review + Hardening
Review the solution for:
- validation gaps
- error handling consistency
- security concerns (basic)
- naming and REST conventions
- edge cases

Output:
1) Top 8 issues/improvements (priority ordered)
2) Concrete patch suggestions (short snippets where needed)
Do not rewrite everything.



