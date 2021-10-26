# code-gen-library - localization-swift module
code-gen-library - localization-swift module with Python bash script execute to localization swift files(struct and extension) by localization strings file


## using example
```python
sh code_gen_lib_example.py
```

## code-gen-lib localization module parameters --info
```python
sh localization-swift.py --info                                            
In the __init__  method of the Base class call child from : FileOperation
you can string file with under folder path -p
-p /string-file-path
you can string file with full path -fp
-fp /Users/***/Desktop/..
```


## code-gen-lib localization module parameters with full path -fp for strings file
```python
sh localization-swift.py -fp /Users/***/Desktop/App/localization-swift/Localizable.strings


generated files ...
Localization-General+Extensions.swift
Localization-Components+Extensions.swift
Localization-Pages+Extensions.swift
Localization-Shared+Extensions.swift
Localization-PushNotification+Extensions.swift
```

## code-gen-lib localization module parameters  with sub path -p for strings file
```python
sh localization-swift.py -p modules/localization-swift/Localizable.strings


generated files ...
Localization-General+Extensions.swift
Localization-Components+Extensions.swift
Localization-Pages+Extensions.swift
Localization-Shared+Extensions.swift
Localization-PushNotification+Extensions.swift
```