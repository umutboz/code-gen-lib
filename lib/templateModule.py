#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# TemplateModule
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################

import os
import sys
# Owned
from abstract import Base
from enums import MESSAGE_TYPE

pathname = os.path.dirname(sys.argv[0])


class TemplateModule(Base):
    name = ""
    templateFiles = []
    outputRootPath = ""
    outputDirectory = ""
    isAppendOutputPath = False
    templateFolders = []

    def __init__(self, name, templates_files, template_folders=[], output_root_path=pathname):
        Base.__init__(self)
        self.name = name
        self.templateFiles = templates_files
        self.outputRootPath = output_root_path
        self.templateFolders = template_folders
        self.initializeTemplateFolder()

    def getOutputDirectoryPath(self):
        return self.outputRootPath + "/" + self.outputDirectory

    def initializeTemplateFolder(self):
        for t_folder in self.templateFolders:
            t_folder_output_full_path = self.getOutputDirectoryPath() + "/" + t_folder.outputPath
            t_folder_source_full_path = self.getOutputDirectoryPath() + "/" + t_folder.source
            print(t_folder_output_full_path)
            print(t_folder_source_full_path)
