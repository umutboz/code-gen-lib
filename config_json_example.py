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
from lib.enums import MUSTACHE
from lib.log import Log
from lib.environment import Environment
from lib.templateStreaming import TemplateStreaming
from lib.templateFile import TemplateFile
from lib.templateModule import TemplateModule
from lib.parser import Parser

json_file_path = os.getcwd() + "/sample_config.json"
if ~os.path.exists(json_file_path):
    print("sada")
sampleJsonModule = Parser.jsonToTemplateModule()
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






