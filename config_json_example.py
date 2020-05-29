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
from lib.fileOperation import FileOperation
from lib.parser import Parser

json_file_name = "sample_config.json"
json_file_path = "/Users/umut/Desktop/Architecture/CodeGenerationCore/" + json_file_name

sampleJsonModule = Parser.jsonToTemplateModule(jsonFile=json_file_path)
print(sampleJsonModule.templates)
for template in sampleJsonModule.templates:
    print(template.name)
    print(template.dict)
    print(template.isChildTemplate)
    print(template.parentMustache)

tStreaming = TemplateStreaming(
    templateModule = sampleJsonModule
)
tStreaming.execute()







