import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = []

setup(
    name = "lpstats",
    version = "0.0.1",
    author = "Manuel Kiessling",
    author_email = "manuel@kiessling.net",
    description = ("Web-based Leanpub statistics viewer"),
    license = "MIT",
    keywords = "leanpub api statistics",
    url = "https://github.com/manuelkiessling/lpstats",
    packages=['lpstats'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=requires,
    test_suite='lpstats',
)
