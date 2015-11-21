# -*- encoding: utf-8 -*-
import json

from opensearchsdk.client import Client


def list_app(client):
    apps = client.app.list(page=1, page_size=1)
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


def creat_data_process(client):
    table_name = 'test_table'
    items = [
                {
                    "cmd": "add",
                    "timestamp": 1401342874777,
                    "fields": {
                        "id": "1",
                        "title": "This is the title",
                        "body": "This is the body"
                    }
                },
                {
                    "cmd": "update",
                    "timestamp": 1401342874778,
                    "fields": {
                        "id": "2",
                        "title": "This is the new title"
                    }
                },
                {
                    "cmd": "delete",
                    "fields": {
                        "id": "3"
                    }
                }
            ]
    items = json.dumps(items)
    data_ret = client.data.create(table_name, items)
    print(data_ret)
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
            u'request_id': u'1448079259020634800692900'
        }
    '''


if __name__ == '__main__':
    import mykey
    import logging
    LOG = logging.basicConfig(level=logging.DEBUG,
                              format="[%(asctime)s] %(name)s:"
                                     "%(levelname)s: %(message)s")
    url = 'http://opensearch-cn-hangzhou.aliyuncs.com'
    key = mykey.KEY['key_secrete']
    key_id = mykey.KEY['key_id']
    client = Client(url, key, key_id)
    list_app(client)
    creat_data_process(client)

