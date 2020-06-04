#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## test
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################



from lib.enums import MessageType

from lib.enums import CodeLine
from lib.log import Log
from lib.fileOperation import FileOperation
from lib.environment import Environment


MESSAGE = MessageType()

CODE = CodeLine()

path = "/"
fileName = "test.swift"
#eger bir path belirlenmis ise
#op = FileOperation("/Users/umut/Desktop/Architecture/CodeGenerationCore/lib")
#run path kullanılmak isteniyorsa
op = FileOperation()

#get content of file with relative Path
#print(op.getFileContentWithPath(filePath=path + CODE.SLASH + fileName))

#get content of file with fileName on the current path
#print(op.getFileContent(fileName="lib/test.py"))

#get content of file with fileName on the relative path
#print(op.getFileContent(filePath = "/lib/test.py"))

#create file with relative path 
#op.create(filePath=filePath,content="hello")

#path param ile verilen path üzerine dosya oluşturulur.
#op.createFile(path="lib",fileName="test.swift",content="hello")


#init de verilen default path üzerine klasör oluşturulur.
#op.createFolder(folderName="hello/1")

#path is valid
#print(op.isExist("/Users/umut/Desktop/Architecture/CodeGenerationCore/lib"))

#append file add content
#op.appendFile(fileName="test.swift",content="\nworld")


#loglar kapali artik
#Environment.Shared().online()

print(type(Environment.Shared().online()))

#remove file
#op.removeFile(fileName=fileName)
#op.createFile(fileName=fileName, content="hello")


#print(MESSAGE.ERROR)
#print(DEV_ENV.LOCAL)
#print(CODE.SLASH)


#log samples
#Log.i(message=MESSAGE.INFO)
#Log.s(MESSAGE.SUCCESS)
#Log.e(MESSAGE.ERROR)
