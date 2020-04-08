import requests

url = "http://httpbin.org/get"
data = {"age": 1, "name": "g"}
get_value = requests.get(url, data)
print(get_value)
print(get_value.text)

url = "http://httpbin.org/post"
data = {"age": 1, "name": "g"}
get_value = requests.post(url, data)
print(get_value)
print(get_value.json())
