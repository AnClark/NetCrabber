from netcrabber.__init__ import *
from netcrabber.tag_tools import *


def extract_html_element_by_attr(html_code, conditions):
    result = []

    test = html_code

    target_tags = query_tag_by_attr(test, conditions)

    for target_tag in target_tags:
        # 这个正则就是我们的搜索条件了
        regex = '(%s)|(<%s.*?>)|(%s)' % (target_tag, extract_tag_name(target_tag), get_opposite_tag(target_tag))
        r = re.compile(regex)

        result_raw = r.split(test)
        result_cat = []
        in_target_area = False

        # Filter target area, and remove None items
        for item in result_raw:
            if item == target_tag:
                in_target_area = True
            # 实践中发现split()会分割出很多None项
            # 必须去掉，否则后续处理列表时会报错
            if item and in_target_area:
                # print("*", item)
                result_cat.append(item)

        # print('<%s.*?>' % extract_tag_name(target_tag))

        # 提取标签内容开始！
        # 下面两个正则对应嵌套的标签。注意要匹配所有可能的标签
        r_divL = re.compile('<%s.*?>' % extract_tag_name(target_tag))
        r_divR = re.compile(get_opposite_tag(target_tag))
        stack = []
        output = []

        for item in result_cat:
            output.append(item)
            if r_divL.match(item):
                stack.append(item)
            if r_divR.match(item):
                stack.pop()
            if len(stack) <= 0:
                break

        # print("=========Result=========")
        string = ""
        for item in output:
            string += item

        result.append(string)

    return result


def _empty_to_match_all(x):
    if x == "":
        return '.*'
    else:
        return x


def query_tag_by_attr(html_code, _attr_conditions):
    _conditions = _attr_conditions
    conditions = {}

    if isinstance(_conditions, dict):
        conditions = _conditions
    else:
        try:
            conditions = dict.fromkeys(_conditionqs, '')
        except:
            raise TypeError("Argument 'conditions' should be a dict, set or list, whose keys are attributes\' names")

    #print(conditions)

    tags = re.findall(r'<.+?>', html_code)
    result = []
    n = conditions.__len__()

    # print(tags)

    for item in tags:
        weight = 0
        for attr in conditions.keys():
            regex = '.*\s%s\=["|\s]%s["|\s].*' % (attr, _empty_to_match_all(conditions[attr]))

            r = re.compile(regex)
            if r.match(item):
                weight += 1
        if weight == n:
            result.append(item)

    return result


def query_tag_by_tagname(html_code, tagname):
    result=[]
    tags=re.findall(r'<.+?>', html_code)
    
    for item in tags:
        if re.match(r'^<%s' % tagname, item):
            result.append(item)
            
    return result
