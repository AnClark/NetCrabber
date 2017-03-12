import re

from urllib import request

# 正则作用: 提取所有标签
regex='\<.+?\>'
r=re.compile(regex)

html="http://cn.jide.com/"
html_code=request.urlopen(html).read().decode()

tags=r.findall(html_code)

condition={
	'attrib': "id",
	'value': ""
	}

result=[]

for item in tags:
 # 正则: 找出属性名和/或属性值满足检索条件的标签。额外的\s空白符条件可以把不相干的内容(如HTML属性值的传参)排除在外
 if re.match(r'.*\s%s=%s.*' % (condition['attrib'], condition['value']), item):
  result.append(item)
 
 
for item in result:
 print(item)
 
 