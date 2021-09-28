#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# Enums
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################


from constantType import constant


# choose these enums for user feedback


class MessageType(object):
    @constant
    def INFO():
        return "INFO"

    @constant
    def ERROR():
        return "ERROR"

    @constant
    def SUCCESS():
        return "SUCCESS"


# TemplateFile choose what development environment you want
# github raw templates or local template files


class DevelopmentEnvironment(object):
    @constant
    def LOCAL():
        return "LOCAL"

    @constant
    def ONLINE():
        return "ONLINE"

    @constant
    def DEBUG():
        return "DEBUG"


# choose these enums for code syntax


class CodeLine(object):
    @constant
    def NEWLINE():
        return "\n"

    @constant
    def SPACE_AFTER():
        return "    "

    @constant
    def SLASH():
        return "/"

    @constant
    def DOT():
        return "."
    
    @constant
    def TAB():
        return "\t"


# choose these Mustache enums for code syntax


class Mustache(object):
    @constant
    def PARENT():
        return "PARENT"

    @constant
    def SUB():
        return "SUB"

    @constant
    def LEFT_BRACKET():
        return "{"

    @constant
    def RIGHT_BRACKET():
        return "}"


CODING = CodeLine()
MESSAGE_TYPE = MessageType()
MUSTACHE = Mustache()
