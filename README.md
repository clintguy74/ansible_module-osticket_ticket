ansible\_module-osticket\_ticket
================================

Requirements
--------------------------------
`requests`

Installation
--------------------------------
1. Clone repo
2. Copy `osticket_ticket.py` into your module folder defined in `ansible.cfg`

Examples
--------------------------------

```yaml
- name: create help desk ticket
  osticket_ticket:
   alert: True
   autorespond: False
   name: Display Name
   email: service_account@domain.tld
   subject: Error during check
   message: "Check on error"
   ip: "127.0.0.1"
   priority: Normal
   api_key: secret_key_defined_in_osticket
   url: "https://osticket.domain.tld/api/tickets.json" 
```
