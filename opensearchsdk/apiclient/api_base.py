# -*- encoding: utf-8 -*-
import logging
import requests
from six.moves.urllib.parse import urlencode
from opensearchsdk.apiclient import exceptions
from opensearchsdk.utils import prepare_url


USER_AGENT = 'ali-opensearch-python-client'
_logger = logging.getLogger(__name__)


class HTTPClient(object):
    """HTTP client for sending request to server"""
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method, url, **kwargs):
        url = self.base_url + url
        kwargs.setdefault("headers", {})
        kwargs["headers"]["User-Agent"] = USER_AGENT
        kwargs["headers"]["Content-Type"] = 'application/x-www-form-urlencoded'
        # self._logger_req(method, url, **kwargs)
        resp = requests.request(method, url, **kwargs)
        # self._logger_resp(resp)
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
            resp_body = resp.json()
        except ValueError:
            raise exceptions.InvalidResponse(response=resp)
        return resp_body

    def _parse_error_resp(self, resp):
        try:
            jresp = resp.json()
            return jresp
        except ValueError:
            pass
        return resp.text
    #
    # def _logger_req(self, method, url, **kwargs):
    #     if not _logger.isEnabledFor(logging.DEBUG):
    #         return
    #     string_parts = [
    #         "curl -i",
    #         "-X '%s'" % method,
    #         "'%s'" % url,
    #     ]
    #     if method != 'GET':
    #         for element in kwargs['headers'].items():
    #             header = " -H '%s: %s'" % element
    #             string_parts.append(header)
    #         string_parts.append('--data')
    #         data = kwargs.get('data', '')
    #         if data:
    #             data_str = urllib.urlencode(data)
    #             data_str = "'" + data_str + "'"
    #             string_parts.append(data_str)
    #     print("REQ: %s" % " ".join(string_parts))
    #     _logger.debug("REQ: %s" % " ".join(string_parts))
    #
    # def _logger_resp(self, resp):
    #     if not _logger.isEnabledFor(logging.DEBUG):
    #         return
    #     _logger.debug(
    #         "RESP: [%s] %r" % (
    #             resp.status_code,
    #             resp.headers,
    #         ),
    #     )
    #     # if resp._content_consumed:
    #     #     _logger.debug(
    #     #         "RESP BODY: %s",
    #     #         resp.text,
    #     #     )
    #     _logger.debug(
    #         "encoding: %s",
    #         resp.encoding,
    #     )


class Manager(object):
    def __init__(self, api, resource_url):
        self.api = api
        self.resource_url = resource_url

    def send_request(self, method, spec_url, body):
        key = self.api.key
        key_id = self.api.key_id
        body['Signature'] = prepare_url.get_signature(
            method, body, key, key_id)
        final_url = self.resource_url + spec_url
        return self.api.http_client.request(method, final_url, data=body)

    def send_get(self, body, spec_url=''):
        key = self.api.key
        key_id = self.api.key_id
        body['Signature'] = prepare_url.get_signature(
            'GET', body, key, key_id)
        encoded_url = urlencode(body)
        final_url = self.resource_url + spec_url + '?' + encoded_url
        return self.api.http_client.request('GET', final_url)

    def send_post(self, body, spec_url=''):
        return self.send_request('POST', spec_url, body)
