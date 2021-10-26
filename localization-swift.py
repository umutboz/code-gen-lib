# -*-coding:UTF-8 -*-
#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""
#!/usr/bin/python

############################################################
# localization-swfit .py
############################################################
# Author: Umut Boz
# Copyright (c) 2020, OneframeMobile, KoçSistem
# Email: oneframemobile@gmail.com
############################################################
# Version: 0.1.0
############################################################

# Built-in/Generic Imports
import os
import sys
import numpy as np

# for localization import
from os.path import dirname,join, abspath,sys
module_path =  os.path.join(os.path.dirname(__file__), 'modules/localization-swift')
module = os.path.abspath(module_path)

# Own modules
from lib.enums import MUSTACHE
from lib.enums import CODING
from lib.templateFile import TemplateFile
from lib.templateModule import TemplateModule
from lib.templateStreaming import TemplateStreaming
from lib.fileOperation import FileOperation
from lib.log import Log
from lib.parser import Parser
from lib.environment import Environment

# for importing added sub module python files 
sys.path.append(module)
from localizable import Localizable, LocalizableCodeGen

Environment.Shared().online()
refills = []

'''
# START - written for lib module
import sys
import os
from os.path import dirname, join, abspath
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
lib_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib'))
sys.path.append(root_dir)
sys.path.append(lib_dir)
# END - written for lib module
'''
localizationModule = TemplateModule(
    name = "localization-swift",
    templates_files = []
)
tStreaming = TemplateStreaming(
    template_module = localizationModule        
)

def recursive_field_content(parent):
    # alllast keys
    content = ""
    index = 0
    # sample dictionary = {"field_name":"title", "localization_string_key": "Pages.UI.title"}
    for child in parent.childs:
        index = child.index
        field_tf = TemplateFile(
            name = "localization_struct_field_mustache",
            dict = {"field_name": child.key, "localization_string_key":child.fullKey},
            parent_mustache = "extension_child_add",
            is_child_template=True,
            output_file = None
        )
        loop_child_content = tStreaming.fileContent(file=field_tf)
        replaced_template_content = Parser.string_multiple_replace(loop_child_content, tStreaming.dictToMustache(field_tf.dict))
        content = content + replaced_template_content + CODING.NEWLINE
        child.templateFile = field_tf
    return tStreaming.tabbedContent(content=content, tab_index=index + 1)

def recursive_struct_content(current):
    # all last keys
    content = ""
    struct_tf = TemplateFile(
        name = "localization_child_inline_struct_extension_mustache",
        dict = {"extension_child_struct_name": current.key},
        parent_mustache = "extension_parent_add",
        is_child_template=True,
        output_file = None,
        child_template_files = []
    )
    content = tStreaming.fileContent(file=struct_tf)
    replaced_template_content = Parser.string_multiple_replace(content, tStreaming.dictToMustache(struct_tf.dict))
    current.templateFile = struct_tf
    return tStreaming.tabbedContent(content=replaced_template_content, tab_index=current.index)

def get_index_on_array(obj):
    index = next((i for i, item in enumerate(obj.parentObject.childs) if item.key == obj.key), -1)
    return index

def seek_and_find_clear_field(temp_obj):
    last_child_keys_filter = filter(lambda x : x.isLastKey == True, temp_obj.childs)
    last_child_keys = list(last_child_keys_filter)
    result_content = recursive_field_content(parent = temp_obj)
    temp_obj.generatedFieldContent = CODING.NEWLINE + result_content
    temp_obj.childs = list(set(temp_obj.childs) - set(last_child_keys_filter))

