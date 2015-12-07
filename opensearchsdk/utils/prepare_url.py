# -*- coding:utf-8 -*-
import base64
import hashlib
import hmac
import six
import sys
import time
import uuid
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


def url_quote(encode_str):
    if isinstance(encode_str, six.binary_type):
        if sys.stdin.encoding is None:
            encode_str = encode_str.decode('cp936').encode('utf8')
        else:
            encode_str = encode_str.decode(sys.stdin.encoding).encode('utf8')
    res = quote(encode_str, '~')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    return res


def get_common_params(key_id):
    params = dict(Version="v2",
                  SignatureMethod="HMAC-SHA1",
                  SignatureVersion="1.0",
                  Timestamp=time.strftime(
                      "%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                  SignatureNonce=str(uuid.uuid4()),
                  AccessKeyId=key_id
                  )
    return params


def get_quote_body(body):
    items = body.items()
    items = sorted(items, key=lambda x: x[0])
    encode_str = ''
    for k, v in items:
        encode_str += url_quote(k) + '=' + url_quote(v) + '&'
    encode_str = encode_str[:-1]
    return encode_str


def get_str_to_sign(encode_str, method):
    encode_str = url_quote(encode_str)
    to_sign = method + '&%2F&' + encode_str
    return to_sign


def sign_str(key, str_to_sign):
    key += '&'
    if isinstance(str_to_sign, six.text_type):
        str_to_sign = str_to_sign.encode()
    if isinstance(key, six.text_type):
        key = key.encode()
    sign = hmac.new(key, str_to_sign, hashlib.sha1).digest()
    signature = base64.encodestring(sign).strip()
    return signature


def get_signature(method, body, key, key_id):
    common_params = get_common_params(key_id)
    body.update(common_params)
    quote_body = get_quote_body(body)
    str_to_sign = get_str_to_sign(quote_body, method)
    signature = sign_str(key, str_to_sign)
    return signature
