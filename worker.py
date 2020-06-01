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

# Built-in/Generic Imports
import os
import sys
import numpy as np

# Own modules

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

#print(type(Environment.Shared().online()))

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

#default path 
#/Users/umut/Desktop/Architecture/CodeGenerationCore/lib

#print(op.aboveNewPath("test"))
#print(op.belowNewPath("test"))

#print(op.createNewPath(pathLocate="../..",folderName="newPath"))
#print(os.getcwd())

#print(os.path.dirname( __file__ ))

'''
a = [[1,2], [2,1]]
b = [[4,1], [2,2]]

dot  = np.dot(a,b)

cross  = np.cross(a,b)
print(cross)
'''
'''
def crash_course(param):
    result = 0
    temp = 1
    for i in range(1,param):
        temp = temp * i
        for k in range(i):
            result += temp
    return result

print(crash_course(4))
'''
'''
def y(x):
    global a
    a = 4
    return 0

def f(a):
    a = 3
    print(a)
    return a

a = 5
f(a)
print(a)
y(a)
print(a)
'''
'''
arr = [1.4,3.7,4.8,6.3,99.9]

print(arr.pop(2))
'''
'''
array = np.array([[1,2,3],[4,5,6]])

print(np.transpose(array))
'''
'''
x = np.arange(6).reshape(2,3)
print(x)
print(np.transpose(x).shape)
print(np.ndim(x))
#print(np.transpose(x))
'''
'''

print(np.ndim(np.arange(10)))
print(type(x))
print(x)
print(x.dtype)
y = np.transpose(np.arange(4))
'''

