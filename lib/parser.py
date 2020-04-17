#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## parser
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

#Owned
from abstract import Base
from templateModule import TemplateModule
from templateFile import TemplateFile


class Parser(Base):
    def __init__(self):
        Base.__init__(self)
    
    def jsonToTemplateModule(jsonFile):
        module = TemplateModule(name="",templates=[])

        input_file=open(jsonFile, 'r')
        json_decode=json.load(input_file)
        json_decode_dump = json.dumps(json_decode)
        for tempFile in json_decode["module"]["templateFiles"]:
            name = tempFile["name"]
            dictionary = None
            outputFile = None
            isChildTemplate = False
            parentMustache = ""
            if not (tempFile.get('dict') is None):
                dictionary = eval(json.dumps(tempFile["dict"]))
            if not (tempFile.get('outputFile') is None):
                outputFile = tempFile["outputFile"]
            if not (tempFile.get('isChildTemplate') is None):
                isChildTemplate = tempFile.get('isChildTemplate')
            if not (tempFile.get('parentMustache') is None):
                parentMustache = tempFile.get('parentMustache')
            
            module.templates.append(TemplateFile(
                name=name,
                dict=dictionary,
                outputFile = outputFile,
                isChildTemplate=True,
                parentMustache=parentMustache))
        module.name = json_decode["module"]["name"]    
        return module

    def string_multiple_replace(string, replacement_dict):
        pattern = re.compile("|".join([re.escape(k) for k in sorted(
        replacement_dict, key=len, reverse=True)]), flags=re.DOTALL)
        return pattern.sub(lambda x: replacement_dict[x.group(0)], string)
    
    string_multiple_replace = staticmethod(string_multiple_replace)
    jsonToTemplateModule = staticmethod(jsonToTemplateModule)