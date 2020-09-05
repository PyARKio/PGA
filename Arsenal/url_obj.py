# -- coding: utf-8 --
from __future__ import unicode_literals
from __future__ import annotations
from Arsenal.log_settings import log
import requests
import datetime


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class URL(object):
    def __init__(self, set_url, post=False):
        self.__post = post
        self.__url = set_url
        self.__error = {}  # {date: err}
        self.__data = {}

    def __str__(self):
        return 'object for {}'.format(self.__url)

    @property
    def errors(self):
        return self.__error

    @property
    def data(self):
        return self.__data

    def status(self, data=False):
        if self.__post:
            try:
                response = requests.post(self.__url, data=data)
            except Exception as err:
                log.error(err)
                self.__error[datetime.datetime.now()] = err
                return False
            else:
                self.__data = {'headers': response.headers, 'status_code': response.status_code, 'url': response.url,
                               'reason': response.reason, 'request': response.request, 'content': response.content,
                               'json': response.json, 'history': response.history, 'cookies': response.cookies,
                               'elapsed': response.elapsed, 'links': response.links, 'raw': response.raw}
                return True
        else:
            try:
                response = requests.get(self.__url)
            except Exception as err:
                log.error(err)
                self.__error[datetime.datetime.now()] = err
                return False
            else:
                self.__data = {'headers': response.headers, 'status_code': response.status_code, 'url': response.url,
                               'reason': response.reason, 'request': response.request, 'content': response.content,
                               'json': response.json, 'history': response.history, 'cookies': response.cookies,
                               'elapsed': response.elapsed, 'links': response.links, 'raw': response.raw}
                return True


if __name__ == '__main__':
    urls = ['https://google.com', 'https://google.coms']
    for url in urls:
        url_obj = URL(url)
        log.debug(url_obj)
        if url_obj.status():
            for i, v in url_obj.data.items():
                log.debug(i)
                log.debug(v)
        else:
            for i, v in url_obj.errors.items():
                log.debug(i)
                log.debug(v)



