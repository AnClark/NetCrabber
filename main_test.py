from netcrabber import crabhtml, tag_tools


hcode=tag_tools.get_html_code("https://www.zhihu.com")
print(crabhtml.query_tag_by_tagname(hcode, "script"))



