# @Author: Ciro García <kolterdyx>
# @Date:   14-Aug-2020
# @Email:  kolterdev@gmail.com
# @Project: Pygame GUI
# @Last modified by:   kolterdyx
# @Last modified time: 16-Aug-2020
# @License: This file is subject to the terms and conditions defined in file 'LICENSE', which is part of this source code package.


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt", r) as f:
    version = f.read().strip()

setuptools.setup(
    name="pgui",
    version=version,
    author="Ciro García",
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
