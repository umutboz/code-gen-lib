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

# Own modules
from src.codegenlib.templateStreaming import TemplateStreaming
from src.codegenlib.templateFile import TemplateFile
from src.codegenlib.templateModule import TemplateModule

activity_TF = TemplateFile(
    name="list_activity_mustache",
    dict={"package_name": "com.myapp", "activity_name" : "ListActivity"},
    output_file="list_activity.kt"
)
listModule = TemplateModule(
    name="android-kotlin-list",
    templates_files=[activity_TF],
   
)
listModule.outputDirectory = "android-kotlin-list"

tStreaming = TemplateStreaming(
    template_module = listModule
)
tStreaming.execute()
