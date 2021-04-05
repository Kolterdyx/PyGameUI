import os
import shutil

with open("version.txt", "r") as f:
    version = f.read().strip().split('.')

patch = int(version[-1])
version[-1] = str(patch+1)

for i,d in enumerate(version):
    version[i] = d+"."
version = "".join(version)
version = version[:-1]
print(version)
with open("version.txt", "w") as f:
    f.write(version)

commands = [
"python setup.py sdist",
"twine upload dist/* -u Kolterdyx -p tengo1hermano123"
]
for i in commands:
    os.system(i)

remove = [
    "dist",
    "pgui.egg-info"
]
for i in remove:
    try:
        shutil.rmtree(i)
    except:
        continue
