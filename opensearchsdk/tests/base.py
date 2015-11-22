import requests
import testtools


class TestCase(testtools.TestCase):
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

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def json(self):
        return self._text

    def raise_for_status(self):
        pass
