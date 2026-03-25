
Task: Write Javadoc in the exact style shown.

Examples:
Code:
public final class RateLimiter {
  /**
   * Try to acquire a single token if available.
   */
  public boolean tryAcquire() { ... }
}
Doc:
Class: RateLimiter
Summary: A thread-safe token-bucket rate limiter for controlling request throughput.
Usage: Create with capacity and refill rate, then call tryAcquire() before gated operations.
Thread-safety: All public methods are safe for concurrent use.

Method: tryAcquire
Summary: Attempts to consume one token from the bucket.
Params: none
Returns: true if a token was acquired; false otherwise
Throws: none
Example:
RateLimiter rl = new RateLimiter(100, 50.0);
if (rl.tryAcquire()) { /* proceed */ }

Code:
public boolean tryAcquire(int permits) throws IllegalArgumentException { ... }
Doc:
Method: tryAcquire
Summary: Attempts to acquire the specified number of tokens.
Params:
- permits: number of tokens to consume; must be >0 and ≤ capacity
Returns: true if enough tokens were available; otherwise false
Throws:
- IllegalArgumentException if permits ≤ 0 or exceeds capacity
Example:
boolean ok = rl.tryAcquire(5);

Now document (produce Javadoc blocks) for this code:
public record PaymentRequest(java.util.UUID customerId, java.math.BigDecimal amount, String currency) {
  public PaymentRequest {
    if (amount == null || amount.signum() <= 0) throw new IllegalArgumentException("amount>0 required");
    if (currency == null || currency.isBlank()) throw new IllegalArgumentException("currency required");
  }
}
