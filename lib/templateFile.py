#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## TemplateFile
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################



# Owned
from abstract import Base
from enums import MESSAGETYPE


class TemplateFile(Base):
    name = ""
    outputFile = ""
    dict = None
    isChildTemplate = False
    subTemplates = []
    parentMustache = ""
    def __init__(self, name,dict,outputFile,isChildTemplate=False,parentMustache=""):
        Base.__init__(self)
        self.name = name
        self.dict = dict
        self.outputFile = outputFile
        self.isChildTemplate = isChildTemplate
        self.parentMustache = parentMustache