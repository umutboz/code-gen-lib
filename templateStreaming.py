#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# TemplateStreaming
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################


# Built-in/Generic Imports
import os
import sys
import re

# Own modules

from lib.abstract import Base
from lib.enums import MessageType
from lib.enums import CODING
from lib.enums import MUSTACHE
from lib.fileOperation import FileOperation
from lib.templateFile import TemplateFile
from lib.templateModule import TemplateModule
from lib.httpOperation import HttpOperation
from lib.parser import Parser
from lib.enums import MESSAGE_TYPE


class TemplateStreaming(Base):
    global httpOp
    global fileOp
    templateModule = None
    isCreationFile = True
    enableLog = False

    def __init__(self, template_module, enable_log=False):
        Base.__init__(self)
        self.httpOp = HttpOperation()
        self.fileOp = FileOperation()
        self.templateModule = template_module
        self.enableLog = enable_log

    def execute(self):
        # search all template files
        # if it has output directory in module, it is generating
        if self.templateModule.templates > 0 and str(self.templateModule.outputDirectory).strip():
            if self.fileOp.isExist(
                    self.templateModule.getOutputDirectoryPath()) and self.templateModule.isAppendOutputPath:
                # TODO : delete folder
                self.fileOp.removeRecursively(folder_path=self.templateModule.getOutputDirectoryPath())
                directory_path = self.fileOp.createNewPath(self.templateModule.outputRootPath,
                                                           self.templateModule.outputDirectory)
                self.fileOp.createFolderWithoutPath(directory_path)

            elif self.fileOp.isExist(
                    self.templateModule.getOutputDirectoryPath()) and not self.templateModule.isAppendOutputPath:
                # folder has already
                Base.log(self,
                         message="This Folder already exists \n" + self.templateModule.getOutputDirectoryPath() +
                                 "\n if you renew re-creation this folder, you should set 'isAppendOutputPath' field "
                                 "to True. But all files will be deleted",
                         message_type=MESSAGE_TYPE.INFO)
            else:
                directory_path = self.fileOp.createNewPath(self.templateModule.outputRootPath,
                                                           self.templateModule.outputDirectory)
                self.fileOp.createFolderWithoutPath(directory_path)

        for t_file in self.templateModule.templates:
            # print(t_file.name)
            # only work parent files
            if not t_file.isChildTemplate:
                # get filter Node return tuple (x,y)
                has_parent_key, parent_objects = self.filterParentNode(t_file.dict)
                if has_parent_key:
                    # loop parentObject
                    child_content = ""
                    for parent in parent_objects:
                        # findChildFile By ParentObjects
                        founded_files = self.findTemplateFileByKey(mustache_key=parent[0], is_child=True)
                        # find hasChild File
                        if len(founded_files) > 0:
                            for child_file in founded_files:
                                # get Child Content
                                # print(childFile)
                                loop_child_content = self.fileContent(file=child_file)
                                loop_child_content = Parser.string_multiple_replace(loop_child_content,
                                                                                    self.dictToMustache(
                                                                                        child_file.dict))
                                # print(loopChildContent)
                                child_content = child_content + CODING.NEWLINE + loop_child_content

                    t_file.dict[parent[0]] = MUSTACHE.LEFT_BRACKET + MUSTACHE.LEFT_BRACKET + parent[
                        0] + MUSTACHE.RIGHT_BRACKET + MUSTACHE.RIGHT_BRACKET + child_content
                    # print(t_file.dict[parent[0]])
                    # print(t_file.dict)
                content = self.fileOp.readContent(file_path=self.getModulePath() + CODING.SLASH + t_file.name)
                replaced_template_content = Parser.string_multiple_replace(content, self.dictToMustache(t_file.dict))
                if self.enableLog:
                    print(replaced_template_content)

                # generate output file
                if str(t_file.outputFile).strip():
                    self.fileOp.create(file_path=self.templateModule.getOutputDirectoryPath() + CODING.SLASH + t_file.outputFile, content=replaced_template_content)

    def getModulePath(self):
        module_path = self.fileOp.createNewPath(
            pathLocate="..",
            folderName="modules/" + self.templateModule.name
        )
        return module_path

    def findTemplateFileByKey(self, mustache_key, is_child):
        found_files = []  # type: List[TemplateFile]
        for tFile in self.templateModule.templates:
            if tFile.isChildTemplate == is_child and self.findChildMustachFilter(file=tFile, mustache_key=mustache_key):
                found_files.append(tFile)
        return found_files

    def fileContent(self, file):
        content = self.fileOp.readContent(file_path=self.getModulePath() + CODING.SLASH + file.name)
        return content

    def findChildMustachFilter(self, file, mustache_key):
        # print(file.name, mustacheKey)
        if file.parentMustache == mustache_key:
            return True
        else:
            return False

    def findMustacheFilter(self, file, mustache_key):
        # print(file.name, mustacheKey)
        find_mustache_filter = lambda x: x[0] == mustache_key
        filter_output = filter(find_mustache_filter, file.dict.items())
        # print(filter_output)
        return len(filter_output) > 0 if True else False

    def filterParentNode(self, dict):
        find_parent_filter = lambda x: x[1] == MUSTACHE.PARENT
        filter_output = filter(find_parent_filter, dict.items())
        return (len(filter_output) > 0 if True else False), filter_output

    def dictToMustache(self, dictionary):
        new_dict = dict()
        for key in dictionary.keys():
            new_key = MUSTACHE.LEFT_BRACKET + MUSTACHE.LEFT_BRACKET + key + MUSTACHE.RIGHT_BRACKET + MUSTACHE.RIGHT_BRACKET
            new_dict[new_key] = dictionary[key]
        return new_dict
