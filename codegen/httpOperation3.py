#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# HttpOperation
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################


# Built-in/Generic Imports
import os
import sys
import json
import urllib3
import ssl

# Own modules
from abstract import Base
from enums import MESSAGE_TYPE


class HttpOperation3(Base):
    _url = ""
    _response = None

    def __init__(self, url=None):
        Base.__init__(self)
        self._url = url

    def url(self):
        if self._url == None or not str(self._url).strip():
            return None
        else:
            return self._url

    def request(self, url=None, http_method="GET"):
        request_url = None
        if url is not None:
            request_url = str(url)
        else:
            request_url = self.url()
        if request_url is None:
            Base.log(self, message="HttpOperation " + "request : "
                                   + " \error : \n url cannot be None", message_type=MESSAGE_TYPE.ERROR)
            return
        try:
            http = urllib3.PoolManager()
            resp = http.request(http_method, request_url)
            data_string = resp.data.decode('utf-8')
            Base.log(self, message="HttpOperation " + "request : " + str(request_url) + " \nresponse : \n" + data_string,
                     message_type=MESSAGE_TYPE.INFO)
            self._response = data_string
            return self
        except urllib3.exceptions.HTTPError as e:
            Base.log(self, message="HttpOperation " + "request : "
                                   + " \HTTPError : \n " + str(e.code), message_type=MESSAGE_TYPE.ERROR)
        except urllib3.exceptions.RequestError as e:
            Base.log(self, message="HttpOperation request : URLError : " + str(e.reason),
                     message_type=MESSAGE_TYPE.ERROR)
        except Exception as e:
            Base.log(self, message="HttpOperation " + "request : "
                                   + " \generic exception : \n " + str(e), message_type=MESSAGE_TYPE.ERROR)
        self._response = None
        return None

    def jsonParse(self):
        if self._response is None or not str(self._response).strip():
            return None
        jsonData = json.loads(self._response)
        return jsonData

    def fetch(self, url=None, httpMethod="GET"):
        request_url = None
        if url is not None:
            request_url = str(url)
        else:
            request_url = self.url()
        if request_url is None:
            Base.log(self, message="HttpOperation " + "request : "
                                   + " \error : \n url cannot be None", message_type=MESSAGE_TYPE.ERROR)
            return
        try:
            http = urllib3.PoolManager()
            resp = http.request(httpMethod, request_url)
            data_string = resp.data.decode('utf-8')
            Base.log(self, message="HttpOperation " + "request : " + str(request_url) + " \nresponse : \n" + data_string,
                     message_type=MESSAGE_TYPE.INFO)
            return data_string
        except urllib3.exceptions.HTTPError as e:
            Base.log(self, message="HttpOperation " + "request : "
                                   + " \HTTPError : \n " + str(e.code), message_type=MESSAGE_TYPE.ERROR)
        except urllib3.exceptions.RequestError as e:
            Base.log(self, message="HttpOperation request : URLError : \n " + str(e.reason),
                     message_type=MESSAGE_TYPE.ERROR)
        except Exception as e:
            Base.log(self, message="HttpOperation " + "request : "
                                   + " \generic exception : \n " + str(e), message_type=MESSAGE_TYPE.ERROR)
        return None
