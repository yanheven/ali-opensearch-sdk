import requests
import unittest


class TestCase(unittest.TestCase):
    """wrap testtools.TestCase"""
    def setUp(self):
        super(TestCase, self).setUp()


class TestResponse(requests.Response):
    """wrap request.Response"""
    def __init__(self, data):
        super(TestResponse, self).__init__()
        self._text = None
        self.status_code = data.get('status_code')
        self.headers = data.get('headers')
        self._text = data.get('text')
        self.raise_e = data.get('raise_e', '')
    #
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__

    def json(self):
        if self.raise_e:
            raise self.raise_e
        return self._text
