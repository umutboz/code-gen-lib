#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## test
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################
from enums import MessageType
from enums import CodeLine
from log import Log
from environment import Environment
from httpOperation3 import HttpOperation3

MESSAGE = MessageType()

CODE = CodeLine()

#close log
Environment.Shared().online()

url = "https://petstore.swagger.io/v2/swagger.json"

op = HttpOperation3()
jsonData = op.request(url=url).jsonParse()

op2 = HttpOperation3(url=url)
jsonData = op2.request().jsonParse()


op3 = HttpOperation3()
print(op3.fetch(url=url))

print(jsonData["swagger"])