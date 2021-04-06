
# -*- coding: UTF-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pgui",
    version="0.0.28",
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
