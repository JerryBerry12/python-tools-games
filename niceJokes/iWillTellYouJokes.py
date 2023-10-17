import random
import urllib.request
from urllib.request import Request
target_url = "https://jssources.com/jokefile.txt"

jokelist = []
raw_request = Request('https://dblp.org/db/conf/lak/index')
raw_request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
raw_request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
resp = urllib.request.urlopen(raw_request)
raw_html = resp.read()
for line in resp.readlines():
  jokelist.append(line)
while True:
  print(jokelist[1])
  userchoice = input('Another one? (y/n)')
  userchoice.lower()
  if userchoice == 'n':
    exit()
