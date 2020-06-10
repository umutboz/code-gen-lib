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
from fileOperation import FileOperation
from lib.enums import CODING
from enums import MESSAGE_TYPE

pathname = os.path.dirname(sys.argv[0])


class TemplateModule(Base):
    name = ""
    templateFiles = []
    outputRootPath = ""
    outputDirectory = ""
    isAppendOutputPath = False
    templateFolders = []
    fileOp = FileOperation()

    def __init__(self, name, templates_files, template_folders=[], output_root_path=pathname):
        Base.__init__(self)
        self.name = name
        self.templateFiles = templates_files
        self.outputRootPath = output_root_path
        self.templateFolders = template_folders

    def getOutputDirectoryPath(self):
        return self.outputRootPath + "/" + self.outputDirectory

    def initializeTemplateFolder(self):
        for t_folder in self.templateFolders:
            t_folder_source_full_path = self.outputRootPath + CODING.SLASH + t_folder.source
            t_folder_output_full_path = self.getOutputDirectoryPath() + CODING.SLASH + t_folder.outputPath
            # template folder is exist ?
            if not self.fileOp.isExist(t_folder_output_full_path):
                self.fileOp.createFolderWithoutPath(t_folder_output_full_path)
                print("kol")
            if self.fileOp.isExist(t_folder_source_full_path):
                source_files = self.fileOp.files(t_folder_source_full_path)
                for s_file in source_files:
                    source = t_folder_source_full_path + CODING.SLASH + s_file
                    destination = t_folder_output_full_path + CODING.SLASH + s_file
                    # print("source: ", source)
                    os.system("cp " + source + " " + destination)

            print("target: ", t_folder_output_full_path)
