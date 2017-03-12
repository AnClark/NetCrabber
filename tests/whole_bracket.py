import re, os
# 引入写好的标签检索函数与标签解析工具包
from query_from_all_tags2 import *
from tag_tool import *

def extract_html_element_by_attr(html_code, conditions):

 result=[]

 test=html_code
	
 target_tags=query_tag_by_attr(test, conditions)
 
 
 for target_tag in target_tags:
  # 这个正则就是我们的搜索条件了
  regex='(%s)|(<%s.*?>)|(%s)' % (target_tag, extract_tag_name(target_tag), get_opposite_tag(target_tag))
  r=re.compile(regex)

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
    #print("*", item)
    result_cat.append(item)


  #print('<%s.*?>' % extract_tag_name(target_tag))
 
  # 提取标签内容开始！
  # 下面两个正则对应嵌套的标签。注意要匹配所有可能的标签
  r_divL=re.compile('<%s.*?>' % extract_tag_name(target_tag))
  r_divR=re.compile(get_opposite_tag(target_tag))
  stack=[]
  output=[]

  for item in result_cat:
   output.append(item)
   if r_divL.match(item):
    stack.append(item)
   if r_divR.match(item):
    stack.pop()
   if len(stack)<=0:
    break
  
  #print("=========Result=========")
  string=""
  for item in output:
   string+=item

  result.append(string)
  
 return result


if __name__ == "__main__":
 #test=open(os.path.split(os.path.relpath(__file__))[0]+'/_test_page.txt','r').read()
 test=get_html_code("http://cn.jide.com")
 
 result=extract_html_element_by_attr(test, {'class'})
 
 print(result.__len__())
 
 for item in result:
  print("========================")
  print(item)
 

