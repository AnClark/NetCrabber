import re, os
# 引入写好的标签检索函数与标签解析工具包
from query_from_all_tags2 import *
from tag_tool import *



test=open(os.path.split(os.path.relpath(__file__))[0]+'/_test_page.txt','r').read()

	
#target_tag=query_tag(test, {'id': 'next-song'})[0]
target_tag=query_tag(test, {'id':'lennon'})[0]
print(target_tag)

# 这个正则就是我们的搜索条件了
regex='(%s)|(<%s.*?>)|(%s)' % (target_tag, extract_tag_name(target_tag), get_opposite_tag(target_tag))
r=re.compile(regex)

print(regex)


result_raw=r.split(test)
result_cat=[]
in_target_area=False
# Filter target area, and remove None items
for item in result_raw:
 if item == target_tag:
  in_target_area=True
 # 实践中发现split()会分割出很多None项
 # 必须去掉，否则后续处理列表时会报错
 if item and in_target_area:
  print("*", item)
  result_cat.append(item)



#print('<%s.*?>' % extract_tag_name(target_tag))
 
# 提取<div>标签内容开始！
# 下面两个正则对应嵌套的<div>标签。注意要匹配所有可能的<div>
r_divL=re.compile('<%s.*?>' % extract_tag_name(target_tag))
r_divR=re.compile(get_opposite_tag(target_tag))
a=0
output=[]

for item in result_cat:
 output.append(item)
 if r_divL.match(item) or r_divR.match(item):
  a+=1
 if r_divR.match(item):
  if a % 2 == 0:
   break
  
print("=========Result=========")
string=""
for item in output:
 string+=item

print(string)



 

