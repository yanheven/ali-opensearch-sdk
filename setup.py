#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from setuptools import setup,find_packages

setup(
    name='ali-opensearch',
    version='2.0.0',
    packages = find_packages(),
    keywords=('OpenSearch SDK', 'Ali Cloud'),
    description='Python SDK for OpenSearch of Ali Cloud',
    license='Apache License Version 2.0',
    url='https://github.com/yanheven/ali-opensearch-sdk',
    author='Yan Haifeng(颜海峰)',
    author_email='yanheven@qq.com',

    include_package_data=True,
    platforms='python2.7',
    # install_requires=['PrettyTable>=0.7,<0.8', 'six>=1.9.0'],
    entry_points={
        'console_scripts': [],
    },
    classifiers = ['Operating System :: MacOS',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux']
)
