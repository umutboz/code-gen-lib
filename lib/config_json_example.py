#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## replace_module_test.py
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
import re
import json

# Own modules
from enums import MUSTACHE
from log import Log
from environment import Environment
from templateStreaming import TemplateStreaming
from templateFile import TemplateFile
from templateModule import TemplateModule
from parser import Parser

sampleJsonModule = Parser.jsonToTemplateModule("sample_config.json")
print(sampleJsonModule.templates)
for template in sampleJsonModule.templates:
    print(template.name)
    print(template.dict)
    print(template.isChildTemplate)
    print(template.parentMustache)
'''
tStreaming = TemplateStreaming(
    templateModule = sampleJsonModule
)
#tStreaming.execute()
'''






