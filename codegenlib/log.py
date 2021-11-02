#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# Log
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################


class Logger:
    """This class now shares all its attributes among its various instances"""

    # This essentially makes the singleton objects an object-oriented global variable
    def __init__(self):
        pass

    def e(self, message):
        print ("\x1b[6;30;41m" + message + "\x1b[0m")

    def i(self, message):
        print ("\x1b[7;37;40m" + message + "\x1b[0m")

    def s(self, message):
        print ("\x1b[6;30;42m" + message + "\x1b[0m")
    
    def w(self, message):
        print ("\x1b[6;30;43m" + message + "\x1b[0m")


Log = Logger()
