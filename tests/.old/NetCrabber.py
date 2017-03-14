import re

def _get_all_tags(html_code):
    regex = r'\<.+?\>'
    r = re.compile(regex)

    result_raw = r.findall(html_code)
    result=[]

    for item in result_raw:
        if not re.match(r'^</', item):
            result.append(item)

    return result


def _extract_tag_attrib(tag_definition):
    regex = r'(\w{1,})\=\"(.*?)\"'
    r = re.compile(regex)

    result_raw = r.findall(tag_definition)
    result = []

    for item in result_raw:
        result.append({
            item[0]: item[1]
        })


    tag_name = re.findall(r'<(.{0,}?)\s', tag_definition)[0]
    result.insert(0, {
        '__tag_name__': tag_name
    })

    return result


