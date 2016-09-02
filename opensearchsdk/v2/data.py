# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class DataManager(api_base.Manager):
    """Data Process resource manage class"""
    def create(self, app_name, table_name, items):
        """
        create data process to application
        :param app_name: app name
        :param table_name: table name of upload items
        :param items: items in json format
        :return:{"status":"OK","request_id":"10373587"}
        """
        body = dict(table_name=table_name, items=items)
        spec_url = '/' + app_name
        return self.send_post(body, spec_url)
