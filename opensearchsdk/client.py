# -*- encoding: utf-8 -*-
'''
opensearch python sdk client.
'''
from opensearchsdk.v2 import app
from utils import base


class Client(object):
    '''
    opensearch python sdk client.
    '''

    def __init__(self, base_url, key, key_id):
        self.base_url = base_url
        self.key = key
        self.key_id = key_id
        self.app = app.UhostManager(self)
        self.client = base.HTTPClient(base_url)