def seek_and_find(parent_obj,temp_obj = None):
    if temp_obj == None:
        temp_obj = parent_obj
    
    if len(temp_obj.childs) != 0:
        # is lastKey ? thats field
        if contains(temp_obj.childs, lambda x: x.isLastKey == True):
            # has any child struct members at same time
            if contains(temp_obj.childs, lambda x: x.isLastKey == False):
                seek_and_find_clear_field(temp_obj = temp_obj)

                other_struct_len = len(temp_obj.childs)
                if other_struct_len > 0:
                    first_obj = temp_obj.childs[0]
                    find_member_filter = filter(lambda x : x.key != first_obj.key, temp_obj.childs)
                    find_members = list(find_member_filter)
                    if len(find_members) > 0:
                        for other in find_members:
                            refills.append(other)
                    return seek_and_find(parent_obj = parent_obj, temp_obj = first_obj)
            else:
                seek_and_find_clear_field(temp_obj = temp_obj)

                # generate struct content all own parents
                is_there_any_work_to_do_for_parents = True
                loop_obj = temp_obj
                while is_there_any_work_to_do_for_parents:
                    if loop_obj.generatedStructContent == '':
                        loop_obj.generatedStructContent = recursive_struct_content(current = loop_obj)
                        if loop_obj.parentObject.parent != '':
                            loop_obj = loop_obj.parentObject
                        else:
                            is_there_any_work_to_do_for_parents = False
                    else:
                        is_there_any_level_to_do_for_parents_child = False
                        for child in loop_obj.childs:
                            if len(child.childs) != 0 or child.generatedStructContent == '':
                                is_there_any_level_to_do_for_parents_child = True
                                break
                        
                        if is_there_any_level_to_do_for_parents_child == False:
                            loop_obj.resultContent = loop_obj.get_last_struct_merge_content()
                            loop_obj.childs = []
                            inner_content = loop_obj.generatedFieldContent 
                            if loop_obj.resultContent != '':
                                inner_content += CODING.NEWLINE + loop_obj.resultContent
                            temp_dict = { "{{extension_child_add}}" : inner_content }
                            loop_obj.generatedStructContent = Parser.string_multiple_replace(loop_obj.generatedStructContent, temp_dict)
                            '''
                            if loop_obj.parent == 'UI' and loop_obj.key == 'UserInfoDetails':
                                print("fur")
                            '''
                        if loop_obj.parentObject.parent != '':
                            loop_obj = loop_obj.parentObject
                        else:
                            is_there_any_work_to_do_for_parents = False    
        else:
            first_obj = temp_obj.childs[0]
            find_member_filter = filter(lambda x : x.key != first_obj.key, temp_obj.childs)
            find_members = list(find_member_filter)
            if len(find_members) > 0:
                for other in find_members:
                    refills.append(other)
            return seek_and_find(parent_obj=parent_obj, temp_obj=first_obj)

     # other memory work to do
    if len(refills) > 0:
        toDo = refills[0]
        #todo find from parent
        refills.remove(toDo)
        return seek_and_find(parent_obj=parent_obj, temp_obj=toDo)
         
