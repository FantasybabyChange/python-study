# 正则表达式
import re


class Matcher:
    def __init__(self, pattern, matcher, sub_str=None):
        self.pattern = pattern
        self.matcher = matcher
        self.sub_str = sub_str

    def match(self):
        re_compile = re.compile(self.pattern)
        result = re_compile.match(self.matcher)
        return result

    def search(self):
        re_compile = re.compile(self.pattern)
        result = re_compile.search(self.matcher)
        return result

    def sub(self):
        re_compile = re.compile(self.pattern)
        result = re.sub(self.pattern, self.sub_str, self.matcher)
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

# search  可以不需要完全匹配

p3 = r'(\d+)-(\d+)-(\d+)'
match_str = "aa2020-03-10asa"
print(Matcher(p3, match_str).search().groups())
# year, month, day = Matcher(p3, match_str).search()
print(year)

# sub
p4 = r'#.*$' # ti huan
p5 = r'\D'
sub_str = "1-3-2-1 # 后面的都没用"
print(Matcher(p5, sub_str, "").sub())
# find_all
