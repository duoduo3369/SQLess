#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from tools.tools import object_in_file_list,append_string_to_file

project_path = os.getcwd()
databases_file_path = project_path + r'\system\databases.txt'

def create_database(new_database_name,databases_path = databases_file_path):
    new_database_name = str(new_database_name)
    
    if object_in_file_list(obj = new_database_name, file_path = databases_path):
        print 'The database named %s was already exists!' % (new_database_name)
        return False
    
    new_database_path = project_path + (r'\databases\%s' % new_database_name)
    
    try:
        os.mkdir(new_database_path)
    except:
        print 'can not built the database!'
        return False    
        
    append_string_to_file(string = new_database_name + '\n', file_path = databases_path)
        
    return True