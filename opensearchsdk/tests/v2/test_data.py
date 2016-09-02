import mock

from opensearchsdk.apiclient.api_base import Manager
from opensearchsdk.tests import base
from opensearchsdk.v2.data import DataManager


FAKE_RESP = {'data': 'name'}


class AppTest(base.TestCase):
    def setUp(self):
        super(AppTest, self).setUp()
        self.data_manager = DataManager('', '')
        mock_send = mock.Mock(return_value=FAKE_RESP)
        Manager.send_get = Manager.send_post = mock_send

    def test_list(self):
        resp = self.data_manager.create('a', '1', '2')
        self.assertEqual(FAKE_RESP, resp)
        Manager.send_post.assert_called_with({'table_name': '1',
                                              'items': '2'},
                                             '/a')
