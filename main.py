#!/usr/bin/env python3
"""
    Signs in, retrieves balance information, returns a json structure.
"""

import http.cookiejar
import json
import urllib
import time
import re
import os
import logging
from pprint import pprint

get_cookie = lambda jar, name: next( item.value for item in jar if item.name == name )

get_internet_remainder = lambda obj: next( item['remainders'] for item in obj['remainders'] if item["name"] == "Интернет по России" )
get_internet_stat = lambda obj: next( {"total": item['totalValue']['value'], "available": item['availableValue']['value']} for item in get_internet_remainder(obj) if item["name"] == "Интернет" )

cookiejar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))

response = opener.open('https://lk.megafon.ru/login/')

cookie_csrf = get_cookie(cookiejar, "CSRF-TOKEN")
logging.warn("CSRF: %s" % cookie_csrf)

params = {
    "CSRF": cookie_csrf,
    "j_username": "",
    "j_password": "",
}

response = opener.open('https://lk.megafon.ru/dologin/', data=urllib.parse.urlencode(params).encode('utf-8'))
response = opener.open('https://lk.megafon.ru/api/lk/balance/get?CSRF=%s' % cookie_csrf)
balance = json.loads(response.read())
logging.warn("Balance: %(balance)s" % balance)

response = opener.open('https://lk.megafon.ru/api/options/remaindersMini?CSRF=%s' % cookie_csrf)
remainders = json.loads(response.read())
logging.warn("Internet: %s" % get_internet_stat(remainders))
