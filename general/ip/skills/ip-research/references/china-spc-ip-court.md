# China SPC IP Court hearing notices

The official Supreme People's Court Intellectual Property Court website publishes scheduled hearing notices and a broader site search. No credentials are required.

```python
from patent_client_agents.china_spc_ip_court import ChinaSpcIpCourtClient

async with ChinaSpcIpCourtClient() as client:
    index = await client.list_hearing_index(page=1)
    notice = await client.get_hearing_notice(index.notices[0].notice_id)
    semiconductor_results = await client.search_site("集成电路")
```

The MCP tools can inspect multiple recent index pages and filter normalized notice text using Chinese party or technology terms. Useful semiconductor terms include `芯片`, `半导体`, and `集成电路`.

This source is a public hearing calendar, not a complete docket. Notices may omit case number, patent number, filings, and later disposition. Do not convert the scheduled hearing date into an authoritative open/closed case status. The Chinese WAF may also block some foreign DNS or cloud-egress paths.
