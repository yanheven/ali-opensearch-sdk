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


def create_app(client):
    app = client.app.create('test_app', 'a')
    print(app)
    '''
    {
        u'status': u'OK',
        u'result': {
                        u'index_name': u'test_app'
                    },
        u'request_id': u'1449146731021309800470027'
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
    data_ret = client.data.create('test_app', table_name, items)
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


def search(client):
    # simple search
    body = dict(index_name='test_app',
                query='query=id:"0"',
                fetch_fields='testname',
                first_formula_name='default',
                formula_name='default',
                summary='summary_snipped:1,summary_field:title,summ'
                        'ary_element:high,summary_len:32,summary_el'
                        'lipsis:...;summary_snipped:2,summary_field'
                        ':body,summary_element:high,summary_len:60,s'
                        'ummary_ellipsis:...')

    def simple_search():
        res = client.search.search(**body)
        print(res)
        '''
        {
            u'status': u'OK',
            u'tracer': u'',
            u'errors': [],
            u'result': {
                            u'searchtime': 0.005986,
                            u'items': [
                                        {
                                            u'index_name': u'test_app',
                                            u'testname': u'0',
                                        }
                                    ],
                            u'facet': [],
                            u'viewtotal': 1,
                            u'num': 1,
                            u'total': 1
                        },
            u'request_id': u'144932743917790790023680'
        }
        '''

    def combine_search_1():
        # first combine search
        body['scroll'] = '1h'
        body['search_type'] = 'scan'
        res = client.search.search(**body)
        print(res)
        '''
        {
            u'status': u'OK',
            u'tracer': u'',
            u'errors': [],
            u'result': {
                            u'scroll_id': u'eJyNjk1LxDAQhn9NcizdZNnSQw+rXkTUk
                            +dQk2k7ki8zqW7315sWhRUVhAwZnnmHZ45aA9EdLLemexpz87
                            Ab8f7t0b2fw5kr21NWek4UUjdgoozeQyKdgrVouCqdVXCKKqO
                            Dbrfft1KKRtZt2/ABsp7UgGANdRko+94BR2/gpNZ2Y6qPkb/O
                            kJZOBz/gyOTNEJLrM5PHFwqeiUN5W6KM0BTMhKhLcZqd68vi5
                            6/IY4ywJnZMXH/R7YDCMmYLFxwsOPCrZsJxuhhY8AVK8S1rMR
                            JS4VVVMXn1Uyl+UT4Hs/zfeKj/NH4A34SVcg==',
                            u'searchtime': 0.002997,
                            u'items': [],
                            u'facet': [],
                            u'viewtotal': 1,
                            u'num': 0,
                            u'total': 1
                        },
            u'request_id': u'144932913017790788000125'
        }
        '''
        return res.get('result').get('scroll_id')

    def combine_search_2(scroll_id):
        del body['scroll']
        body['scroll_id'] = scroll_id
        res = client.search.search(**body)
        print(res)
        '''
        the same as simple search
        '''

    simple_search()
    scroll_id = combine_search_1()
    combine_search_2(scroll_id)


def suggest(client):
    res = client.suggest.suggest('的', 'test_app', 's2')
    print(res)
    '''
    {
        u'errors': [
            {
                u'message': u'nosuggesterdataonline',
                u'code': 2422
            }
        ],
        u'suggestions': [],
        u'searchtime': 0.034475,
        u'request_id': u'144937817217790789042028'
    }
    '''


def index_refactor(client):
    # only refactor index
    def refactor_only():
        res = client.index.refactor('test_app')
        print(res)
        '''
        {
            u'status': u'OK',
            u'result': {
                u'task_id': u'159469'
            },
            u'request_id': u'1449378626069143700426870'
        }
        '''
    def refactor_import_data():
        #  refactor index and import data
        res = client.index.refactor('test_app', 'import', 'id')
        print(res)

    # refactor_only()
    refactor_import_data()


def get_error_log(client):
    res = client.log.get('test_app', '1', 1, 'ASC')
    print(res)
    '''
    {
        u'status': u'OK',
        u'result': {
            u'count': 0,
            u'items': [],
            u'page': 1,
            u'page_size': u'1'
        },
        u'request_id': u'1449379073037249300677090'
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
    # list_app(client)
    # create_app(client)

    # must create app before create data process

    # creat_data_process(client)
    # search(client)
    # suggest(client)
    # index_refactor(client)
    # get_error_log(client)
