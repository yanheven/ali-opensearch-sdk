import mock
import requests

from opensearchsdk.apiclient import api_base
from opensearchsdk.tests import base


URL = 'http://www.aliyun.com'
RESOURCE_URL = '/index'
SPEC_URL = ''
HEADERS = {'User-Agent': 'ali-opensearch-python-client',
           'Content-Type': 'application/x-www-form-urlencoded'}
BODY = {'a': '1'}
SIGN = 'sign'
SIGNED_BODY = {'Signature': SIGN}
SIGNED_BODY.update(BODY)
ENCODE_BODY = "{'b': 2}"
KEY = 'key'
KEY_ID = 'key_id'
GET = 'GET'
POST = 'POST'
FAKE_RESP = {
    "status_code": 200,
    "text": BODY}


def fake_resp():
    return base.TestResponse(FAKE_RESP)


class FakeClient(object):
    key = KEY
    key_id = KEY_ID
    http_client = api_base.HTTPClient(URL)


mock_req = mock.Mock(return_value=base.TestResponse(FAKE_RESP))


class HTTPClientTest(base.TestCase):
    @mock.patch.object(requests, 'request', mock_req)
    def test_request(self):
        http_client = http_client = api_base.HTTPClient(URL)

        def get():
            resp = http_client.request(GET, RESOURCE_URL)
            mock_req.assert_called_with(GET, URL + RESOURCE_URL, headers=HEADERS)
            self.assertEqual(BODY, resp)

        def post():
            resp = http_client.request(POST, RESOURCE_URL)
            mock_req.assert_called_with(
                POST, URL + RESOURCE_URL, headers=HEADERS)
            self.assertEqual(BODY, resp)

        get()
        post()


class ManagerTest(base.TestCase):

    @mock.patch.object(api_base.HTTPClient, 'request')
    @mock.patch('opensearchsdk.utils.prepare_url.get_signature')
    def test_request(self, mock_get_sign, mock_http):
        mock_http.return_value = FAKE_RESP
        mock_get_sign.return_value = SIGN
        manager = api_base.Manager(FakeClient, RESOURCE_URL)
        resp = manager.send_request(GET, SPEC_URL, BODY)

        mock_http.assert_called_with(
            GET, RESOURCE_URL+SPEC_URL, data=SIGNED_BODY)
        mock_get_sign.assert_called_with(GET, BODY, KEY, KEY_ID)
        self.assertEqual(FAKE_RESP, resp)

    @mock.patch.object(api_base.HTTPClient, 'request')
    @mock.patch('opensearchsdk.utils.prepare_url.get_signature')
    @mock.patch('urllib.urlencode')
    def test_get(self, mock_urlencode, mock_get_sign, mock_http):
        mock_http.return_value = FAKE_RESP
        mock_get_sign.return_value = SIGN
        mock_urlencode.return_value = ENCODE_BODY
        manager = api_base.Manager(FakeClient, RESOURCE_URL)
        resp = manager.send_get(BODY, SPEC_URL)

        mock_http.assert_called_with(
            GET, RESOURCE_URL+SPEC_URL+'?'+ENCODE_BODY)
        mock_get_sign.assert_called_with(GET, BODY, KEY, KEY_ID)
        mock_urlencode.assert_called_with(BODY)
        self.assertEqual(FAKE_RESP, resp)

    @mock.patch.object(api_base.Manager, '_request')
    def test_post(self, mock_request):
        mock_request.return_value = FAKE_RESP
        manager = api_base.Manager(FakeClient, RESOURCE_URL)
        resp = manager.send_post(BODY, SPEC_URL)

        mock_request.assert_called_with(POST, SPEC_URL, BODY)
        self.assertEqual(FAKE_RESP, resp)















