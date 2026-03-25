Specific
You are a Spring Boot performance engineer.Context: ProductService.getProductById(String id) calls a downstream HTTP service with ~500ms latency.Task: Add caching to reduce repeated latency for identical IDs.Constraints & Details:
Use Spring Cache with Caffeine (spring-boot-starter-cache, com.github.ben-manes.caffeine)
Cache name: products
Key: id (string)
TTL: 10 minutes; Max size: 5,000 entries; Eviction policy: size + time based
Invalidate on update: When updateProduct(Product p) is called, evict the cache entry for p.id
Observability: Expose cache metrics via Micrometer (cache hits/misses/evictions)
Fallback: On downstream 5xx, return last cached value (if exists) and include header X-Cache-Fallback: true; otherwise propagate error
