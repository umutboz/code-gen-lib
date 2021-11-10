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
from codegenlib.templateStreaming import TemplateStreaming
from codegenlib.templateFile import TemplateFile
from codegenlib.templateModule import TemplateModule

activity_TF = TemplateFile(
    name ="list_activity_mustache",
    dict = {"package_name": "com.myapp", "activity_name" : "ListActivity"},
    output_file="list_activity.kt"
)
# should be name property in root mustache_folder property directory
# all mustache files belonging to for this module
#modules/android-kotlin-list
listModule = TemplateModule(
    name = "android-kotlin-list",
    mustache_folder = "modules",
    templates_files = [activity_TF],
)
listModule.outputDirectory = "output"
listModule.isAppendOutputPath = True
tStreaming = TemplateStreaming(
    template_module = listModule
)
tStreaming.execute()
