#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## TemplateStreaming
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

# Own modules
from abstract import Base
from enums import MessageType
from enums import CODING
from enums import MUSTACHE
from fileOperation import FileOperation
from templateFile import TemplateFile
from templateModule import TemplateModule
from httpOperation import HttpOperation
from parser import Parser

class TemplateStreaming(Base):
    global httpOp
    global fileOp
    templateModule = None

    def __init__(self, templateModule):
        Base.__init__(self)
        self.httpOp = HttpOperation()
        self.fileOp = FileOperation()
        self.templateModule = templateModule
    

    def execute(self):
        #search all template files
        for tFile in self.templateModule.templates:
            print(tFile.name)
            #only work parent files
            if tFile.isChildTemplate == False:
                #get filter Node return tupple (x,y)
                hasParentKey, parentObjects = self.filterParentNode(tFile.dict)
                if hasParentKey:
                    #loop parentObject
                    childContent = ""
                    for parent in parentObjects:
                        #findChildFile By ParentObjects
                        foundedFiles = self.findTemplateFileByKey(mustacheKey=parent[0],isChild=True)
                        #find hasChild File
                        if len(foundedFiles) > 0:
                            for childFile in foundedFiles:
                                #get Child Content
                                #print(childFile)
                                loopChildContent = self.fileContent(file=childFile)
                                loopChildContent = Parser.string_multiple_replace(loopChildContent,self.dictToMustache(childFile.dict))
                                #print(loopChildContent)
                                childContent = childContent + CODING.NEWLINE + loopChildContent

                    tFile.dict[parent[0]] = MUSTACHE.LEFT_BRACKET + MUSTACHE.LEFT_BRACKET + parent[0] + MUSTACHE.RIGHT_BRACKET + MUSTACHE.RIGHT_BRACKET + childContent
                    #print(tFile.dict[parent[0]])
                    #print(tFile.dict)
                content = self.fileOp.readContent(filePath= self.getModulePath() + CODING.SLASH + tFile.name)
                print(Parser.string_multiple_replace(content,self.dictToMustache(tFile.dict)))



    def getModulePath(self):
        modulePath = self.fileOp.createNewPath(
            pathLocate = "..",
            folderName = "modules/" + self.templateModule.name
        )
        return modulePath

    def findTemplateFileByKey(self,mustacheKey,isChild):
        foundFiles = []
        for tFile in self.templateModule.templates:
            if tFile.isChildTemplate == isChild and self.findChildMustachFilter(file=tFile,mustacheKey=mustacheKey):
                foundFiles.append(tFile)
        return foundFiles

    def fileContent(self,file):
        content = self.fileOp.readContent(filePath= self.getModulePath() + CODING.SLASH + file.name)
        return content
    
    def findChildMustachFilter(self,file, mustacheKey):
        #print(file.name, mustacheKey)
        if file.parentMustache == mustacheKey:
            return True
        else:
            return False


    def findMustacheFilter(self,file, mustacheKey):
        print(file.name, mustacheKey)
        findMustacheFilter = lambda x: x[0] == mustacheKey
        filterOutput = filter(findMustacheFilter,file.dict.items())
        print(filterOutput)
        return (len(filterOutput) > 0 if True else False)

    def filterParentNode(self,dict):
        findParentFilter = lambda x: x[1] == MUSTACHE.PARENT
        filterOutput = filter(findParentFilter,dict.items())
        return ((len(filterOutput) > 0 if True else False), filterOutput)

    def dictToMustache(self, dictionary):
        newDict = dict()
        for key in dictionary.keys():
            newKey = MUSTACHE.LEFT_BRACKET + MUSTACHE.LEFT_BRACKET + key + MUSTACHE.RIGHT_BRACKET + MUSTACHE.RIGHT_BRACKET
            newDict[newKey] = dictionary[key]
        return newDict