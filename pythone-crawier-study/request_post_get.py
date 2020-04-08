from urllib import request, parse

data = bytes(parse.urlencode({"word": "hello"}), encoding='utf8')
r1 = request.urlopen("http://httpbin.org/get")
print(r1.read().decode("UTF-8"))
r2 = request.urlopen("http://httpbin.org/post", data=data)
print(r2.read().decode("UTF-8"))
