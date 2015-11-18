# -*- encoding: utf-8 -*-
import json
import httplib
import urlparse
import urllib
import hashlib
import os
import glob
import errno
import time

from opensearchsdk.utils import prepare_url
from opensearchsdk import uexceptions


class HTTPClient(object):
    def __init__(self, base_url, debug=None, timing=None):
        self.base_url = base_url
        self.timing = timing
        self.debug = debug
        self.time = []
        o = urlparse.urlsplit(base_url)
        if o.scheme == 'https':
            self.conn = httplib.HTTPSConnection(o.netloc)
        else:
            self.conn = httplib.HTTPConnection(o.netloc)

    def __del__(self):
        self.conn.close()

    def get_timing(self):
        return self.time

    def reset_timing(self):
        self.time = []

    def get(self, resouse, params):
        resouse += "?" + urllib.urlencode(params)
        if self.debug:
            print("DEBUG START>>>>\nRequest: %s%s\n" %
                  (self.base_url, resouse))
        response = None

        try:
            if self.timing:
                start_time = time.time()
            self.conn.request("GET", resouse)
            if self.timing:
                self.time.append(("%s %s" % ('GET', resouse),
                                  start_time, time.time()))

        except Exception as e:
            raise uexceptions.ConnectionRefused(e)

        respones_raw = self.conn.getresponse().read()

        try:
            response = json.loads(respones_raw)
            if self.debug:
                print(
                    "Respone: %s\n<<<<DEBUG END\n" %
                    json.dumps(response, encoding='UTF-8', ensure_ascii=False,
                               indent=2))

        except Exception as e:
            raise uexceptions.NoJsonFound(e)

        if response.get('RetCode') != 0:
            print('Message:%(Message)s\nRetCode:%(RetCode)s' % response)
            raise uexceptions.BadParameters("message: %s /n bad parameters:%s"
                                            % (response.get('Message'),
                                               params))
        return response


class Manager(object):
    def __init__(self, api):
        self.api = api

    def _get(self, body):
        token = prepare_url.g(self.api.private_key, body)
        body['Signature'] = token
        return self.api.client.get('/', body)