# 正则表达式
import re


class Matcher:
    def __init__(self, pattern, matcher):
        self.pattern = pattern
        self.matcher = matcher

    def match(self):
        re_compile = re.compile(self.pattern)
        result = re_compile.match(self.matcher)
        return result


p1 = 'd*g'
match_str = 'gggggggg'
print(Matcher(p1, match_str).match())

p2 = 'do{3}g'
match_str = 'dooog'
print(Matcher(p2, match_str).match())
p3 = '....-..-..'
match_str = "2020-03-10"
print(Matcher(p3, match_str).match())

p3 = r'(\d+)-(\d+)-(\d+)'
match_str = "2020-03-10"
print(Matcher(p3, match_str).match().group())
year, month, day = Matcher(p3, match_str).match().groups()
print(year)

# search

p3 = r'(\d+)-(\d+)-(\d+)'
match_str = "2020-03aa-10asa"
print(Matcher(p3, match_str).match().group())
year, month, day = Matcher(p3, match_str).match().groups()
print(year)