def collect_execute_data(parent_obj,temp_obj = None):
    if temp_obj == None:
        temp_obj = parent_obj
    '''
    # for test
    if parent_obj.key == "Shared":
        print("fur")
    '''
    if len(temp_obj.childs) == 0:
        if temp_obj.parent == '':
            inner_content = temp_obj.generatedFieldContent + CODING.NEWLINE + temp_obj.resultContent
            temp_dict = { "{{extension_parent_add}}" : inner_content }
            loop_child_content = Parser.string_multiple_replace(temp_obj.generatedStructContent, temp_dict)
            #temp_obj.content = loop_child_content + CODING.NEWLINE
            temp_obj.generatedStructContent = loop_child_content + CODING.NEWLINE
        else:
            inner_content = temp_obj.generatedFieldContent + CODING.NEWLINE + temp_obj.resultContent
            temp_dict = { "{{extension_child_add}}" : inner_content }
            loop_child_content = Parser.string_multiple_replace(temp_obj.generatedStructContent, temp_dict)
        
            found_parent = temp_obj.parentObject
            if found_parent.parent != "":
                found_parent.childs.remove(temp_obj)
            found_parent.content += loop_child_content + CODING.NEWLINE
    else:
        first_obj = temp_obj.childs[0]
        find_member_filter = filter(lambda x : x.key != first_obj.key, temp_obj.childs)
        find_members = list(find_member_filter)
        if len(find_members) > 0:
            for other in find_members:
                refills.append(other)
        return collect_execute_data(parent_obj=parent_obj, temp_obj = first_obj)
    
    # other memory work to do
    if len(refills) > 0:
        toDo = refills[0]
        #todo find from parent
        refills.remove(toDo)
        return collect_execute_data(parent_obj=parent_obj, temp_obj=toDo)
    else:
        '''
        if parent_obj.key == "Pages":
            print("fur")
        '''
        if len(parent_obj.childs) > 0:
            has_any_child = False
            find_child_filter = filter(lambda x : len(x.childs) > 0, parent_obj.childs)
            if len(find_child_filter) == 0:
                if parent_obj.content == "":
                    for child in parent_obj.childs:
                        inner_content = CODING.NEWLINE + child.content
                        if child.resultContent != '':
                            inner_content += CODING.NEWLINE + child.resultContent   
                        temp_dict = { "{{extension_child_add}}" : inner_content }
                        parent_obj.content += Parser.string_multiple_replace(child.generatedStructContent, temp_dict)

                temp_dict = { "{{extension_parent_add}}" : parent_obj.content }
                parent_obj.generatedStructContent = Parser.string_multiple_replace(parent_obj.generatedStructContent, temp_dict)
                parent_obj.childs = []
            else:
                is_there_any_work_to_do_for_parents = True
                temps = []
                loop_obj = parent_obj
                while is_there_any_work_to_do_for_parents:
                    if len(loop_obj.childs) == 0:
                        '''
                        if loop_obj.key == "Appointment":
                            print("fur")
                        '''
                        inner_content = CODING.NEWLINE + loop_obj.content
                        if loop_obj.resultContent != '':
                            inner_content += CODING.NEWLINE + loop_obj.resultContent 
                        temp_dict = { "{{extension_child_add}}" : inner_content }
                        loop_child_content = Parser.string_multiple_replace(loop_obj.generatedStructContent, temp_dict)
                        found_parent = loop_obj.parentObject
                        if loop_obj.parent != "":
                            found_parent.childs.remove(loop_obj)

                        if found_parent.content.find(loop_child_content) == -1:
                            found_parent.content += loop_child_content + CODING.NEWLINE

                        has_found_parent = False
                        if found_parent.parent != '' and len(found_parent.childs) == 0:
                            inner_content = found_parent.generatedFieldContent + CODING.NEWLINE + found_parent.content #+  CODING.NEWLINE
                            temp_dict = { "{{extension_child_add}}" : inner_content }
                            loop_child_content = Parser.string_multiple_replace(found_parent.generatedStructContent, temp_dict)
                            found_parent.parentObject.childs.remove(found_parent)
                            found_parent.parentObject.content += loop_child_content
                            if len(found_parent.parentObject.childs) == 0 and found_parent.parent != '' and found_parent.parentObject.content != '':
                                #   has next parent object contains from temps
                                if len(filter(lambda x : x.key == found_parent.parentObject.key, temps)) == 0:
                                    loop_obj = found_parent.parentObject
                                    has_found_parent = True

                        if has_found_parent == False:
                        # continue to do work other temp object or same level object
                            if len(temps) > 0:
                                same_level_next_member_filter = filter(lambda x : x.parent == loop_obj.parent, temps)
                                if len(list(same_level_next_member_filter)) > 0:
                                    toDo = list(same_level_next_member_filter)[0]
                                    #todo find from parent
                                    temps.remove(toDo)
                                    loop_obj = toDo
                                else:
                                    toDo = temps[0]
                                    #todo find from parent
                                    temps.remove(toDo)
                                    loop_obj = toDo
                            else:
                                # has not change {{extension_parent_add}} parent on generatedStructContent return to beginning point
                                is_there_any_work_to_do_for_parents = False                        
                    else:
                        first_obj = loop_obj.childs[0]
                        find_other_member_filter = filter(lambda x : x.key != first_obj.key, loop_obj.childs)
                        for child in list(find_other_member_filter):
                            temps.append(child)
                        if len(first_obj.childs) == 0:
                            # to do merge all childs any level
                            inner_content = first_obj.generatedFieldContent + CODING.NEWLINE + first_obj.content #+  CODING.NEWLINE
                            temp_dict = { "{{extension_child_add}}" : inner_content }
                            loop_child_content = Parser.string_multiple_replace(first_obj.generatedStructContent, temp_dict)
                            found_parent = first_obj.parentObject
                            #crash
                            found_parent.childs.remove(first_obj)
                            found_parent.content += loop_child_content

                            has_found_parent = False
                            # has any child member
                            if found_parent.parent != '' and len(found_parent.childs) == 0:
                                inner_content = found_parent.generatedFieldContent + CODING.NEWLINE + found_parent.content #+  CODING.NEWLINE
                                temp_dict = { "{{extension_child_add}}" : inner_content }
                                loop_child_content = Parser.string_multiple_replace(found_parent.generatedStructContent, temp_dict)
                                found_parent.parentObject.childs.remove(found_parent)
                                found_parent.parentObject.content += loop_child_content
                                if len(found_parent.parentObject.childs) == 0 and found_parent.parent != '' and found_parent.parentObject.content != '':
                                    #   has next parent object contains from temps
                                    if len(filter(lambda x : x.key == found_parent.parentObject.key, temps)) == 0:
                                        loop_obj = found_parent.parentObject
                                        has_found_parent = True
                            
                            if has_found_parent == False:
                                if len(temps) > 0:
                                    same_level_next_member_filter = filter(lambda x : x.parent == first_obj.parent, temps)
                                    if len(list(same_level_next_member_filter)) > 0:
                                        toDo = list(same_level_next_member_filter)[0]
                                        #todo find from parent
                                        temps.remove(toDo)
                                        loop_obj = toDo
                                    else:
                                        toDo = temps[0]
                                    #todo find from parent
                                        temps.remove(toDo)
                                        loop_obj = toDo
                                else:
                                    # has not change {{extension_parent_add}} parent on generatedStructContent
                                    is_there_any_work_to_do_for_parents = False
                        else:
                            next_first_obj = first_obj.childs[0]
                            find_next_other_member_filter = filter(lambda x : x.key != next_first_obj.key, first_obj.childs)
                            for child in list(find_next_other_member_filter):
                                temps.append(child)
                            # set next loop object    
                            loop_obj = next_first_obj
                        
            # has not change {{extension_parent_add}} parent on generatedStructContent return to beginning point
            is_there_any_work_to_do_for_parents = False
            if parent_obj.generatedStructContent.find("{{extension_parent_add}}") != -1:
                temp_dict = { "{{extension_parent_add}}" : parent_obj.content }
                parent_obj.generatedStructContent = Parser.string_multiple_replace(parent_obj.generatedStructContent, temp_dict)


