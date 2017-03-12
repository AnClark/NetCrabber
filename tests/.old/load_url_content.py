from urllib import request
from chardet import detect

get_charset = lambda x : detect(x)['encoding']

def load_urlpage_code(url):
    req = request.urlopen(url)

    data = req.read()

    z = get_charset(data)

    return data.decode(get_charset(data))

if __name__ == "__main__":
    print(load_urlpage_code('http://www.baidu.com'))