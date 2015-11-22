# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class DataManager(api_base.Manager):
    """Data Process resource manage class"""
    def create(self, table_name, items):
        """
        create data process to application
        :param table_name: table name of upload items
        :param items: items in json format
        :return:{"status":"OK","request_id":"10373587"}
        """
        body = dict(table_name=table_name, items=items)
        return self.send_post(body)
