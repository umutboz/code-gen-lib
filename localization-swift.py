#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# localization-swfit .py
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################

# Built-in/Generic Imports
import sys
import os

# Own modules
from lib.environment import Environment
Environment.Shared().online()
from lib.enums import MUSTACHE
from lib.enums import CODING
from lib.templateFile import TemplateFile
from lib.templateModule import TemplateModule
from templateStreaming import TemplateStreaming
from lib.fileOperation import FileOperation
from lib.log import Log


# for localization import
from os.path import dirname, join, abspath,sys
module = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules/localization-swift'))
sys.path.append(module)
from localizable import Localizable
from localizable import LocalizableCodeGen

'''
# START - written for lib module
import sys
import os
from os.path import dirname, join, abspath
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
lib_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib'))
sys.path.append(root_dir)
sys.path.append(lib_dir)
# END - written for lib module
'''

struct_file_tf = TemplateFile(
    name = "localization_struct_file_mustache",
    dict = {},
    output_file="Localization.swift"
)
#inline_field
child_inline_struct_field_tf = TemplateFile(
    name = "localization_struct_field_mustache",
    dict = {"field_name":"title", "localization_string_key": "Pages.UI.title"},
    parent_mustache = "extension_child_add",
    is_child_template=True,
    output_file = None
)
#inline ui_struct
child_inline_ui_struct_tf = TemplateFile(
    name = "localization_child_inline_struct_extension_mustache",
    dict = {"extension_child_struct_name":"UI", "extension_child_add" : MUSTACHE.PARENT},
    parent_mustache = "extension_child_add",
    is_child_template=True,
    output_file = None,
    child_template_files = [child_inline_struct_field_tf]
)

#inline Appointment_struct
child_inline_appointment_struct_tf = TemplateFile(
    name = "localization_child_inline_struct_extension_mustache",
    dict = {"extension_child_struct_name":"Appointment", "extension_child_add" : MUSTACHE.PARENT},
    parent_mustache = "extension_parent_add",
    is_child_template=True,
    output_file = None,
    child_template_files = [child_inline_ui_struct_tf]
)


parent_page_struct_file = TemplateFile(
    name = "localization_parent_struct_extension_mustache",
    dict = {"extension_parent_struct_name":"Page", "extension_parent_add" : MUSTACHE.PARENT},
    output_file="Localization-Pages+Extensions.swift",
    child_template_files = [child_inline_appointment_struct_tf]
)

localizationModule = TemplateModule(
    name = "localization-swift",
    templates_files = [struct_file_tf,parent_page_struct_file]
)
localizationModule.outputDirectory = "localization"
localizationModule.isAppendOutputPath = True

tStreaming = TemplateStreaming(
    template_module = localizationModule
)

def checkStringFileExtension(string_file):
    result = False
    if string_file.lower().endswith('.strings'):
        result = True
    else :
        Log.e("** must be localizable string file ! **")
        Log.w(string_file)
    return result

def checkStringFileExists(string_file):
    result = False
    if FileOperation().isExist(string_file):
        result = True
    else :
        Log.e("** localizable string file not found **")
        Log.w(string_file)
    return result

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False
#tStreaming.execute()

# -localizable-string-file -params "-p/-fp/--info"
if len(sys.argv) >= 3:
    Environment.Shared().online()
    op = FileOperation()
    is_okay_string_file = False
    params = str(sys.argv[1])
    localizable_string_file_path_param = str(sys.argv[2])
    localizable_string_file_path = ""

    if params == "-p":
        path_name = os.getcwd()
        localizable_string_file_path = path_name + CODING.SLASH + localizable_string_file_path_param
        #print(localizable_string_file_path)
        if checkStringFileExtension(string_file=localizable_string_file_path) and checkStringFileExists(localizable_string_file_path):
            is_okay_string_file = True
    
    elif params == "-fp":
        localizable_string_file_path = localizable_string_file_path_param
        #print(localizable_string_file_path)
        if checkStringFileExtension(string_file=localizable_string_file_path) and checkStringFileExists(localizable_string_file_path):
            is_okay_string_file = True
    
    if is_okay_string_file:
        op = FileOperation()
        localizable_string_file_content = op.readContent(localizable_string_file_path)
        #print(localizable_string_file_content)

        # load localizable content
        parsed_data = []
        for line in localizable_string_file_content.splitlines():
            if "=" in line:
                first_split = str(line).split('"')
                dot_split = str(first_split[1]).split(".")
                localizable = Localizable(key = str(first_split[1]), data = dot_split, parent = dot_split[0])
                parsed_data.append(localizable)
                #print(localizable.split)
                #print(localizable.childs)

        localizables = []
        for parsed in parsed_data:
            #print(data.data)
            # for each split member
            if len(localizables) == 0:
                localizable = LocalizableCodeGen(key = parsed.data[0])
                localizables.append(localizable)
            else:
                if contains(localizables, lambda x: x.key == parsed.data[0]):
                    continue
                else:
                    localizable = LocalizableCodeGen(key = parsed.data[0])
                    localizables.append(localizable)
                    

           
        
        for loc in localizables:
            print(loc)
        '''
        for loc in localizables:
            print(loc)
        for localize in parsed_data:
            localizable = LocalizableCodeGen(key = localizable.key)
            result = False
            if len(localizables) == 0:
                localizables.append(localizable)
            else:
                for obj in localizables:
                    if obj.key <> localize.data[0]:
                        localizables.append(localizable)  

            
            if localize.data[0] <>  
            for obj in localize.data:    
                localizable = Localizable(key = localizable.key, is_parent parent = dot_split[0])
        '''
        #print(localizables)


        
        
        
        



else:
    if len(sys.argv) >= 2:
        params = str(sys.argv[1])
        if params == "--info":
            Log.i("you can string file with under folder path -p")
            Log.w("-p /string-file-path")
            Log.i("you can string file with full path -fp")
            Log.w("-fp /Users/***/Desktop/..")

        else:
            Log.e("must be use min. 2 parameters ")
            Log.i("or u can use params --info")
    else:
        Log.e("must be use min. 2 parameters ")
        Log.i("or u can use params --info")





'''
findParentFilter = lambda x: x[1] == MUSTACHE.PARENT
output = filter(findParentFilter,testManagerClassTF.dict.items())
print(len(output) > 0 if True else False)
'''
# print(testManagerClassTF.dict["request_func"] == MUSTACHE.PARENT)
# print(testManagerClassTF.dict.items()[0][0])
# print(testManagerClassTF.dict.get("request_func")=="PARENT")
