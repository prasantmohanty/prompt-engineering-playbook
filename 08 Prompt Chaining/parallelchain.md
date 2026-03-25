Prompt A — Exact solution

Provide an exact Java solution to compute top-K frequent IDs from a stream.
Constraints: IDs are strings, K <= 1000.
Return: algorithm + time/memory complexity + code sketch.

Prompt B — Approximate solution (memory constrained)

Provide an approximate approach for top-K frequent IDs under memory constraints.
Discuss Count-Min Sketch / Misra-Gries (heavy hitters).
Return: which method to use, error bounds intuition, and Java-friendly design.
Avoid external libraries.

Prompt C — Engineering reality checks

Think like a production engineer:
- how to handle ingestion batching
- concurrency considerations
- test strategy and data validation
Return: pitfalls + recommended safeguards

Merge prompt

Merge into a final recommendation:
- When to use exact vs approximate
- Provide one exact implementation (Java) and one approximate outline
- Add unit test


If Copilot forgets earlier outputs (happens many times )
First summarize key conclusions from A/B/C in 6 bullets, then produce the merged final answer.