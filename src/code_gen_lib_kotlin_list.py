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

# example : com.kocsistem.codegendemo City theme1 -o /Users/***/Desktop/kotlin-list-id

# param1 : package
# param2 : name
# param3 : theme -> theme1 - theme2
if len(sys.argv) >= 6 and "theme" in sys.argv[3]:
    params = str(sys.argv[0])
    package = str(sys.argv[1])
    name = str(sys.argv[2])
    theme = str(sys.argv[3])
    output_param = str(sys.argv[3])

    activity_name = name + "Activity"
    activity_layout_name = str(name).lower() + "_activity_layout"
    item_layout_xml = str(name).lower() + "_item_layout"
    adapter_name = name + "Adapter"
    model = str(name).lower()

    activity_TF = None
    adapter_TF = None
    layout_xml_TF = None
    item_layout_xml_TF = None

    if theme == "theme2":
        # theme2
        activity_TF = TemplateFile(
            name="list_activity_theme2_mustache",
            dict={"package_name": package, "activity_name": activity_name,
                  "list_activity_layout_xml_name": activity_layout_name,
                  "adapter_name": adapter_name},
            output_file=activity_name + kotlin_extension
        )
        item_layout_xml = item_layout_xml + "_theme2"
        adapter_TF = TemplateFile(
            name="list_adapter_theme2_mustache",
            dict={"adapter_name": adapter_name, "package_name": package, "list_item_xml_name": item_layout_xml,
                  "model": model},
            output_file=adapter_name + kotlin_extension
        )
        layout_xml_TF = TemplateFile(
            name="list_activity_layout_xml_mustache",
            dict={"activity_name": activity_name, "list_item_xml_name": item_layout_xml},
            output_file=activity_layout_name + xml_extension
        )
        item_layout_xml_TF = TemplateFile(
            name="list_item_xml_theme2_mustache",
            dict={"model": model},
            output_file=item_layout_xml + xml_extension
        )
    elif theme == "theme1":
        activity_TF = TemplateFile(
            name="list_activity_theme1_mustache",
            dict={"package_name": package, "activity_name": activity_name,
                  "list_activity_layout_xml_name": activity_layout_name,
                  "adapter_name": adapter_name},
            output_file=activity_name + kotlin_extension
        )
        item_layout_xml = item_layout_xml + "_theme1"
        adapter_TF = TemplateFile(
            name="list_adapter_theme1_mustache",
            dict={"adapter_name": adapter_name, "package_name": package, "list_item_xml_name": item_layout_xml},
            output_file=adapter_name + kotlin_extension
        )
        layout_xml_TF = TemplateFile(
            name="list_activity_layout_xml_mustache",
            dict={"activity_name": activity_name, "list_item_xml_name": item_layout_xml},
            output_file=activity_layout_name + xml_extension
        )
        item_layout_xml_TF = TemplateFile(
            name="list_item_xml_theme1_mustache",
            dict={},
            output_file=item_layout_xml + xml_extension
        )

    # modules/android-kotlin-list
    listModule = TemplateModule(
        name="android-kotlin-list",
        mustache_folder="modules",
        templates_files=[activity_TF, layout_xml_TF, adapter_TF, item_layout_xml_TF]
    )
    listModule.isGenerateOutPutFullPath = True
    listModule.outputDirectory = sys.argv[5]
    listModule.isAppendOutputPath = True
    tStreaming = TemplateStreaming(
        template_module=listModule
    )
    tStreaming.onlineMustache = False
    tStreaming.execute()
else:
    # python main.py com.mypackage.app List
    Log.e("must be use min. 4 parameters ")
    Log.i("First param is :  package id")
    Log.i("Second param is :  Naming")
    Log.i("third param :  theme1 or theme2")
    Log.i("fifth param is with -o :  output path folder")
    if len(sys.argv) >= 4:
        if sys.argv[4] != "-o":
            Log.e("must be use -o param due to output path")

