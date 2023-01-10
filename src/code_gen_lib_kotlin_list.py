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

import sys


# Built-in/Generic Imports
from codegenlib.templateStreaming import TemplateStreaming
from codegenlib.templateFile import TemplateFile
from codegenlib.templateModule import TemplateModule
from codegenlib.log import Log
from codegenlib.environment import Environment

package, name = "", ""
kotlin_extension = ".kt"
xml_extension = ".xml"

# should be name property in root mustache_folder property directory
# all mustache files belonging to for this module

# param1 : package
# param2 : name
if len(sys.argv) >= 2:
    params = str(sys.argv[0])
    package = str(sys.argv[1])
    name = str(sys.argv[2])

    activity_name = name + "Activity"
    activity_layout_name = str(name).lower() + "_activity_layout"
    item_layout_xml = str(name).lower() + "_item_layout"
    adapter_name = name + "Adapter"

    activity_TF = TemplateFile(
        name="list_activity_mustache",
        dict={"package_name": package, "activity_name": activity_name,
              "list_activity_layout_xml_name": activity_layout_name},
        output_file=activity_name + kotlin_extension
    )
    layout_xml_TF = TemplateFile(
        name="list_activity_layout_xml_mustache",
        dict={"activity_name": activity_name},
        output_file=activity_layout_name + xml_extension
    )
    adapter_TF = TemplateFile(
        name="list_adapter_mustache",
        dict={"adapter_name": adapter_name, "package_name": package, "list_item_xml_name": item_layout_xml},
        output_file=adapter_name + kotlin_extension
    )

    item_layout_xml_TF = TemplateFile(
        name="list_item_xml_mustache",
        dict={},
        output_file=item_layout_xml + xml_extension
    )

    # modules/android-kotlin-list
    listModule = TemplateModule(
        name="android-kotlin-list",
        mustache_folder="modules",
        templates_files=[activity_TF, layout_xml_TF, adapter_TF, item_layout_xml_TF]
    )
    listModule.outputDirectory = "output"
    listModule.isAppendOutputPath = True
    tStreaming = TemplateStreaming(
        template_module=listModule
    )
    tStreaming.onlineMustache = True
    tStreaming.execute()
else:
    # python main.py com.mypackage.app List
    Log.e("must be use min. 2 parameters ")
    Log.i("or u can use params --info")

#https://raw.githubusercontent.com/umutboz/code-gen-lib/master/modules/android-kotlin-list/list_item_xml_mustache

