#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
import re


def emit(url):
    return url


def openurl(url):

    response = urlopen(url)
    if urlopen.getcode() == 200:
        return response.read().encode('utf-8')
    else:
        return None


def findAllHref(htmlString):

    return [url.replace('href="', '').replace('"', '')
            for url in re.findall(r'href=[a-zA-Z0-9"-.:/#\_]*', htmlString)
            if url != 'href=""']


def emitUrls(urlArray):

    for url in urlArray:
        emit(url)
