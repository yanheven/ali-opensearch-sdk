# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class LogManager(api_base.Manager):
    """Error Log resource manage class"""
    def get(self, name, page, page_size, sort_mode):
        """
        get error log of application
        :param name: application name
        :param page: (str)page number
        :param page_size: (int)page size
        :param sort_mode: 'ASC' or 'DESC'
        :return: (json)log content
        """
        body = dict(page=page,
                    page_size=str(page_size),
                    sort_mode=sort_mode)
        spec_url = '/' + name

        return self.send_get(body, spec_url)
