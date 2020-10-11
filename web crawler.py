import urllib.request,urllib.parse,urllib.error
import bs4
import ssl
#import re
aa=""
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ur=input('Enter The website - ')
for i in range(10000):
 #print(ur)
 ht=urllib.request.urlopen(ur+"/"+aa,context=ctx).read()
#print(ht)
 so=bs4.BeautifulSoup(ht,'html.parser')

 tag=so('a')
 for t in tag:
    aa=t.get('href',None)
    print(aa)
    #print(t.get('href',None))
    #r=re.findall("[0-9]+",so)
