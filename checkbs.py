from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.html' #'http://py4e-data.dr-chuck.net/comments_1435786.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
lst=[]
count=0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
   num=int(tag.contents[0]).append(lst)
   count=count+1

print('Count',count)
print('Sum',sum(lst))
