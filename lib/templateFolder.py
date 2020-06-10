#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# TemplateFolder
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################


# Owned
from abstract import Base
from enums import MESSAGE_TYPE


class TemplateFolder(Base):
    # root templateStreaming file path + append your source path
    source = ""
    # root templateModule path + append your target path
    outputPath = ""
    isOnline = False

    def __init__(self, source, output_path, is_online=False):
        Base.__init__(self)
        self.source = source
        self.outputPath = output_path
        self.isOnline = is_online
