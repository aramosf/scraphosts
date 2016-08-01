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

url = "https://www.virustotal.com/en-gb/domain/" + domain + "/information/"
req = urllib2.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('Accept-Language', 'en-US,en;q=0.5')
resp = urllib2.urlopen(req)
html = resp.read()

soup = BeautifulSoup(html)
div=soup.find("div", {"id": "observed-subdomains"})
soupdata = BeautifulSoup(str(div))
for link in soupdata.findAll('a'):
    host = link.contents[0].strip()
    ips = get_ips_for_host(host)
    if host == 'More': continue
    if len(ips) > 1:
      ip = ips[2]
      print host + "," + ','.join(map(str, ip))
    else:
        print host

