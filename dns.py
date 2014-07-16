#!/usr/bin/env python
"""
Usage:
    dns.py list domains
    dns.py list records <domain>
    dns.py add record <domain> <type> <hostname> <ip> <ttl>

Options:
    -h --help              Help
    --version              Show version

Example:
        dns.py add record mahi.ws A rax-dev 10.23.21.12 301
"""
from docopt import docopt
import pyrax
import os
import sys


def init_pyrax():
    pyrax.set_setting("identity_type", "rackspace")
    pyrax.set_credentials(os.environ['OS_USERNAME'], os.environ['OS_APIKEY'])


def list_domains(arguments):
    init_pyrax()
    dns = pyrax.cloud_dns
    try:
        domains = dns.list()
        print "Domain \t\t Admin Email"
        for item in domains:
            print "%s \t %s" % (item.name, item.emailAddress)
    except Exception:
        print "Could not get any information from rackspace DNS service"
        sys.exit(0)


def add_record(arguments):
    init_pyrax()
    dns = pyrax.cloud_dns
    dom = dns.find(name=arguments['<domain>'])
    try:
        new_rec = [{
            "type": str(arguments['<type>']),
            "name": str(arguments['<hostname>'] + "." + arguments['<domain>']),
            "data": str(arguments['<ip>']),
            "ttl": int(arguments['<ttl>']),
        }]
        print dns.add_record(dom, new_rec)
    except Exception:
        print "Could not create record, please try again"
        sys.exit(0)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    if arguments['list'] and arguments['domains']:
        list_domains(arguments)
    elif arguments['add']:
        add_record(arguments)

#    else:
#        update(arguments).
