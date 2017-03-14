import re

from tests.tag_tool import *

def _empty_to_match_all(x):
 if x=="": 
  return '.*' 
 else:
  return x

def query_tag_by_attr(html_code, _attr_conditions):
 _conditions=_attr_conditions
 conditions={}
 
 if isinstance(_conditions, dict):
  conditions=_conditions
 else:
  try:
   conditions=dict.fromkeys(_conditions, '')
  except:
   raise TypeError("Argument 'conditions' should be a dict, set or list, whose keys are attributes\' names")

 print(conditions)

 tags=re.findall(r'<.+?>',html_code)
 result=[]
 n=conditions.__len__()
 
 #print(tags)
 
 for item in tags:
  weight=0
  for attr in conditions.keys():
   regex='.*\s%s\=["|\s]%s["|\s].*' % (attr, _empty_to_match_all(conditions[attr]))
   
   r=re.compile(regex)
   if r.match(item):
    weight+=1
  if weight == n:
   result.append(item)
   
 return result


def query_tag_kwarg(html_code, **conditions):
 tags=re.findall(r'<.+?>',html_code)
 result=[]
 n=conditions.__len__()
 
 #print(tags)
 
 for item in tags:
  weight=0
  for attr in conditions.keys():
   regex='.*\s%s\=["|\s]%s["|\s].*' % (attr, _empty_to_match_all(conditions[attr]))
   r=re.compile(regex)
   if r.match(item):
    weight+=1
  if weight == n:
   result.append(item)
   
 return result


if __name__ == '__main__':
 html="http://cn.jide.com/"
 html_code=get_html_code(html)

 
 result=query_tag_by_attr(html_code, {'id', 'class'})
 #result=query_tag_kwarg(html_code, style='')
  
 for item in result:
  print(item)
 
 