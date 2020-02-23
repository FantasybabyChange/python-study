import re


# #文件读取
def search_hero_count(file_name, hn=None):
    """
     读取文件查找文件中出现的次数
    :param file_name:
    :param hn:
    :return:
    """
    if hn is None:
        return
    with open(file_name, encoding='GB18030') as f:
        content = f.read().replace("\n", "")
        return len(re.findall(heroName, content))


nameWithCount = {}
with open('../san_name.txt', encoding='GB18030') as file:
    for heroName in file.read().split("|"):
        nameWithCount[heroName] = search_hero_count('../sanguo.txt', heroName)
sorted_name = sorted(nameWithCount.items(), key=lambda item: item[1], reverse= True)
print(nameWithCount)
print(sorted_name)

