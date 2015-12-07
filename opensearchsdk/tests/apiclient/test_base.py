import mock
import requests

from opensearchsdk.apiclient import api_base
from opensearchsdk.apiclient import exceptions
from opensearchsdk.tests import base
from opensearchsdk.utils import prepare_url


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
FAKE_INVALID_RESP = {
    "status_code": 200,
    "text": BODY,
    "raise_e": ValueError}
RESP_404 = {
    "status_code": 404,
    "text": BODY,
    "raise_e": ValueError}
RESP_400 = {
    "status_code": 400,
    "text": BODY}


class FakeClient(object):
    key = KEY
    key_id = KEY_ID
    http_client = api_base.HTTPClient(URL)


class HTTPClientTest(base.TestCase):
    def setUp(self):
        super(HTTPClientTest, self).setUp()
        requests.request = mock.Mock(
            return_value=base.TestResponse(FAKE_RESP))
        self.http_client = api_base.HTTPClient(URL)

    def test_request_get(self):
        resp = self.http_client.request(GET, RESOURCE_URL)
        requests.request.assert_called_with(
            GET, URL + RESOURCE_URL, headers=HEADERS)
        self.assertEqual(BODY, resp)

    def test_request_post(self):
        resp = self.http_client.request(POST, RESOURCE_URL)
        requests.request.assert_called_with(
            POST, URL + RESOURCE_URL, headers=HEADERS)
        self.assertEqual(BODY, resp)

    @mock.patch.object(requests, 'request',
                       return_value=base.TestResponse(FAKE_INVALID_RESP))
    def test_invalid_response(self, mock_req):
        self.assertRaises(exceptions.InvalidResponse,
                          self.http_client.request, POST, RESOURCE_URL)

    @mock.patch.object(requests, 'request',
                       return_value=base.TestResponse(RESP_404))
    def test_request_404(self, mock_req):
        self.assertEqual('NotFoundException: NotFoundException, app',
                         str(exceptions.NotFoundException(details='app')))
        self.assertRaises(exceptions.NotFoundException,
                          self.http_client.request, POST, RESOURCE_URL)

    @mock.patch.object(requests, 'request',
                       return_value=base.TestResponse(RESP_400))
    def test_request_400(self, mock_req):
        self.assertRaises(exceptions.HttpException,
                          self.http_client.request, POST, RESOURCE_URL)


class ManagerTest(base.TestCase):
    def setUp(self):
        super(ManagerTest, self).setUp()
        self.ori_request = api_base.HTTPClient.request
        self.ori_get_signature = prepare_url.get_signature
        api_base.HTTPClient.request = mock.Mock(return_value=FAKE_RESP)
        prepare_url.get_signature = mock.Mock(return_value=SIGN)
        self.manager = api_base.Manager(FakeClient, RESOURCE_URL)

    def tearDown(self):
        super(ManagerTest, self).tearDown()
        api_base.HTTPClient.request = self.ori_request
        prepare_url.get_signature = self.ori_get_signature

    def test_request(self):
        resp = self.manager.send_request(GET, SPEC_URL, BODY)
        api_base.HTTPClient.request.assert_called_with(
            GET, RESOURCE_URL+SPEC_URL, data=SIGNED_BODY)
        prepare_url.get_signature.assert_called_with(GET, BODY, KEY, KEY_ID)
        self.assertEqual(FAKE_RESP, resp)

    @mock.patch('opensearchsdk.apiclient.api_base.urlencode')
    def test_get(self, mock_urlencode):
        mock_urlencode.return_value = ENCODE_BODY
        resp = self.manager.send_get(BODY, SPEC_URL)

        prepare_url.get_signature.assert_called_with(GET, BODY, KEY, KEY_ID)
        mock_urlencode.assert_called_with(BODY)
        self.assertEqual(FAKE_RESP, resp)

    @mock.patch.object(api_base.Manager, 'send_request')
    def test_post(self, mock_request):
        mock_request.return_value = FAKE_RESP
        resp = self.manager.send_post(BODY, SPEC_URL)

        mock_request.assert_called_with(POST, SPEC_URL, BODY)
        self.assertEqual(FAKE_RESP, resp)
