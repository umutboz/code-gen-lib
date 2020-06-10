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
