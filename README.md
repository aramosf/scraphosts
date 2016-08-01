# Scrap hostnames from multiple sources like DNSDB, VirusTotal or NetCraft


### Usage

Example using DNSDB:

```sh
ninjabox: aramosf$ python dnsdbext.py nba.com
40.nba.com
a5.nba.com
account.nba.com,50.18.159.38,184.169.178.146
ads.nba.com
arabic.nba.com,157.166.249.247,157.166.248.245
asiafans.nba.com,199.7.201.15
audience.nba.com,157.166.255.87,157.166.255.74
blogs.nba.com,157.166.249.247,157.166.248.245
broadband.nba.com,185.43.182.49,185.43.182.75
broker.nba.com
china.nba.com,84.53.132.48,84.53.132.33
chinanba.nba.com,84.53.132.153,84.53.132.179
...
```

Example using VirusTotal:

```sh
ninjabox: aramosf$ python vtext.py nba.com
origin.nba.com,157.166.248.245,157.166.239.111,157.166.238.209,157.166.249.247
losangeles.dleague.nba.com,84.53.132.90,84.53.132.97
uk.global.nba.com,84.53.132.192,84.53.132.171
jazz.nba.com,157.166.249.247,157.166.248.245
on.nba.com,67.199.248.12,67.199.248.13
stats.nba.com,84.53.132.153,84.53.132.136
www.qa.nba.com,104.126.92.140
pluckcb.nba.com,69.64.158.205
responses.nba.com,12.130.158.104
wnbastore.nba.com,50.31.158.88
...
```


