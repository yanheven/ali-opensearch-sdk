# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class AppManager(api_base.Manager):
    """Application resource manage class"""
    def list(self, page=None, page_size=None):
        """
        get application list with given page and page size.
        :param page:
        :param page_size:
        :return: app list
        """
        body = {}
        if page is not None:
            body['page'] = str(page)
        if page_size is not None:
            body['page_size'] = str(page_size)

        return self._post(body)

