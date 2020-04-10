#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## FileOperation
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

# Own modules
from abstract import Base
from enums import CODING
from enums import MESSAGETYPE

class FileOperation(Base):
    _path = ""
    def __init__(self, path=None):
        Base.__init__(self)
        self._path = path

    def getPath(self):
        #path has not chars and is none
        if self._path == None or not str(self._path).strip():
            return os.getcwd()
        else:
            return self._path

    def create(self,filePath, content):
        try:
            filePath = open(filePath, "w")
            filePath.write(content)
            filePath.close()
            Base.log(self, message="FileOperation " + "create : " + str(filePath) + " \ncontent : \n" + content,
             messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self,message = "FileOperation " + "create : " 
            + " \error : \n" + str(e), messageType=MESSAGETYPE.ERROR)

    def createFile(self,fileName, content):
        filePath = self.getPath() + CODING.SLASH + fileName
        try:
            filePath = open(filePath, "w")
            filePath.write(content)
            filePath.close()
            Base.log(self, message="FileOperation " + "createFile : " +
            str(filePath) + " \ncontent : \n" + content, messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self, message="FileOperation " + "createFile : "
            + " \error : \n" + str(e), messageType=MESSAGETYPE.ERROR)

    def createFolder(self, folderName):
        folderPath = self.getPath() + CODING.SLASH + folderName
        try:
            if not os.path.isdir(folderPath):
                os.makedirs(folderPath)
                Base.log(self,message = "FileOperation " + "createFolder : " + 
                folderPath + "\n", messageType=MESSAGETYPE.INFO)
            else :
                Base.log(self,message = "FileOperation " + "createFolder : " + 
                folderPath + "\n already path", messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self,message = "FileOperation " + "createFileWithPath : " + " \error : \n" + 
            str(e), messageType=MESSAGETYPE.ERROR)

    def appendFile(self, fileName, content,isTruncate=False):
        filePath = self.getPath() + CODING.SLASH + fileName
        try:
            with open(filePath, "a+") as f:
            # f.seek(0)
                if isTruncate:
                    f.truncate()
                f.write(content)
                f.close()
                Base.log(self,message = "FileOperation " + "appendFile : " + 
                    filePath + "\n", messageType=MESSAGETYPE.INFO)
        except OSError as e:
            Base.log(self,message = "FileOperation " + "appendFile : " + " \error : \n" + 
            str(e), messageType=MESSAGETYPE.ERROR)
    
    #has path valid and exist return true
    def isExist(self,path):
        if os.path.exists(path):
            return True
        else:
            return False

    #for content of file with filePath
    def readContent(self,filePath):
        global content
        if self.isExist(filePath):
            with open(filePath, "r") as data:
                content = data.read()
            return content
        else:
            Base.log(self, message="FileOperation " + "readContent : " + filePath +
                     "\n has not found file", messageType=MESSAGETYPE.INFO)
            return ""
    
    #for content of file with fileName
    def getFileContent(self,fileName):
        filePath = self.getPath() + CODING.SLASH + fileName
        return self.readContent(filePath=filePath)
    
    #for remove file with filePath
    def remove(self, filePath):
        if self.isExist(filePath):
            os.remove(filePath)
            Base.log(self, message="FileOperation " + "remove : " + filePath +
                     "\n file was removed", messageType=MESSAGETYPE.INFO)
        else:
            Base.log(self, message="FileOperation " + "remove : " + filePath +
                     "\n has not found file", messageType=MESSAGETYPE.INFO)
            return ""

    #for remove file with fileName
    def removeFile(self, fileName):
        filePath = self.getPath() + CODING.SLASH + fileName
        self.remove(filePath)

    def aboveNewPath(self,path):
        return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', path))
    
    def belowNewPath(self,path):
        return os.path.abspath(os.path.join(os.path.dirname( __file__ ), '', path))
    
    def createNewPath(self,pathLocate,folderName):
        return os.path.abspath(os.path.join(os.path.dirname( __file__ ), pathLocate, folderName))
    

