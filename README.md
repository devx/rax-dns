# Script to interact with rackspace DNS service

This is a simple script that interacts with rackspace dns service. It currently
supports the following:

  [x] List Domains
  [x] List records of a domain
  [x] Add a record to a domain
  [ ] Delete a record from a domain
  [ ] Delete a domain

# Requirements
Install the required libraries from the requirements.txt file.

```
   pip install -r requirements.txt
```

# Example:
```
./dns.py -h
Usage:
    dns.py list domains
    dns.py list records <domain>
    dns.py add record <domain> <type> <hostname> <ip> <ttl>

Options:
    -h --help              Help
    --version              Show version

Example:
        dns.py add record mahi.ws A rax-dev 10.23.21.12 301
```