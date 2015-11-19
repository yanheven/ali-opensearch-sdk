# -*- encoding: utf-8 -*-
'''
opensearch python sdk client.
'''
from opensearchsdk.apiclient import base
from opensearchsdk.v2 import app


class Client(object):
    '''
    opensearch python sdk client.
    '''

    def __init__(self, base_url, key, key_id):
        self.base_url = base_url
        self.key = key
        self.key_id = key_id
        self.app = app.AppManager(self, '/index')
        self.client = base.HTTPClient(base_url)


if __name__ == '__main__':
    import mykey
    url = 'http://opensearch-cn-hangzhou.aliyuncs.com'
    key = mykey.KEY['key_secrete']
    key_id = mykey.KEY['key_id']
    client = Client(url, key, key_id)
    apps = client.app.get(page=1, page_size=1)
    print(apps)
    '''
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
    '''