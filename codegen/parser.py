#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# parser
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################

# Built-in/Generic Imports

import re
import json
import os
import sys

# Owned
from abstract import Base
from templateModule import TemplateModule
from templateFile import TemplateFile
from templateFolder import TemplateFolder


class Parser(Base):
    def __init__(self):
        Base.__init__(self)

    def jsonToTemplateModule(json_file):
        module = TemplateModule(name="", templates_files=[])
        with open(json_file, 'r') as json_file:
            try:
                json_decode=json.load(json_file)
                json_decode_dump = json.dumps(json_decode)
                for tempFile in json_decode["module"]["templateFiles"]:
                    name = str(tempFile["name"])
                    dictionary = None
                    output_file = None
                    is_child_template = False
                    parent_mustache = ""
                    if not (tempFile.get('dict') is None):
                        dictionary = eval(json.dumps(tempFile["dict"]))
                    if not (tempFile.get('outputFile') is None):
                        output_file = str(tempFile["outputFile"])
                    if not (tempFile.get('isChildTemplate') is None):
                        is_child_template = tempFile.get('isChildTemplate')
                    if not (tempFile.get('parentMustache') is None):
                        parent_mustache = str(tempFile.get('parentMustache'))

                    module.templateFiles.append(TemplateFile(
                        name=name,
                        dict=dictionary,
                        output_file=output_file,
                        is_child_template=is_child_template,
                        parent_mustache=parent_mustache))

                # template folder generate
                if not (json_decode.get('module').get('templateFolders') is None):
                    for tempFolder in json_decode["module"]["templateFolders"]:
                        source = ""
                        output_path = ""
                        is_online = False
                        if not (tempFolder.get('source') is None):
                            source = eval(json.dumps(tempFolder["source"]))
                        if not (tempFolder.get('outputPath') is None):
                            output_path = str(tempFolder["outputPath"])
                        if not (tempFolder.get('isOnline') is None):
                            is_online = tempFolder.get('isOnline')

                    module.templateFolders.append(TemplateFolder(
                        source=source,
                        output_path=output_path,
                        is_online=is_online
                    ))

                module.name = str(json_decode["module"]["name"])
            except OSError:
                print ("Could not open/read file:", json_file)
                json_file.seek(0)
        return module

    def string_multiple_replace(string, replacement_dict):
        if len(replacement_dict) == 0:
            return string
        pattern = re.compile("|".join([re.escape(k) for k in sorted(replacement_dict, key=len, reverse=True)]), flags=re.DOTALL)
        return pattern.sub(lambda x: replacement_dict[x.group(0)], string)

    def string_multiple_replace_with_child(string, replacement_dict):
        if len(replacement_dict) == 0:
            return string
        pattern = re.compile("|".join([re.escape(k) for k in sorted(replacement_dict, key=len, reverse=True)]), flags=re.DOTALL)
        return pattern.sub(lambda x: replacement_dict[x.group(0)], string)
    

    string_multiple_replace = staticmethod(string_multiple_replace)
    jsonToTemplateModule = staticmethod(jsonToTemplateModule)
    string_multiple_replace_with_child = staticmethod(string_multiple_replace_with_child)