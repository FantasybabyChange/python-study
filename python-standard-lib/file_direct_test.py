# 文件或者文件夹
import os
from pathlib import Path
import shutil

print(os.path.abspath("."))
print(os.path.abspath(".."))
print(os.path.exists("C:\workspace\pyWorkspace\python-study\python-standard-libc"))
print(os.path.isdir("C:\workspace\pyWorkspace\python-study\python-standard-lib"))
print(os.path.isfile("C:\workspace\pyWorkspace\python-study\python-standard-lib"))
# 连接路径
print(os.path.join("C:\workspace\pyWorkspace", "\python-study"))

# pathlib
path = Path(".")
print(path.resolve())
all_dir = [x for x in path.iterdir() if x.is_file()]
print(all_dir)

# Path.mkdir(path.joinpath("a/b"), parents=True)
# Path.rmdir(path.joinpath("a"))
# os.removedirs(path.joinpath("a"))
#下面这个能删掉
shutil.rmtree(path.joinpath("a"))