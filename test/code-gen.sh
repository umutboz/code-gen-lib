#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""

import os
import sys
from lib.fileOperation import FileOperation


module = ''

# coding start
# code-gen -module -params
if len(sys.argv) >= 3:
    module = str(sys.argv[1])
    print(module)
    param_serviceName = str(sys.argv[2])
    op = FileOperation()
    print(op.getPath())