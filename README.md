# code-gen-library
code-gen-library for Python

![alt text](https://github.com/umutboz/code-gen-lib/blob/master/code_gen_diagram.png?raw=true)


## code-gen-lib import package

```python
from lib.enums import MUSTACHE
from templateStreaming import TemplateStreaming
from lib.templateFile import TemplateFile
from lib.templateModule import TemplateModule
```

## using example
```python
code_gen_lib_example.py
```

## code-gen-lib generation from json file
```python
config_json_example.py

## with folder
 config_json_with_template_folder_example.py
```

## code-gen-lib generation programming example
You should add your module containing your folder pathname to the 'modules' path. You can add mustache files and template folder/files in your module path
```python
from lib.enums import MUSTACHE
from templateStreaming import TemplateStreaming
from lib.templateFile import TemplateFile
from lib.templateModule import TemplateModule

fileName = "test.swift"

testManagerClassTF = TemplateFile(
    name="learning_class_mustache",
    dict={"service_name": "OneframeMobile", "request_func": MUSTACHE.PARENT},
    output_file="Manager.swift"
)
testGetRequestFuncTF = TemplateFile(
    name="request_get_func_mustache",
    dict={"result_model_name": "String"},
    output_file=None,
    is_child_template=True,
    parent_mustache="request_func"
)
testPostRequestFuncTF = TemplateFile(
    name="request_post_func_mustache",
    dict={"result_model_name": "UserModel"},
    output_file=None,
    is_child_template=True,
    parent_mustache="request_func"
)

testModule = TemplateModule(
    name="networking-swagger-swift",
    templates_files=[testManagerClassTF, testGetRequestFuncTF, testPostRequestFuncTF]
)

tStreaming = TemplateStreaming(
    templateModule=testModule
)
tStreaming.execute()
```

## code-gen-lib generation programming example with your json file
```python
import os
import sys

from lib.parser import Parser
# Own modules
from templateStreaming import TemplateStreaming

pathname = os.path.dirname(sys.argv[0])
# current path
json_file_name = "sample_config_with_template_folder.json"
json_file_path = pathname + "/" + json_file_name

sampleJsonModule = Parser.jsonToTemplateModule(json_file=json_file_path)
sampleJsonModule.outputDirectory = "oneframe-api-ios"
sampleJsonModule.isAppendOutputPath = True

print(sampleJsonModule.getOutputDirectoryPath())

tStreaming = TemplateStreaming(
    template_module=sampleJsonModule,
    enable_log=False,
)
tStreaming.execute()
```

Can be Contribution, join us!
![alt text](https://github.com/umutboz/code-gen-lib/blob/master/contribution_model.png?raw=true)