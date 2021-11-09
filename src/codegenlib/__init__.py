__version__ = "0.6"

import os
import sys
import re
import shutil
import json
#import urllib2
import ssl
#import urllib3

from . import constantType
from .constantType import constant
from . import enums
from . import environment
from . import singleton
from .log import Logger,Log
from .enums import MESSAGE_TYPE,MUSTACHE,CODING
from .enums import DevelopmentEnvironment
from .environment import Environment
from .singleton import Singleton
from .abstract import Base
from .templateFile import TemplateFile
from .fileOperation import FileOperation
from .templateModule import TemplateModule

from .templateFolder import TemplateFolder

#from .httpOperation import HttpOperation
#from .httpOperation3 import HttpOperation3
from .parser import Parser


from .templateStreaming import TemplateStreaming


