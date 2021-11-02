#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# Localizable
############################################################
# Author: Umut Boz
# Copyright (c) 2021, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 1.0.0
############################################################

# Owned
import os
import sys

from os.path import dirname,join, abspath,sys
lib_dir_path =  os.path.join(os.path.dirname(__file__), '../../codegen')
lib_dir_module = os.path.abspath(lib_dir_path)
sys.path.insert(0, lib_dir_module) 

from abstract import Base
from enums import MESSAGE_TYPE
from enums import CODING
from enums import MUSTACHE
from parser import Parser


class Localizable(Base):
    key = ""
    data = []
    parent = ""
    childs = []
    lastKey = ""

    def __init__(self, key, data, parent):
        Base.__init__(self)
        self.key = key
        self.data = data
        self.parent = parent
        for word in data:
            if self.parent != word:
                # is last object ?
                if data[len(data)-1] == word:
                    self.lastKey = word
                    self.childs.append(word)
                else:
                    self.childs.append(word)

class LocalizableCodeGen(Base):
    key = ""
    childs = []
    generatedFieldContent = ""
    generatedStructContent = ""
    parent = ""
    parentObject = None
    isLastKey = False
    index = -1
    fullKey = ""
    templateFile = None
    resultContent = ""
    content = ""

    def __init__(self, key):
        Base.__init__(self)
        self.key = key
        results = []

    def __str__(self):
        return self.key

    def get_last_struct_content(self):
        temp_dict = { "{{extension_child_add}}" : self.generatedFieldContent }
        replaced_template_content = Parser.string_multiple_replace(self.generatedStructContent, temp_dict)
        return replaced_template_content

    def get_last_struct_content_by_obj(self,obj):
        temp_dict = { "{{extension_child_add}}" : obj.generatedFieldContent }
        replaced_template_content = Parser.string_multiple_replace(obj.generatedStructContent, temp_dict)
        return replaced_template_content

    def get_last_struct_merge_content(self):
        loop_replaced_template_content = ""

        if len(self.childs) > 0:
            for idx, child in enumerate(self.childs):
                loop_content = self.get_last_struct_content_by_obj(obj=child)
                loop_replaced_template_content += loop_content + CODING.NEWLINE
        else:
            temp_dict = { "{{extension_child_add}}" : self.generatedFieldContent }
            loop_replaced_template_content = Parser.string_multiple_replace(self.generatedStructContent, temp_dict)

        return loop_replaced_template_content

    def dictToMustache(self, dictionary):
        new_dict = dict()
        if dictionary is None:
            return new_dict
        for key in dictionary.keys():
            new_key = MUSTACHE.LEFT_BRACKET + MUSTACHE.LEFT_BRACKET + key + MUSTACHE.RIGHT_BRACKET + MUSTACHE.RIGHT_BRACKET
            new_dict[new_key] = dictionary[key]
        return new_dict            
                
                

       
    

