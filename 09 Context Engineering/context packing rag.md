You are a Java reviewer. Use ONLY the context. Do not rely on prior knowledge.

Context (retrieved):
[Doc A] "Prefer try-with-resources for any Closeable. Never swallow exceptions; wrap with domain error code."
[Doc B] "CSV parsing: treat empty lines as skip; invalid row -> collect error with lineNo + reason; never stop parsing."
[Code Snippet] parseIntSafe(s): returns OptionalInt.empty() if invalid.

Task:
Write a Java 17 method parseAges(List<String> csvLines) that extracts the age field (4th column),
returns (validAges, errors). Follow the guidelines.

Output:
1) Code only
2) 3 short test cases
3) Evidence: cite Doc A/Doc B lines used