# code generation execution
def execute(localizations):
    if len(localizations) == 0:
        Log.e("String file parsing issue, Strings must conform to file schema, please check!")
    else:
        parent_struct_file = TemplateFile(
            name = "localization_struct_file_mustache",
            dict = {},
            output_file="Localization.swift"
        )
        localizationModule.templateFiles.append(parent_struct_file)
        
        # collect all child content
        for loc in localizations:
            struct_file = TemplateFile(
                name = "localization_parent_struct_extension_mustache",
                dict = {"extension_parent_struct_name": loc.key },
                output_file="Localization-" + loc.key + "+Extensions.swift",
                child_template_files = []
            )
            loc.templateFile = struct_file

            find_fields_filter = filter(lambda x : x.isLastKey == True, loc.childs)
            find_fields = list(find_fields_filter)
                
            if len(find_fields) > 0:
                seek_and_find_clear_field(temp_obj = loc)

            for child in loc.childs:
                response_data = seek_and_find(parent_obj = child, temp_obj = None)
            
            content = tStreaming.fileContent(file=struct_file)
            replaced_template_content = Parser.string_multiple_replace(content, tStreaming.dictToMustache(struct_file.dict))
            loc.generatedStructContent = replaced_template_content

        # execute generate all content
        for loc in localizations:
            collect_execute_data(parent_obj=loc)
            loc.templateFile.content = loc.generatedStructContent
            localizationModule.templateFiles.append(loc.templateFile)
            Log.w(loc.templateFile.outputFile)
                
        localizationModule.outputDirectory = "localization"
        localizationModule.isAppendOutputPath = True
        
        tStreaming.templateModule = localizationModule
        tStreaming.execute()
        

def check_string_file_extension(string_file):
    result = False
    if string_file.lower().endswith('.strings'):
        result = True
    else :
        Log.e("** must be localizable string file ! **")
        Log.w(string_file)
    return result

def checkStringFileExists(string_file):
    result = False
    if FileOperation().isExist(string_file):
        result = True
    else :
        Log.e("** localizable string file not found **")
        Log.w(string_file)
    return result

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

def getFullKey(split_array):
        fullKey = ""
        array_len = len(split_array)
        for key in split_array:
            fullKey = fullKey + key + "."
        
        fullKey = fullKey[:-1]
        return fullKey


def recursive_find_child_obj(full_split,obj, parent_key,current_key, column_index,index_counter=1):
    response_data = None
    is_found = False
    keyword = full_split[index_counter]
    for j in range(len(obj.childs)):
        child_keyword = obj.childs[j].key
        if keyword == child_keyword:
            if obj.childs[j].index == column_index - 1:
                response_data = obj.childs[j]
                is_found = True
                break
            else:
                try:
                   return recursive_find_child_obj(full_split=full_split,obj=obj.childs[j],parent_key=parent_key,current_key=current_key,column_index=column_index,index_counter=obj.childs[j].index+1)
                except ValueError:                     # the recursion doesn't raise
                    pass   
        else:
            print(keyword, " vs ", child_keyword)
    if is_found:
        return (is_found,response_data)
    else:
        return (False,None)
        

