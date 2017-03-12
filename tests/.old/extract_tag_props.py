import re
regex=r'(\w{1,})\=\"(.*?)\"'

r=re.compile(regex)

test='<div id="login_box" class="login-box col-md-10" onclick="backgroundtask()" alt="">'

result_raw=r.findall(test)
result=[]


for item in result_raw:
 result.append({
 	item[0]: item[1]
 	})
 	
tag_name=re.findall(r'<(.{0,}?)\s', test)[0]
#print("Tag name is: ", tag_name)

result.insert(0,{
	'__tag_name__': tag_name
	})

print(result)

