We need to choose an API Gateway strategy for a large enterprise platform.  
The choices are:  
• Apigee Hybrid  
• Kong OSS + Enterprise Plugins  
• AWS API Gateway  

Constraints:  
- Multi-region deployment  
- Must support AI Gateway features and LLM policy enforcement  
- Strong governance required  
- Cost matters; avoid >25% yearly Opex growth  
- Need observability + distributed tracing  
- Low latency for public APIs (<150ms p95)

Evaluate systematically and produce a defensible architectural decision.
