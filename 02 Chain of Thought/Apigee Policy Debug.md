B — Begin:
We’re seeing 401/403 errors on Apigee for /v1/* after a recent proxy update. Need a root‑cause hypothesis and a minimal set of checks/fixes.

R — Reason:
Systematically inspect OAuth/JWT verification, API Key verify policy, target server auth, and flow variables. Use a short, repeatable diagnostic list.

E — Execute:
1) Inspect VerifyAPIKey/VerifyJWT policy results and variables.
2) Check ConditionalFlows for incorrect conditions (e.g., wrong path/verb scopes).
3) Validate Key/Secret/JWKS/Issuer/Aud matches and time skew.
4) Confirm target auth headers and TLS settings.
5) Provide fix steps and a small test matrix.

A — Answer:
Output JSON:
{
  "steps": string[],
  "likely_causes": string[],
  "fixes": string[],
  "test_matrix": 
    {"path": string, "method": string, "expected_status": number, "notes": string}
  ]
}

K — Know:
Include a "verification" object indicating:
- Which policies/vars were confirmed (true/false).
- A quick curl example to validate a passing and failing case.