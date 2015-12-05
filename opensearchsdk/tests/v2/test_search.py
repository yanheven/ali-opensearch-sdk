import mock

from opensearchsdk.apiclient.api_base import Manager
from opensearchsdk.tests import base
from opensearchsdk.v2.search import SearchManager


class AppTest(base.TestCase):
    def setUp(self):
        super(AppTest, self).setUp()
        self.search_manager = SearchManager('', '')
        mock_send = mock.Mock()
        Manager.send_get = Manager.send_post = mock_send

    def test_search(self):
        # simple search
        self.search_manager.search('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        body = dict(query='a', index_name='b', fetch_fields='c', qp='d',
                    disable='e', first_formula_name='f', formula_name='g',
                    summary='h')
        Manager.send_get.assert_called_with(body)

        # first combine search
        body['scroll'] = '1h'
        body['search_type'] = 'scan'

        self.search_manager.search('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                   '1h', 'scan')
        Manager.send_get.assert_called_with(body)

        # second combine search
        body = dict(scroll='1h', scroll_id='i')
        self.search_manager.search(**body)
        Manager.send_get.assert_called_with(body)