def recursive_add_child(obj,parent_key, current_key, column_index, array_len, full_split):
    if obj.key == parent_key:
        if not contains(obj.childs, lambda x: x.key == current_key and x.index == column_index):
            localizable = LocalizableCodeGen(key = current_key)
            localizable.parent = parent_key
            localizable.parentObject = obj
            localizable.childs = []
            # is last index 
            if column_index + 1 == array_len:
                localizable.fullKey = getFullKey(full_split)
                localizable.index = column_index
                localizable.isLastKey = True
            else:
                localizable.index = column_index
            obj.childs.append(localizable)

        else:
            print(current_key, "exists data")
    else:
        if column_index < 3:
            for child in obj.childs:
                if child.key == parent_key and child.index == column_index - 1:
                    recursive_add_child(child, current_key=current_key, parent_key=parent_key,column_index=column_index,array_len=array_len,full_split=full_split)
        else:
            
            (r,d) = recursive_find_child_obj(full_split=full_split,obj=obj,parent_key=parent_key,current_key=current_key,column_index=column_index)
            if r:
                recursive_add_child(d, current_key=current_key, parent_key=parent_key,column_index=column_index,array_len=array_len,full_split=full_split)
            else:
                print(current_key, "not match")
        

#tStreaming.execute()
# -localizable-string-file -params "-p/-fp/--info"
if len(sys.argv) >= 3:
    Environment.Shared().online()
    op = FileOperation()
    is_okay_string_file = False
    params = str(sys.argv[1])
    localizable_string_file_path_param = str(sys.argv[2])
    localizable_string_file_path = ""

    if params == "-p":
        path_name = os.getcwd()
        localizable_string_file_path = path_name + CODING.SLASH + localizable_string_file_path_param
        #print(localizable_string_file_path)
        if check_string_file_extension(string_file=localizable_string_file_path) and checkStringFileExists(localizable_string_file_path):
            is_okay_string_file = True
    
    elif params == "-fp":
        localizable_string_file_path = localizable_string_file_path_param
        #print(localizable_string_file_path)
        if check_string_file_extension(string_file=localizable_string_file_path) and checkStringFileExists(localizable_string_file_path):
            is_okay_string_file = True
    
    if is_okay_string_file:
        op = FileOperation()
        localizable_string_file_content = op.readContent(localizable_string_file_path)
        #print(localizable_string_file_content)

        # load localizable content
        parsed_data = []
        for line in localizable_string_file_content.splitlines():
            if "=" in line:
                first_split = str(line).split('"')
                dot_split = str(first_split[1]).split(".")
                localizable = Localizable(key = str(first_split[1]), data = dot_split, parent = dot_split[0])
                parsed_data.append(localizable)
                #print(localizable.split)
                #print(localizable.childs)


        parsed_split_datas = []
        # load parsed split data 
        for parsed in parsed_data:
            parsed_split_datas.append(parsed.data)
        
        max_len_count = 0
        for data in parsed_split_datas:
            if len(data) > max_len_count:
                max_len_count = len(data)

        arr = np.asarray(parsed_split_datas)

        # parent disticnt
        zet_indexes = []
        for i in range(len(arr)):
            zet_indexes.append(arr[:][i][0])
        parent_structs = reversed(list(set(zet_indexes)))

        localizable_list = []
        # collect disctinct parent 
        for parent in parent_structs:
            localizable = LocalizableCodeGen(key = parent)
            localizable.parent = ""
            localizable.index = 0
            localizable.childs = []
            localizable_list.append(localizable)

        for obj in localizable_list:
            for i in range(len(arr)):
                if obj.key == arr[:][i][0]:
                    for column_index in range(len(arr[:][i])):
                        child_obj = arr[:][i][column_index]
                        if obj.key != child_obj:
                            parent_key = arr[:][i][column_index-1]
                            print(child_obj)
                            '''
                            if child_obj == "SubPages":
                                print("dur")
                            '''
                            recursive_add_child(obj,parent_key=parent_key, current_key=child_obj, column_index=column_index, array_len=len(arr[:][i]),full_split=arr[:][i])

        
        execute(localizable_list)

        #print(max_len_count)
         


else:
    if len(sys.argv) >= 2:
        params = str(sys.argv[1])
        if params == "--info":
            Log.i("you can string file with under folder path -p")
            Log.w("-p /string-file-path")
            Log.i("you can string file with full path -fp")
            Log.w("-fp /Users/***/Desktop/..")

        else:
            Log.e("must be use min. 2 parameters ")
            Log.i("or u can use params --info")
    else:
        Log.e("must be use min. 2 parameters ")
        Log.i("or u can use params --info")

