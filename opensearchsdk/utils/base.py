# -*- encoding: utf-8 -*-
import logging
import requests

from opensearchsdk.apiclient import exceptions
from opensearchsdk.utils import prepare_url

_logger = logging.getLogger(__name__)


class HTTPClient(object):
    user_agent = 'ali-opensearch-python-client'

    def __init__(self, base_url, ):
        self.base_url = base_url

    def request(self, method, url, **kwargs):

        kwargs.setdefault("headers", {})
        kwargs["headers"]["User-Agent"] = self.user_agent
        kwargs["headers"]["Content-Type"] = 'application/x-www-form-urlencoded'
        self._logger_req(method, url, **kwargs)
        resp = requests.request(method, url, **kwargs)
        self._logger_resp(resp)
        try:
            resp.raise_for_status()
        except requests.RequestException as e:
            if resp.status_code == 404:
                exc_type = exceptions.NotFoundException
            else:
                exc_type = exceptions.HttpException
            raise exc_type(e,
                           details=self._parse_error_resp(resp),
                           status_code=resp.status_code)
        try:
            resp.body = resp.json()
        except ValueError as e:
            raise exceptions.InvalidResponse(response=resp)
        return resp

    def _parse_error_resp(self, resp):
        try:
            jresp = resp.json()
            return jresp
        except ValueError:
            pass
        return resp.text

    def _logger_req(self, method, url, **kwargs):
        string_parts = [
            "curl -i",
            "-X '%s'" % method,
            "'%s'" % url,
        ]
        for element in kwargs['headers'].items():
            header = " -H '%s: %s'" % element
            string_parts.append(header)
        data = kwargs['data']
        string_parts.append("'" + data + "'")
        _logger.debug("REQ: %s" % " ".join(string_parts))

    def _logger_resp(self, resp):
        _logger.debug(
            "RESP: [%s] %r" % (
                resp.status_code,
                resp.headers,
            ),
        )
        if resp._content_consumed:
            _logger.debug(
                "RESP BODY: %s",
                resp.text,
            )
        _logger.debug(
            "encoding: %s",
            resp.encoding,
        )


class Manager(object):
    def __init__(self, api):
        self.api = api

    def _request(self, method, url, body):
        key = self.api.key
        key_id = self.api.key_id
        body['Signature'] = prepare_url.get_signature(
            method, body, key, key_id)
        return self.api.client.request(method, url, body)

    def get(self, url, body):
        return self._request('GET', url, body)

    def post(self, url, body):
        return self._request('POST', url, body)
