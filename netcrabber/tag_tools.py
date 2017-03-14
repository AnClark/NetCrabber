"""
    NetCrabber Project - Tag Tools
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    A toolkit for processing HTML tags in an HTML code.

    :Copyright (c) 2017 By AnClark Liu
    :license MIT Open-source license
"""

from netcrabber.__init__ import *


def extract_tag_name(tag):
 """
 Extract tag name from a tag definition.
 For example, if you specify "<div id="test" class="main-title">", you will get "div".
 :NOTICE Other functions depend on this!
 :param tag: An HTML tag definition.
 :return: The tag name.
 """
 regex='<(.+?)[\s|>|/]'
 r=re.compile(regex)
 
 return r.findall(tag)[0]


def extract_tag_attrs(html_tag_def):
 """
 Extract HTML tag attributes from an HTML tag definition.
 :param html_tag_def: An HTML tag definition.
 :return: A DICT of attributes, whose keys are attr names, and values are attr values.
 """
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
 """
 Convert an HTML tag definition to its basic format. In other word, it will prune all those attrs, only left tag name.
 For example, if you specify "<div class="main-title">", you will get "<div>".
 :NOTICE Other functions depend on this!
 :param tag: An HTML tag definition.
 :return: The corresponding pure tag definition.
 """
 tagname=extract_tag_name(tag)
 return "<%s>" % tagname


def get_opposite_tag(tag):
 """
 Get the close tag of an HTML tag. Necessary for extracting element.
 :NOTICE Other functions depend on this!
 :param tag: An HTML tag, for example, "<body>".
 :return: Its corresponding close tag. For example, "</body>".
 """
 tagname=extract_tag_name(tag)
 return "</%s>" % tagname


def get_all_tags(html_code):
 """
 Get all HTML tag definitions from an HTML source code.
 :param html_code: An HTML source code.
 :return: A LIST including all those tags.
 """
 regex='<.+?>'
 L=re.findall(regex,html_code)
 return [item for item in L if not re.match(r'^</', item)]


def get_html_code(url):
 """
 BETA - Get an HTML source code by URL.
 :param url: The URL you want to access.
 :return: HTML code.
 """
 httpobj=request.urlopen(url)
 raw_data=httpobj.read()
 return raw_data.decode()
 
