#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# Environment
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################

# Built-in/Generic Imports
# from __future__ import annotations
# rom typing import Optional

# Own modules
from enums import DevelopmentEnvironment
from singleton import Singleton


@Singleton
class Environment(object):
    global env
    env = DevelopmentEnvironment().DEBUG

    def debug(self):
        global env
        env = DevelopmentEnvironment().DEBUG

    def local(self):
        global env
        env = DevelopmentEnvironment().LOCAL

    def online(self):
        global env
        env = DevelopmentEnvironment().ONLINE

    def current(self):
        global env
        return env
