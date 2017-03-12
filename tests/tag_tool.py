import re
from urllib import request


def extract_tag_name(tag):
 regex='<(.+?)[\s|>|/]'
 r=re.compile(regex)
 
 return r.findall(tag)[0]


def extract_tag_props(html_tag_def):
 test=html_tag_def

 regex=r'(\w{1,})\=\"(.*?)\"'
 r=re.compile(regex)

 result_raw=r.findall(test)
 result={}

 for item in result_raw:
  result[item[0]]=item[1]
  	
 tag_name=re.findall(r'\<(.{0,}?)\s', test)[0]
 result['__tag_name__']=tag_name

 return result


def get_pure_tag(tag):
 tagname=extract_tag_name(tag)
 return "<%s>" % tagname


def get_opposite_tag(tag):
 tagname=extract_tag_name(tag)
 return "</%s>" % tagname


def get_all_tags(html_code):
 regex='<.+?>'
 L=re.findall(regex,html_code)
 return [item for item in L if not re.match(r'^</', item)]


def get_html_code(url):
 httpobj=request.urlopen(url)
 raw_data=httpobj.read()
 return raw_data.decode()
 

if __name__ == "__main__":
 print(extract_tag_name('<div id="main">'))
 print(extract_tag_name('<script type="text/javascript">'))
 print(extract_tag_name('<link rel="stylesheet" href="main.css" />'))
 print(extract_tag_name('<br/>'))
 print(get_opposite_tag('<div id="main">'))

 print("==================")
 print(get_all_tags(get_html_code("http://cn.jide.com/")))

 print("==================")
 test='<div id="login_box" class="login-box col-md-10" onclick="backgroundtask()" alt="">'
 print(extract_tag_props(test))