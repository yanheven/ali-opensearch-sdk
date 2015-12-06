import mock

from opensearchsdk.apiclient.api_base import Manager
from opensearchsdk.tests import base
from opensearchsdk.v2.log import LogManager


class AppTest(base.TestCase):
    def setUp(self):
        super(AppTest, self).setUp()
        self.log_manager = LogManager('', '')
        mock_send = mock.Mock()
        Manager.send_get = Manager.send_post = mock_send

    def test_get(self):
        self.log_manager.get('a', '1', 1, 'ASC')
        body = dict(page='1',
                    page_size='1',
                    sort_mode='ASC')
        spec_url = '/a'
        Manager.send_post.assert_called_with(body, spec_url)
