# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import base


class AppManager(base.Manager):
    """Application resource manage class"""
    def get(self, page=None, page_size=None):
        """
        get application list with given page and page size.
        :param page:
        :param page_size:
        :return: app list
        """
        body = {}
        if page is not None:
            body['page'] = page
        if page_size is not None:
            body['page_size'] = page_size

        return self._post(body)

