import mock

from opensearchsdk.apiclient.api_base import Manager
from opensearchsdk.tests import base
from opensearchsdk.v2.suggest import SuggestManager


class AppTest(base.TestCase):
    def setUp(self):
        super(AppTest, self).setUp()
        self.suggest_manager = SuggestManager('', '')
        mock_send = mock.Mock()
        Manager.send_get = Manager.send_post = mock_send

    def test_list(self):
        self.suggest_manager.suggest('a', 'b', 'c', 1)
        body = dict(query='a',
                    index_name='b',
                    suggest_name='c',
                    hit='1')
        Manager.send_post.assert_called_with(body)
