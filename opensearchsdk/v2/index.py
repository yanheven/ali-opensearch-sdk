# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class IndexManager(api_base.Manager):
    """Index resource manage class"""
    def refactor(self, name, operate=None, table_name=None):
        """
        refactor index
        :param name: application name
        :param operate: weather import data for refactor
        :param table_name: import data tables name, separated by ','
        :return:
        """
        body = dict(action='createtask')
        if operate and table_name:
            body['operate'] = 'import'
            body['table_name'] = table_name
        spec_url = '/' + name

        return self.send_get(body, spec_url)
