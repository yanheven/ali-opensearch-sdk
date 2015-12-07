[![Build Status](https://travis-ci.org/yanheven/ali-opensearch-sdk.svg?branch=master)](https://travis-ci.org/yanheven/ali-opensearch-sdk)
[![Coverage Status](https://coveralls.io/repos/yanheven/ali-opensearch-sdk/badge.svg?branch=master&service=github)](https://coveralls.io/github/yanheven/ali-opensearch-sdk?branch=master)
[![PyPI version](https://badge.fury.io/py/ali-opensearch.svg)](https://badge.fury.io/py/ali-opensearch)  

### Aliyun OpenSearch Python SDK

ali-opensearch-sdk is a python SDK for [Aliyun OpenSearch](http://www.aliyun.com/product/opensearch) Product.    
Based on OpenSearch API version v2. This SDK supports both python2.x and python3.x.  
Pypi link：[https://pypi.python.org/pypi/ucloudclient](https://pypi.python.org/pypi/ali-opensearch/2.0.0)  
Project manage [Launchpad](https://launchpad.net/ali-opensearch-python-sdk)

#### 1 Design
##### 1.1 SDK structure
There are 7 type of resources provided by opensearch, they are:   
 
1, app: Application  
2, data: Data Process  
3, search: Search Related Action  
4, suggest: Suggestion for Search  
5, index: Index Reconstruction  
6, quota: Quota Management  
7, log: Error Log Query  

There are 5 Operation for almost all resources, they are CURD as follow:  

1, list: list all of this type of resources.    
2, show: show detail information of a specific resource.      
3,4,5, CUD: create, update and delete a specific resource.

###### 1.1.1 app Operation：

#### 2, Installation:

You can install via pip:

    #pip install ali-opensearch

Or, From Source code:

    #git clone https://git.oschina.net/yanhyphen/ali-opensearch-sdk.git
    #cd ali-opensearch-sdk
    #python setup.py install

####  3, Getting Started ：

    from opensearchsdk.client import Client as osclient
    client = osclient(base_url, key, key_id)
    apps = client.app.list()
    print apps

output:

    {
        u'status': u'OK',
        u'total': u'1',
        u'result': [
                        {
                            u'description': u'test',
                            u'created': u'1447753400',
                            u'id': u'119631',
                            u'name': u'test'
                        }
                    ],
        u'request_id': u'1447866418002866600607068'
    }

More examples can be found in `opensearchsdk/demo.py`.  
Note: All return data from server were remained. 

#### 4, Contribute and BUG:
This project was managed via [Launchpad](https://launchpad.net/ali-opensearch-python-sdk).  
Welcome to log bugs and commit patch.
Code style follow the PEP8 rules.

#### 5, License：
Apache License Version 2.0

#### 6, Release Note：
1, V2.0.0-dev Provide only few functions of opensearch, not yet cover all functions.
2, V2.0.0 completed all api functions.
3, V2.0.1 add compatibility for python3.5.

