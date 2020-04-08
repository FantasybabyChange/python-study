from urllib import request

url = "http://www.baidu.com"
response = request.urlopen(url, timeout=1)
read = response.read().decode("UTF-8")
print(read)
