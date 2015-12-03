# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class SearchManager(api_base.Manager):
    """Search resource manage class"""
    def search(self, query, index_name, fetch_fields=None, qp=None,
               disable=None, first_formula_name=None, formula_name=None,
               summary=None):
        """
        do search with given parameters
        :param query: query string
        :param index_name: application name(s), separate by ';'
        :param fetch_fields: field to return, separate by ';'
        :param qp: search analyse rules, separate by ','
        :param disable: whether turn off search analyse
        :param first_formula_name:
        :param formula_name:
        :param summary:
        :return: json, search result
        """
        body = dict(query=query, index_name=index_name)
        if fetch_fields:
            body['fetch_fields'] = fetch_fields
        if qp:
            body['qp'] = qp
        if disable:
            body['disable'] = disable
        if first_formula_name:
            body['first_formula_name'] = first_formula_name
        if formula_name:
            body['formula_name'] = formula_name
        if summary:
            body['summary'] = summary

        return self.send_get(body)

    def combine_search(self, scroll, scroll_id=None):
        """
        combination search
        :param scroll: expire time, default ms
        :param scroll_id: last search id, None if first time search
        :return: json, search result
        """
        body = dict(scroll=scroll)

        # if not the first time, must with last search id.
        if scroll_id:
            body['scroll_id'] = scroll_id
        else:
            body['search_type'] = 'scan'

        return self.send_get(body)
