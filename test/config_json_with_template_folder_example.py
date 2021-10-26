#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# replace_module_test.py
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

from lib.parser import Parser
# Own modules
from templateStreaming import TemplateStreaming

pathname = os.path.dirname(sys.argv[0])
# current path
json_file_name = "sample_config_with_template_folder.json"
json_file_path = pathname + "/" + json_file_name

sampleJsonModule = Parser.jsonToTemplateModule(json_file=json_file_path)
sampleJsonModule.outputDirectory = "oneframe-api-ios"
sampleJsonModule.isAppendOutputPath = True

print(sampleJsonModule.getOutputDirectoryPath())

tStreaming = TemplateStreaming(
    template_module=sampleJsonModule,
    enable_log=False,
)
tStreaming.execute()
