# _*_ encoding: utf-8 _*_
from testtools import TestCase

from opensearchsdk.utils import prepare_url


BODY = {"Version": "2014-05-26",
        "AccessKeyId": "testid",
        "SignatureMethod": "HMAC-SHA1",
        "SignatureVersion": "1.0",
        "SignatureNonce": "NwDAxvLU6tFE0DVb",
        "TimeStamp": "2012-12-26T10:33:56Z",
        "RegionId": "region1",
        "Action": "DescribeRegions",
        "Format": "XML"}
KEY_ID = 'testid'
KEY = 'testsecret'
SIGNATURE = 'SDFQNvyH5rtkc9T5Fwo8DOjw5hc='
SIGNATURE= "fxGidmIYSsx2AMa8onxuavOijuE="
CANONICALIZE_STR = 'config%3Dformat%3Ajson%2Cstart%3A0%2Chit%3A20%26%26query%3' \
                   'A%27%E7%9A%84%27'
CANONICALIZED_STR = 'config%253Dformat%253Ajson%252Cstart%253A0%252Chit%253' \
                    'A20%2526%2526query%253A%2527%25E7%259A%2584%2527'

class TokenTest(TestCase):

    def test_canonicalize(self):
        encoded_str = prepare_url.canonicalize(CANONICALIZE_STR)
        self.assertEqual(CANONICALIZED_STR, encoded_str)

    def test_get_token(self):
        signature = prepare_url.get_signature('GET', BODY, KEY)
        self.assertEqual(SIGNATURE, signature)

    def test_get_signed_url(self):
        pass

    def test_get_common_params(self):
        pass
