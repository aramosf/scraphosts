#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import sys
import urllib2
import requests
import socket

if len(sys.argv) == 2:
  domain = sys.argv[1]
else:
  print "Error: " + sys.argv[0] + " <domain>"
  sys.exit(0) 


def get_ips_for_host(host):
        try:
            ips = socket.gethostbyname_ex(host)
        except socket.gaierror:
            ips=[]
        return ips

url = "http://" + domain + ".dnsdb.org/"
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
for link in soup.findAll('a'):
    host = link.contents[0]
    ips = get_ips_for_host(host)
    if len(ips) > 1:
	ip = ips[2]
        print host + "," + ','.join(map(str, ip))
    else:
	print host

