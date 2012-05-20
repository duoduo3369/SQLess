#!/usr/bin/python
# -*- coding: utf8 -*-


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