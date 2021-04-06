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

setup_script = f"""
# -*- coding: UTF-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgui",
    version="{version}",
    author="Ciro Garcia",
    author_email="kolterdev@gmail.com",
    description="A GUI module compatible with pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kolterdyx/PyGameUI",
    packages=setuptools.find_namespace_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
"""
with open("setup.py", "w") as f:
    f.write(setup_script)

with open("version.txt", "w") as f:
    f.write(version)

commands = [
"python setup.py sdist",
"twine upload dist/* -u Kolterdyx -p tengo1hermano123"
]
for i in commands:
    os.system(i)

remove = [
    "build",
    "dist",
    "pgui.egg-info"
]
for i in remove:
    try:
        shutil.rmtree(i)
    except:
        continue

print(f"Finished uploading version: {version}")
