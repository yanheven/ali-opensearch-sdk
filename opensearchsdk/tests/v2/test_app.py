import mock

from opensearchsdk.apiclient.api_base import Manager
from opensearchsdk.tests import base
from opensearchsdk.v2.app import AppManager


FAKE_RESP = {'app': 'name'}


class AppTest(base.TestCase):
    def setUp(self):
        super(AppTest, self).setUp()
        self.app_manager = AppManager('', '')
        mock_send = mock.Mock(return_value=FAKE_RESP)
        self.ori_get = Manager.send_get
        self.ori_post = Manager.send_post
        Manager.send_get = Manager.send_post = mock_send

    def tearDown(self):
        super(AppTest, self).tearDown()
        Manager.send_get = self.ori_get
        Manager.send_post = self.ori_post

    def test_list(self):
        resp = self.app_manager.list(1, 2)
        self.assertEqual(FAKE_RESP, resp)
        Manager.send_post.assert_called_with({'page': '1', 'page_size': '2'})
