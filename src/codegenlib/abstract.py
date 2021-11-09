#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
# Abstract
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################
from codegenlib.enums import DevelopmentEnvironment
from codegenlib.environment import Environment
from codegenlib.singleton import Singleton
from codegenlib.enums import MESSAGE_TYPE
from codegenlib.log import Log


class Base():
    def __init__(self):
        if type(self) is Base:
            raise Exception('Base is an abstract class and cannot be instantiated directly')
        # Any initialization code
        if Environment.Shared().current() == DevelopmentEnvironment().DEBUG:
            print('In the __init__  method of the Base class' + ' call child from : ' + self.toString())

    def log(self, message, message_type):
        #print("base'den " + str(Environment.Shared().current()))
        # ÇALIŞMA ORTAMI FARKET meksizin tüm hatalar(exceptions) gösterilir.
        if message_type == MESSAGE_TYPE.ERROR:
            Log.e(message=message)
        else:
            # loglar ise sadece debug modda gösterilir
            if Environment.Shared().current() == DevelopmentEnvironment().DEBUG:
                print("base log çalıştı")
                Log.i(message=message)
            '''
            else:
                print("base log çalışmadı")
            '''
            
    def toString(self):
        return self.__class__.__name__
