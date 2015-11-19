import mock
import requests

from opensearchsdk.tests import base
from opensearchsdk.apiclient import api_base

URL = 'http://www.aliyun.com'

HEADERS = {'User-Agent': 'ali-opensearch-python-client',
         'Content-Type': 'application/x-www-form-urlencoded'}


def fake_resp():
    return base.TestResponse({
        "status_code": 200,
        "text": {"hello": "ali"}})


def get_http_client():
    http_client = api_base.HTTPClient(URL)
    return http_client


def get_manager():
    manager = api_base.Manager()


class FakeHttpClient(object):
    request = fake_resp()


mock_req = mock.Mock(return_value=fake_resp())


class HTTPClientTest(base.TestCase):
    @mock.patch.object(requests, 'request', mock_req)
    def test_request(self):
        http_client = get_http_client()

        def get():
            resp = http_client.request('GET', '/hi')
            mock_req.assert_called_with('GET', URL + '/hi', headers=HEADERS)
            self.assertEqual({"hello": "ali"}, resp)

        def post():
            resp = http_client.request('POST', '/hello')
            mock_req.assert_called_with(
                'POST', URL + '/hello', headers=HEADERS)
            self.assertEqual({"hello": "ali"}, resp)

        get()
        post()









