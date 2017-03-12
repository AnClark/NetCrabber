import re

regex='(<div.*?>)|(</div>)'
#regex='(</div>)([\s\S]*?)(<div[\s|\S]*?>)'
#regex='(<div.*?>)([\s\S]*?)(</div>)|(<div.*?>)([\s\S]*?)(<div.*?>)|(</div>)'
#regex='<(?P<HtmlTag>div)[^>]*?>((?P<Nested><\k<HtmlTag>[^>]*>)|</\k<HtmlTag>>(?<-Nested>)|.*?)*</\k<HtmlTag>>'
r=re.compile(regex)

test="""
<div id="main">
 <h1>朴树——生如夏花</h1>
 
 <div id="parse-issue" class="col-md-6">
  <p>嵌套解析出问题了吗？</p>
 </div>
 
 <div>
  <p>这是一个美妙的世界</p>
  <ul>
   <li>出品于21世纪初
  </ul>
 </div>
 
 <div id="next-song" class="col-md-6">
  <p>你为什么哎，言无声泪如雨</p>
  <p>这是《在木星》，朴树的又一个作品</p>
  <p><strong>尽现心路历程</strong></p>
 </div>
 
 <h3>现在就书写属于你的生如夏花！</h3>
 <p>我在这里呀，就在这里呀！</p>
 <div>aaa</div>
 
</div>

<div>
 <h3>IMAGINE ALL THE PEOPLE</h3>
</div>
"""

result_raw=r.split(test)
print(result_raw)


"""
result_raw=r.findall(test)
result_cat=()

for item in result_raw:
 #print("=====================")
 #print(item)
 result_cat+=item
 
print(result_cat)
 
# 提取<div>标签内容开始！
r_divL=re.compile(r'<div.*?>')
r_divR=re.compile(r'</div>')
a=1
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

"""

 

