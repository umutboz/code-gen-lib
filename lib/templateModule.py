#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## TemplateModule
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################

import os, sys
# Owned
from abstract import Base
from enums import MESSAGE_TYPE

pathname = os.path.dirname(sys.argv[0])


class TemplateModule(Base):
    name = ""
    templates = []
    outputRootPath = ""
    outputDirectory = ""
    isAppendOutputPath = False

    def __init__(self, name, templates, output_root_path=pathname):
        Base.__init__(self)
        self.name = name
        self.templates = templates
        self.outputRootPath = output_root_path

    def getOutputDirectoryPath(self):
        return self.outputRootPath + "/" + self.outputDirectory
