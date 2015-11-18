# -*- coding:utf-8 -*-
import base64
import hashlib
import hmac
import sys
import time
import urllib
import uuid

TO_SIGN = "GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3D" \
          "XML%26RegionId%3Dregion1%26SignatureMethod%3DHMAC-SHA1%26SignatureN" \
          "once%3DNwDAxvLU6tFE0DVb%26SignatureVersion%3D1.0%26TimeStamp%3D2012" \
          "-12-26T10%253A33%253A56Z%26Version%3D2014-05-26"
TO_SIGE2= "GET&%2F&AccessKeyId%3Dtestid%26SignatureMethod%3DHMAC-SHA1%26Signat" \
          "ureNonce%3D14053016951271226%26SignatureVersion%3D1.0%26Timestamp%3" \
          "D2014-07-14T01%253A34%253A55Z%26Version%3Dv2%26fetch_fields%3Dtitle" \
          "%253Bgmt_modified%26format%3Djson%26index_name%3Dut_3885312%26query" \
          "%3Dconfig%253Dformat%253Ajson%252Cstart%253A0%252Chit%253A20%2526%2" \
          "526query%253A%2527%25E7%259A%2584%2527"


def get_signature(method, body, key):
    """
    :param method: request method, eg. "GET"
    :param body: request body dict
    :param key: Access Key Secret
    :return:
    """
    items = body.items()
    items.sort()
    encode_str = ''
    for k, v in items:
        encode_str += canonicalize(k) + '=' + canonicalize(v) + '&'
    encode_str = encode_str[:-1]
    encode_str = canonicalize(encode_str)
    to_sign = method + '&%2F&' + encode_str
    print(to_sign == TO_SIGN)
    key += '&'
    sign = hmac.new('testsecret&', TO_SIGE2, hashlib.sha1).digest()
    signature = base64.encodestring(sign).strip()
    return signature


def canonicalize(encode_str):
    if sys.stdin.encoding is None:
        res = urllib.quote(encode_str.decode('cp936').encode('utf8'), '')
    else:
        res = urllib.quote(encode_str.decode(sys.stdin.encoding).encode('utf8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


def get_signed_url(method, body, key_id, key):
    sign_params = get_common_params(key_id)
    if body:
        sign_params.update(body)
    signature = get_signature(method, sign_params, key)
    sign_params['Signature'] = signature
    url = '/?' + urllib.urlencode(sign_params)
    return url


def get_common_params(key_id):
    params = dict(Version="v2",
                  SignatureMethod="HMAC-SHA1",
                  SignatureVersion="1.0")
    params["Timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    params["SignatureNonce"] = str(uuid.uuid4())
    params["AccessKeyId"] = key_id
    return params


def get_formate_time(now):
    if now:
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
    return ''

# url = get_signed_url('GET', None, key_id, key)
# print(url)