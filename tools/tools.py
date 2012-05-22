#!/usr/bin/python
# -*- coding: utf8 -*-


def sql_input(prompt = '',white_split = ';'):
    print prompt    
    s = raw_input()
    input_string = s
    while len(s) == 0 or s[-1] not in white_split:
        print '...  ',
        s = raw_input()
        input_string += '%s\n' % s        
    return input_string

def object_in_file_list(obj,file_path):
    f = open(file_path,'r')
    
    file_list = []
    for line in f:
        file_list.extend(line.split())
        
    f.close()
    
    if obj in file_list:
        return True
    return False

def append_string_to_file(string, file_path):
    f = open(file_path,'a')    
    f.write(string + '\n')
    f.close()

def write_to_file(string,file_path):
    f = open(file_path,'w')    
    f.write(string)
    f.close()

from default_variable import DATABASE_PATH, TABLES_NAME_FILE,TABLE_INFO_FILE_SUFFIX,TABLE_DATA_FILE_SUFFIX

def get_database_path(database_name):
    return DATABASE_PATH + ( r'\%s' % database_name)

def get_table_data_file_path(dbname,tb_name):
    return r'%s\%s\%s%s' % (DATABASE_PATH, dbname,tb_name,TABLE_DATA_FILE_SUFFIX)

def get_table_info_txt_path(dbname,tb_name):
    return r'%s\%s\%s%s' % (DATABASE_PATH, dbname,tb_name,TABLE_INFO_FILE_SUFFIX)

def get_all_table_name_info_txt_path(dbname):   
    return r'%s\%s\%s' % (DATABASE_PATH, dbname, TABLES_NAME_FILE)

  
def get_object_from_file_extend_to_list(file_path):
    """ 
        only one object at a line, return a list like [x, y ].
    """
    out_list = []
    f = open(file_path , 'r')
    for line in f:
        out_list.extend(line.split())
    f.close()
    return out_list

def get_object_from_file_append_to_list(file_path):
    """ 
        one line has many object ,return a list like [ [x], [xy] ].
    """
    out_list = []
    f = open(file_path , 'r')
    for line in f:
        out_list.append(line.split())
    f.close()
    return out_list


import os
project_path = os.getcwd()

def get_data_base_path(database_name):
    return project_path + (r'\databases\%s' % database_name)