# -*- coding: utf-8 -*-
import re

def check_brk_pair(str):
    bracket_l = ('(', '[', '{')
    bracket_r = (')', ']', '}')

    stack = []

    for i in range(0, len(str) - 1):
        if str[i] in bracket_l:
            stack.append('str[i]')
        elif str[i] in bracket_r:
            stack.pop()

    return len(stack) == 0

def is_tag(tagname, tag_to_check):
    tmp = tagname.replace('>','')
    rgx = re.compile(tagname + '.+?')
    return rgx.match(tag_to_check)


def check_html_tag_pair(str):
    tags = ("<html>", "<head>", "<body>", "<div>", "<p>")
    tags_r = ("</html>", "</head>", "</body>", "</div>", "</p>")
    get_tag_opposite = lambda x : x.replace("<","</")
    is_opposite_tag = lambda x : x[0:1] == "</"
    tag_recover = lambda x : x.replace("</", "<")       # 将反HTML标签（如</html>）还原成正HTML标签（对应<html>）


    stack = []

    for i in range(0, len(str) - 1):
        if str[i] == '<':
            # 查找另一个括号的位置
            j = i
            while str[j] != '>':
                j+=1
            # 获得当前位置的HTML标签
            cur_html_tag = str[i:j+1]

            if is_tag(cur_html_tag)
                stack.append(cur_html_tag)
            elif cur_html_tag in tags_r:
                if len(stack) : stack.pop()

    return len(stack) == 0






if __name__ == "__main__":

    cat = lambda filename : open(filename, 'rb').read().decode('GB18030','ignore')

    test_str1 = """
    function test(int i){
        array=[1,2,3,4,5]
        print("abcde")
        }
    """

    test_str2 = """
    function test(int i{
        array=[1,2,3,4,5]
        print("abcde")
        }
    """

    test_html1 = cat('html_test1.html')
    test_html2 = cat('html_test2.html')

    print("Bracket pair for str1: ", check_brk_pair(test_str1))
    print("Bracket pair for str2: ", check_brk_pair(test_str2))

    print(check_html_tag_pair(test_html1))
    print(check_html_tag_pair(test_html2))

