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
from codegenlib.abstract import Base
from codegenlib.fileOperation import FileOperation
from codegenlib.enums import CODING
from codegenlib.enums import MESSAGE_TYPE

pathname = os.getcwd()

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
        return self.outputRootPath + CODING.SLASH + self.getModulePath() + CODING.SLASH + self.outputDirectory
    
    def getModulePath(self):
        module_path = self.fileOp.createNewPath(
            pathLocate="..",
            folderName="modules/" + self.name
        )
        module_path = "modules/" + self.name
        return module_path

    def getModuleOutputPath(self):
        module_directory_path = self.outputRootPath + CODING.SLASH + "modules" +  CODING.SLASH  + self.name + CODING.SLASH  + self.outputDirectory
        return module_directory_path
        
    def initializeTemplateFolder(self):
        for t_folder in self.templateFolders:
            t_folder_source_full_path = self.outputRootPath + CODING.SLASH + t_folder.source
            t_folder_output_full_path = self.getOutputDirectoryPath() + CODING.SLASH + t_folder.outputPath
            # template folder is exist ?
            if not self.fileOp.isExist(t_folder_output_full_path):
                self.fileOp.createFolderWithoutPath(t_folder_output_full_path)
            # source template is online ?
            if t_folder.isOnline:
                root_github_module_url = "https://raw.githubusercontent.com/umutboz/code-gen-lib/master/modules" + CODING.SLASH + self.name
                # https://raw.githubusercontent.com/umutboz/code-gen-lib/master/modules/oneframe-ios-api-manager/models/ApplicationRole.swift
                t_folder_source_full_path =  root_github_module_url
                print(root_github_module_url)
            else:
                if self.fileOp.isExist(t_folder_source_full_path):
                    source_files = self.fileOp.files(t_folder_source_full_path)
                    for s_file in source_files:
                        source = t_folder_source_full_path + CODING.SLASH + s_file
                        destination = t_folder_output_full_path + CODING.SLASH + s_file
                        # print("source: ", source)
                        os.system("cp " + source + " " + destination)

            print("target: ", t_folder_output_full_path)
