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
    global child_all_content
    global tabCount
    templateModule = None
    isCreationFile = True
    enableLog = False

    def __init__(self, template_module, enable_log=False):
        Base.__init__(self)
        self.httpOp = HttpOperation()
        self.fileOp = FileOperation()
        self.templateModule = template_module
        self.enableLog = enable_log
        self.child_all_content = ""

    def execute(self):
        # search all template files
        # if it has output directory in module, it is generating
        if self.templateModule.templateFiles > 0 and str(self.templateModule.outputDirectory).strip():
            if self.fileOp.isExist(
                    self.templateModule.getOutputDirectoryPath()) and self.templateModule.isAppendOutputPath:
                # TODO : delete folder
                self.fileOp.removeRecursively(folder_path=self.templateModule.getOutputDirectoryPath())
                module_directory_path = self.templateModule.getModuleOutputPath()
                #directory_path = self.fileOp.createNewPath(self.templateModule.outputRootPath,
                #                                           self.templateModule.outputDirectory)
                self.fileOp.createFolderWithoutPath(module_directory_path)

            elif self.fileOp.isExist(
                    self.templateModule.getOutputDirectoryPath()) and not self.templateModule.isAppendOutputPath:
                # folder has already
                Base.log(self,
                         message="This Folder already exists \n" + self.templateModule.getOutputDirectoryPath() +
                                 "\n if you renew re-creation this folder, you should set 'isAppendOutputPath' field "
                                 "to True. But all files will be deleted",
                         message_type=MESSAGE_TYPE.INFO)
            else:
                module_directory_path = self.templateModule.getModuleOutputPath()
                #directory_path = self.fileOp.createNewPath(self.templateModule.outputRootPath + CODING.SLASH + self.getModulePath(),
                #                                           self.templateModule.outputDirectory)
                self.fileOp.createFolderWithoutPath(module_directory_path)

        # initialize template folders
        self.templateModule.initializeTemplateFolder()

        for t_file in self.templateModule.templateFiles:
            # print(t_file.name)
            # do file has own child files?
            if len(t_file.childTemplateFiles) > 0:
                child_loop_all_content = ''
                if t_file.content != '':
                    child_loop_all_content = t_file.content
                else:
                    child_loop_all_content = self.getOwnChildContent(t_file)

                if self.enableLog:
                    print(child_loop_all_content)
                # generate output file
                if str(t_file.outputFile).strip():
                    module_directory_path = self.templateModule.getModuleOutputPath()
                    if self.enableLog:
                        print("output: " + module_directory_path)
                    self.fileOp.create(file_path = module_directory_path + CODING.SLASH + t_file.outputFile, content=child_loop_all_content)

            else :
                replaced_template_content = ''
                if t_file.content != '':
                    replaced_template_content = t_file.content
                else:
                # only work parent files
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

                        t_file.dict[parent[0]] = MUSTACHE.LEFT_BRACKET + MUSTACHE.LEFT_BRACKET + parent[0] + MUSTACHE.RIGHT_BRACKET + MUSTACHE.RIGHT_BRACKET + child_content
                        # print(t_file.dict[parent[0]])
                        # print(t_file.dict)

                    content = self.fileOp.readContent(file_path=self.getModulePath() + CODING.SLASH + t_file.name)
                    replaced_template_content = Parser.string_multiple_replace(content, self.dictToMustache(t_file.dict))
                if self.enableLog:
                    print(replaced_template_content)
                # generate output file
                if str(t_file.outputFile).strip():
                    module_directory_path = self.templateModule.getModuleOutputPath()
                    if self.enableLog:
                        print("output: " + module_directory_path)
                    self.fileOp.create(file_path = module_directory_path + CODING.SLASH + t_file.outputFile, content=replaced_template_content)

    
    # recursive collect child content
    def getOwnChildContent(self, file, previous_content = None):
        if self.enableLog:
            print("t", file.name) 
        content = self.fileContent(file=file)
        if previous_content != None:
            content = previous_content
        else:
            self.child_all_content = ""
            self.tabCount = 0
        
        has_parent_key, parent_objects = self.filterParentNode(file.dict)
        #has parent key
        if has_parent_key:
            child_content = ""
            #has child files
            
            if len(file.childTemplateFiles) > 0:
                for child_file in file.childTemplateFiles:
                    self.tabCount  = self.tabCount  + 1
                    has_did_it_match_parent_mustache = self.didItMatchParentMustache(child_file=child_file,parent_objects=parent_objects)
                    if has_did_it_match_parent_mustache:
                        child_content = self.fileContent(file=child_file)
                        #print(child_content)
                        # tabbed string development
                        tab_string_started_content = ""
                        #print(tab_string_started_content)
                        for i in range(self.tabCount):
                            tab_string_started_content = CODING.TAB + tab_string_started_content 
                        
                        tabbed_child_content = ""
                        for line in child_content.splitlines():
                            tabbed_child_content = tabbed_child_content + tab_string_started_content + line + CODING.NEWLINE

                        # replace parent to child content
                        # replaced_dictionary
                        replaced_dictionary = self.replaceDictToChildContent(parent_dict=file.dict, parent_objects=parent_objects,child_file_content=tabbed_child_content, child_file=child_file)
                        loop_child_content = Parser.string_multiple_replace(content,self.dictToMustache(replaced_dictionary))
                        
                       
                        self.getOwnChildContent(child_file, previous_content = loop_child_content)
            else:
                # only work parent files
                # get filter Node return tuple (x,y)
                has_parent_key, parent_objects = self.filterParentNode(file.dict)
                if has_parent_key:
                    child_content = self.fileContent(file=file)
                    tab_string_started_content = ""
                    #print(tab_string_started_content)
                    for i in range(self.tabCount):
                        tab_string_started_content = CODING.TAB + tab_string_started_content 
                        
                    tabbed_child_content = ""
                    for line in child_content.splitlines():
                        tabbed_child_content = tabbed_child_content + tab_string_started_content + line + CODING.NEWLINE
        
                    replaced_dictionary = self.replaceDictToChildContent(parent_dict=file.dict, parent_objects=parent_objects,child_file_content=tabbed_child_content, child_file=file)
                    loop_child_content = Parser.string_multiple_replace(content,self.dictToMustache(replaced_dictionary))
                    self.child_all_content = loop_child_content
                    return self.child_all_content
        else:
            # fill content
            self.child_all_content = Parser.string_multiple_replace(content,self.dictToMustache(file.dict))
            if self.enableLog:
                print(self.child_all_content)
        
        return self.child_all_content


    def didItMatchParentMustache(self,parent_objects,child_file):
        result = False
        for parent in parent_objects:
            if parent[0] == child_file.parentMustache:
                result = True
        return result

    def replaceDictToChildContent(self,parent_dict,parent_objects,child_file_content,child_file):
        result_dict = parent_dict
        #parent_dict["extension_parent_add"] = child_file_content
        for parent in parent_objects:
            if parent[0] == child_file.parentMustache:
                result_dict[child_file.parentMustache] = child_file_content
        return result_dict  
          
    def getModulePath(self):
        module_path = self.fileOp.createNewPath(
            pathLocate="..",
            folderName="modules/" + self.templateModule.name
        )
        return module_path

    def findTemplateFileByKey(self, mustache_key, is_child):
        found_files = []  # type: List[TemplateFile]
        for tFile in self.templateModule.templateFiles:
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
        if dict is None:
            return False, ""
        filter_output = filter(find_parent_filter, dict.items())
        return (len(filter_output) > 0 if True else False), filter_output


    def dictToMustache(self, dictionary):
        new_dict = dict()
        if dictionary is None:
            return new_dict
        for key in dictionary.keys():
            new_key = MUSTACHE.LEFT_BRACKET + MUSTACHE.LEFT_BRACKET + key + MUSTACHE.RIGHT_BRACKET + MUSTACHE.RIGHT_BRACKET
            new_dict[new_key] = dictionary[key]
        return new_dict
    
    def tabbedContent(self,content, tab_index):
        tab_started_string = ""
        for i in range(tab_index):
            tab_started_string = CODING.TAB + tab_started_string 
                        
        tabbed_content = ""
        for line in content.splitlines():
            tabbed_content = tabbed_content + tab_started_string + line + CODING.NEWLINE
        
        return tabbed_content
        
