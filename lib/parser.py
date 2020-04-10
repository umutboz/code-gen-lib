#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## parser
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

#Owned
from abstract import Base

class Parser(Base):
    def __init__(self):
        Base.__init__(self)
    
    def string_multiple_replace(string, replacement_dict):
        pattern = re.compile("|".join([re.escape(k) for k in sorted(
        replacement_dict, key=len, reverse=True)]), flags=re.DOTALL)
        return pattern.sub(lambda x: replacement_dict[x.group(0)], string)
    
    string_multiple_replace = staticmethod(string_multiple_replace)