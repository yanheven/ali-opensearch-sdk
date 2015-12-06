# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class SuggestManager(api_base.Manager):
    """Suggest resource manage class"""
    def suggest(self, query, index_name, suggest_name, hit=10):
        """
        get suggest from user input.
        :param query: query string
        :param index_name: application name
        :param suggest_name: suggestion rule
        :param hit: count of suggestion, 1-10, default 10
        :return:
        """
        body = dict(query=query,
                    index_name=index_name,
                    suggest_name=suggest_name,
                    hit=str(hit))
        return self.send_get(body)
