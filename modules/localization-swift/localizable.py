#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# Localizable
############################################################
# Author: Umut Boz
# Copyright (c) 2021, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 1.0.0
############################################################

# Owned
import os,sys
from os.path import dirname, join, abspath,sys
lib_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib'))

from lib.abstract import Base
from lib.enums import MESSAGE_TYPE
from lib.enums import CODING

class Localizable(Base):
    key = ""
    data = []
    parent = ""
    childs = []
    lastKey = ""

    def __init__(self, key, data, parent):
        Base.__init__(self)
        self.key = key
        self.data = data
        self.parent = parent
        for word in data:
            if self.parent <> word:
                # is last object ?
                if data[len(data)-1] == word:
                    self.lastKey = word
                    self.childs.append(word)
                else:
                    self.childs.append(word)

class LocalizableCodeGen(Base):
    key = ""
    childs = []
    lastKey = ""
    parent = ""

    def __init__(self, key):
        Base.__init__(self)
        self.key = key

    def __str__(self):
        return self.key

                
                
                

       
    

