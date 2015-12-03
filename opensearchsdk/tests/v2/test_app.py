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
        Manager.send_get = Manager.send_post = mock_send

    def test_list(self):
        resp = self.app_manager.list(1, 2)
        self.assertEqual(FAKE_RESP, resp)
        Manager.send_post.assert_called_with({'page': '1', 'page_size': '2'})

    def test_create(self):
        self.app_manager.create('a', 'b')
        Manager.send_post.assert_called_with({'action': 'create',
                                              'template': 'b'},
                                             '/a')

    def test_delete(self):
        self.app_manager.delete('a')
        Manager.send_post.assert_called_with({'action': 'delete'}, '/a')

    def test_get(self):
        self.app_manager.get('a')
        Manager.send_post.assert_called_with({'action': 'status'}, '/a')
