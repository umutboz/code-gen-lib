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
import shutil

# Own modules
from codegenlib.abstract import Base
from codegenlib.enums import CODING
from codegenlib.enums import MESSAGE_TYPE


class FileOperation(Base):
    _path = ""

    def __init__(self, path=None):
        Base.__init__(self)
        self._path = path

    def getPath(self):
        # path has not chars and is none
        if self._path is None or not str(self._path).strip():
            return os.getcwd()
        else:
            return self._path

    def create(self, file_path, content):
        try:
            file_path = open(file_path, "w")
            file_path.write(content)
            file_path.close()
            Base.log(self, message="FileOperation " + "create : " + str(file_path) + " \ncontent : \n" + content,
                     message_type=MESSAGE_TYPE.INFO)
        except OSError as e:
            Base.log(self, message="FileOperation " + "create : "
                                   + " \error : \n" + str(e), message_type=MESSAGE_TYPE.ERROR)

    def createFile(self, file_name, content):
        file_path = self.getPath() + CODING.SLASH + file_name
        try:
            file_path = open(file_path, "w")
            file_path.write(content)
            file_path.close()
            Base.log(self, message="FileOperation " + "createFile : " +
                                   str(file_path) + " \ncontent : \n" + content, message_type=MESSAGE_TYPE.INFO)
        except OSError as e:
            Base.log(self, message="FileOperation " + "createFile : "
                                   + " \error : \n" + str(e), message_type=MESSAGE_TYPE.ERROR)

    def createFolder(self, folder_name):
        folder_path = self.getPath() + CODING.SLASH + folder_name
        try:
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path)
                Base.log(self, message="FileOperation " + "createFolder : " +
                                       folder_path + "\n", message_type=MESSAGE_TYPE.INFO)
            else:
                Base.log(self, message="FileOperation " + "createFolder : " +
                                       folder_path + "\n already path", message_type=MESSAGE_TYPE.INFO)
        except OSError as e:
            Base.log(self, message="FileOperation " + "createFileWithPath : " + " \error : \n" +
                                   str(e), message_type=MESSAGE_TYPE.ERROR)

    def createFolderWithoutPath(self, folder_name):
        folder_path = folder_name
        try:
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path)
                Base.log(self, message="FileOperation " + "createFolder : " +
                                       folder_path + "\n", message_type=MESSAGE_TYPE.INFO)
            else:
                Base.log(self, message="FileOperation " + "createFolder : " +
                                       folder_path + "\n already path", message_type=MESSAGE_TYPE.INFO)
        except OSError as e:
            Base.log(self, message="FileOperation " + "createFileWithPath : " + " \error : \n" +
                                   str(e), message_type=MESSAGE_TYPE.ERROR)

    def appendFile(self, file_name, content, is_truncate=False):
        file_path = self.getPath() + CODING.SLASH + file_name
        try:
            with open(file_path, "a+") as f:
                # f.seek(0)
                if is_truncate:
                    f.truncate()
                f.write(content)
                f.close()
                Base.log(self, message="FileOperation " + "appendFile : " +
                                       file_path + "\n", message_type=MESSAGE_TYPE.INFO)
        except OSError as e:
            Base.log(self, message="FileOperation " + "appendFile : \error : \n" +
                                   str(e), message_type=MESSAGE_TYPE.ERROR)

    # has path valid and exist return true
    def isExist(self, path):
        if os.path.exists(path):
            return True
        else:
            return False

    # for content of file with filePath
    def readContent(self, file_path):
        global content
        if self.isExist(file_path):
            with open(file_path, "r") as data:
                content = data.read()
            return content
        else:
            Base.log(self, message="FileOperation " + "readContent : " + file_path +
                                   "\n has not found file", message_type=MESSAGE_TYPE.INFO)
            return ""

    # for content of file with fileName
    def getFileContent(self, file_name):
        file_path = self.getPath() + CODING.SLASH + file_name
        return self.readContent(filePath=file_path)

    # for remove file with filePath
    def remove(self, file_path):
        if self.isExist(file_path):
            os.remove(file_path)
            Base.log(self, message="FileOperation " + "remove : " + file_path +
                                   "\n file was removed", message_type=MESSAGE_TYPE.INFO)
        else:
            Base.log(self, message="FileOperation " + "remove : " + file_path +
                                   "\n has not found file", message_type=MESSAGE_TYPE.INFO)
            return ""

    def removeRecursively(self, folder_path):
        if self.isExist(folder_path):
            shutil.rmtree(folder_path)

    # for remove file with fileName
    def removeFile(self, file_name):
        file_path = self.getPath() + CODING.SLASH + file_name
        self.remove(file_path)

    def files(self, directory_path):
        if self.isExist(path=directory_path):
            return os.listdir(directory_path)
        else:
            return []

    def aboveNewPath(self, path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', path))

    def belowNewPath(self, path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '', path))

    def createNewPath(self, pathLocate, folderName):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), pathLocate, folderName))
