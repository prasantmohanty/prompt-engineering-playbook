Task: Transform v1 request into v2.

v1 -> v2 mapping:
- v1.userId -> v2.subject_id
- v1.phone -> v2.contact.msisdn
- v1.amount -> v2.payment.amount.value
- v1.currency -> v2.payment.amount.currency
- v1.metadata.* -> v2.context.*

Examples:
Input (v1):
{"userId":"u-42","phone":"+919999999999","amount":99.5,"currency":"INR","metadata":{"campaign":"HOLI"}}
Output (v2):
{"subject_id":"u-42","contact":{"msisdn":"+919999999999"},"payment":{"amount":{"value":99.5,"currency":"INR"}},"context":{"campaign":"HOLI"}}

Input (v1):
{"userId":"p-77","phone":"00112233","amount":10,"currency":"USD"}
Output (v2):
{"subject_id":"p-77","contact":{"msisdn":"00112233"},"payment":{"amount":{"value":10,"currency":"USD"}},"context":{}}

Now transform:
Input (v1):
{"userId":"z-100","phone":"+447700900123","amount":15,"currency":"EUR","metadata":{"source":"web"}}
Output (v2, JSON only):
