import re
from urllib import request

regex=r'\<.+?\>'

r=re.compile(regex)

html="http://cn.jide.com/"
html_code=request.urlopen(html).read().decode()

result=r.findall(html_code)


for item in result:
 if not re.match(r'^</', item):
  print(item)
  
  """
for item in result:
 print(item)"""

