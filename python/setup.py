__author__ = 'kkrzysztofik'

from setuptools import setup
from version import version

setup(
    name='YouTrack-Python',
    version=version,
    author='JetBrains s.r.o',
    packages=['youtrack'],
    url='http://www.jetbrains.com/youtrack/',
    description='Python library that wraps YouTrack REST API.',
    license='Apache License, Version 2.0',
    install_requires=[
        "httplib2 >= 0.7.4",
        "pyactiveresource >= 2.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7"
    ]
)
