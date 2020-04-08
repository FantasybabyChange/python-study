import requests
import re

url = "http://www.cnu.cc/works/396609"
text = requests.get(url).text
# print(text)
pattern = re.compile(r'<img src="(.*?)"', re.S)
results = re.findall(pattern, text)
# print(results)
for a in results:
    print(a)
