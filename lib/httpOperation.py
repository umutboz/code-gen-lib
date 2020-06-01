#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## HttpOperation
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################


# Built-in/Generic Imports
import os
import sys
import json
import urllib2
import ssl

# Own modules
from abstract import Base
from enums import MESSAGETYPE


class HttpOperation(Base):
    _url = ""
    _response = None

    def __init__(self, url=None):
        Base.__init__(self)
        self._url = url

    def url(self):
        if self._url is None or not str(self._url).strip():
            return None
        else:
            return self._url

    def request(self,url=None):
        request_url = None
        if url is not None:
            request_url = str(url)
        else:
            request_url = self.url()
        if request_url is None:
            Base.log(self, message="HttpOperation " + "request : "
                      + " \error : \n url cannot be None", messageType=MESSAGETYPE.ERROR)
            return
        try:
            resp = urllib2.urlopen(request_url)
            dataString = resp.read().decode('utf-8')
            Base.log(self, message="HttpOperation " + "request : " + str(request_url) + " \nresponse : \n" + dataString,
             messageType=MESSAGETYPE.INFO)
            self._response = dataString
            return self
        except urllib2.HTTPError as e:
            Base.log(self, message="HttpOperation " + "request : "
                      + " \HTTPError : \n " + str(e.code), messageType=MESSAGETYPE.ERROR)
        except urllib2.URLError as e:
            Base.log(self, message="HttpOperation " + "request : " + " \\URLError : \n " + str(e.reason), messageType=MESSAGETYPE.ERROR)
        except Exception as e:
            Base.log(self, message="HttpOperation " + "request : "
                      + " \generic exception : \n " + str(e), messageType=MESSAGETYPE.ERROR)
        self._response = None
        return None 

    def jsonParse(self):
        if self._response == None or not str(self._response).strip():
            return None
        jsonData = json.loads(self._response)
        return jsonData

    def fetch(self,url=None):
        request_url = None
        if url != None:
            request_url = str(url)
        else:
            request_url = self.url()
        if request_url == None:
            Base.log(self, message="HttpOperation " + "request : "
                      + " \error : \n url cannot be None", messageType=MESSAGETYPE.ERROR)
            return
        try:
            resp = urllib2.urlopen(request_url)
            dataString = resp.read().decode('utf-8')
            Base.log(self, message="HttpOperation " + "request : " + str(request_url) + " \nresponse : \n" + dataString,
             messageType=MESSAGETYPE.INFO)
            return dataString
        except urllib2.HTTPError as e:
            Base.log(self, message="HttpOperation " + "request : "
                      + " \HTTPError : \n " + str(e.code), messageType=MESSAGETYPE.ERROR)
        except urllib2.URLError as e:
            Base.log(self, message="HttpOperation " + "request : " + " \\URLError : \n " + str(e.reason), messageType=MESSAGETYPE.ERROR)
        except Exception as e:
            Base.log(self, message="HttpOperation " + "request : "
                      + " \generic exception : \n " + str(e), messageType=MESSAGETYPE.ERROR)
        return None
