from opensearchsdk import client
from opensearchsdk.tests import base


URL = 'http://www.aliyun.com'
KEY = 'KEY'
KEY_ID = 'KEY_ID'


class ClientTest(base.TestCase):
    def test_passing_property(self):
        c = client.Client(URL, KEY, KEY_ID)
        self.assertEqual(KEY, c.key)
        self.assertEqual(URL, c.http_client.base_url)
        self.assertEqual(client.APP_URL, c.app.resource_url)
        self.assertEqual(c, c.app.api)
