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
from src.codegenlib.enums import MUSTACHE
from src.codegenlib.templateStreaming import TemplateStreaming
from src.codegenlib.templateFile import TemplateFile
from src.codegenlib.templateModule import TemplateModule

fileName = "test.swift"

testManagerClassTF = TemplateFile(
    name="manager_class_mustache",
    dict={"service_name": "OneframeMobile", "request_func": MUSTACHE.PARENT},
    output_file="Manager.swift"
)
testGetRequestFuncTF = TemplateFile(
    name="request_get_func_mustache",
    dict={"result_model_name": "String","function_name": "getTest", "query_path" : '"api/getTest?name=query"', "func_param" : "query:String, "},
    output_file=None,
    is_child_template=True,
    parent_mustache="request_func"
)
testPostRequestFuncTF = TemplateFile(
    name="request_post_func_mustache",
    dict={"result_model_name": "UserModel", "function_name": "login", "query_path" : '"api/login"', "func_param" : ""},
    output_file=None,
    is_child_template=True,
    parent_mustache="request_func"
)
testManagerClassTF.childTemplateFiles.append(testGetRequestFuncTF)
testManagerClassTF.childTemplateFiles.append(testPostRequestFuncTF)

testModule = TemplateModule(
    name="networking-swagger-swift",
    templates_files=[testManagerClassTF]
)

tStreaming = TemplateStreaming(
    template_module = testModule
)
tStreaming.execute()
'''
findParentFilter = lambda x: x[1] == MUSTACHE.PARENT
output = filter(findParentFilter,testManagerClassTF.dict.items())
print(len(output) > 0 if True else False)
'''
# print(testManagerClassTF.dict["request_func"] == MUSTACHE.PARENT)
# print(testManagerClassTF.dict.items()[0][0])
# print(testManagerClassTF.dict.get("request_func")=="PARENT")
