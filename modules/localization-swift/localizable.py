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
    split = []
    parent = ""
    childs = []
    lastKey = ""

    def __init__(self, key, split, parent):
        Base.__init__(self)
        self.key = key
        self.split = split
        self.parent = parent
        for word in split:
            if self.parent <> word:
                # is last object ?
                if split[len(split)-1] == word:
                    self.lastKey = word
                    self.childs.append(word)
                else:
                    self.childs.append(word)
             
                
                
                

       
    

