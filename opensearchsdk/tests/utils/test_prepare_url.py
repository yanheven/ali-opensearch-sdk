# -*- encoding: utf-8 -*-
import mock
import six

from opensearchsdk.utils import prepare_url
from opensearchsdk.tests import base


COMMON_PARAMS = {'Version': 'v2',
                 'AccessKeyId': 'testid',
                 'SignatureMethod': 'HMAC-SHA1',
                 'SignatureVersion': '1.0',
                 'SignatureNonce': '14053016951271226',
                 'Timestamp': '2014-07-14T01:34:55Z'
                 }
BODY = {'query': "config=format:json,start:0,hit:20&&query:'的'",
        'index_name': 'ut_3885312',
        'format': 'json',
        'fetch_fields': 'title;gmt_modified'}
METHOD = 'GET'
KEY_ID = 'testid'
KEY = 'testsecret'
SIGNATURE = "fxGidmIYSsx2AMa8onxuavOijuE="
STEP_1 = 'AccessKeyId=testid&SignatureMethod=HMAC-SHA1&SignatureNonce=1405' \
         '3016951271226&SignatureVersion=1.0&Timestamp=2014-07-14T01%3A34%' \
         '3A55Z&Version=v2&fetch_fields=title%3Bgmt_modified&format=json&i' \
         'ndex_name=ut_3885312&query=config%3Dformat%3Ajson%2Cstart%3A0%2C' \
         'hit%3A20%26%26query%3A%27%E7%9A%84%27'
STEP_2 = "GET&%2F&AccessKeyId%3Dtestid%26SignatureMethod%3DHMAC-SHA1%26Signatu" \
         "reNonce%3D14053016951271226%26SignatureVersion%3D1.0%26Timestamp%3D2" \
         "014-07-14T01%253A34%253A55Z%26Version%3Dv2%26fetch_fields%3Dtitle%25" \
         "3Bgmt_modified%26format%3Djson%26index_name%3Dut_3885312%26query%3Dc" \
         "onfig%253Dformat%253Ajson%252Cstart%253A0%252Chit%253A20%2526%2526qu" \
         "ery%253A%2527%25E7%259A%2584%2527"
SAFE = {' ': '%20', '~': '~'}


class TokenTest(base.TestCase):

    def test_get_common_params(self):
        common_params = prepare_url.get_common_params(KEY_ID)
        self.assertEqual(6, len(common_params))
        self.assertEqual(COMMON_PARAMS['Version'], common_params['Version'])
        self.assertEqual(
            COMMON_PARAMS['AccessKeyId'], common_params['AccessKeyId'])
        self.assertEqual(
            COMMON_PARAMS['SignatureMethod'], common_params['SignatureMethod'])
        self.assertEqual(
            COMMON_PARAMS['SignatureVersion'],
            common_params['SignatureVersion'])
        self.assertEqual(20, len(common_params['Timestamp']))

    def test_url_quote(self):
        for k, v in SAFE.items():
            quoted = prepare_url.url_quote(k)
            self.assertEqual(v, quoted)

    def test_get_quote_body(self):
        body = BODY
        body.update(COMMON_PARAMS)
        quoted_body = prepare_url.get_quote_body(body)
        self.assertEqual(STEP_1, quoted_body)

    def test_get_str_to_sign(self):
        str_to_sign = prepare_url.get_str_to_sign(STEP_1, METHOD)
        self.assertEqual(STEP_2, str_to_sign)

    def test_sign_str(self):
        signature = prepare_url.sign_str(KEY, STEP_2)
        if isinstance(signature, six.binary_type):
            signature = signature.decode()
        self.assertEqual(SIGNATURE, signature)

    @mock.patch('opensearchsdk.utils.prepare_url.get_common_params',
                mock.Mock(return_value=COMMON_PARAMS))
    def test_get_signature(self):
        signature = prepare_url.get_signature(METHOD, BODY, KEY, KEY_ID)
        if isinstance(signature, six.binary_type):
            signature = signature.decode()
        self.assertEqual(SIGNATURE, signature)
