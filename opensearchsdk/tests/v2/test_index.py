import mock

from opensearchsdk.apiclient.api_base import Manager
from opensearchsdk.tests import base
from opensearchsdk.v2.index import IndexManager


class AppTest(base.TestCase):
    def setUp(self):
        super(AppTest, self).setUp()
        self.index_manager = IndexManager('', '')
        mock_send = mock.Mock()
        Manager.send_get = Manager.send_post = mock_send

    def test_refactor_without_data(self):
        self.index_manager.refactor('a')
        body = dict(action='createtask',)
        spec_url = '/a'
        Manager.send_post.assert_called_with(body, spec_url)

    def test_refactor_with_data(self):
        self.index_manager.refactor('a', 'b', 'c')
        body = dict(action='createtask',
                    operate='import',
                    table_name='c')
        spec_url = '/a'
        Manager.send_post.assert_called_with(body, spec_url)
