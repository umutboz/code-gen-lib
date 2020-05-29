#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
## TemplateModule
############################################################
## Author: Umut Boz
## Copyright (c) 2020, OneframeMobile, KoçSistem
## Email: oneframemobile@gmail.com
############################################################
## Version: 0.1.0
############################################################


# Owned
from abstract import Base
from enums import MESSAGETYPE


class TemplateModule(Base):
    name = ""
    templates = []

    def __init__(self, name, templates):
        Base.__init__(self)
        self.name = name
        self.templates = templates
