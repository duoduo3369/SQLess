#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from tools.tools import append_string_to_file,get_data_base_path,write_to_file
from tools.default_variable import DATABASE_FILE_PATH,\
 TABLES_NAME_FILE,TABLE_INFO_FILE_SUFFIX,TABLE_DATA_FILE_SUFFIX
from admin.exist import is_database_exist,is_table_exist



def create_database(database_name,databases_file_path = DATABASE_FILE_PATH):
    
    if is_database_exist(database_name) == True:
        print 'The database named %s was already exists!' % (database_name)
        return False

    new_database_path = get_data_base_path(database_name)
    
    try:
        os.mkdir(new_database_path)
    except:
        print 'can not built the database!'
        return False    
    
    write_to_file(string = '',file_path = r'%s\%s' % (new_database_path,TABLES_NAME_FILE))    
    append_string_to_file(string = database_name + '\n', file_path = databases_file_path)
        
    return True


from whether_can_new import whether_can_new_table_object

def create_table(database_name,table_name,rows):
    if  database_name is None:
        print 'No database select ,please use a database first.'
        return False
    
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return False
    
    if is_table_exist(dbname = database_name,table_name = table_name) == True:
        print 'The table named %s has already exists!' % (table_name)
        return False
    
    if whether_can_new_table_object(table_name,rows) == False:
        print r' Your input was wrong.'
        return False
    
    database_path = get_data_base_path(database_name)
    table_name_append_suffix = table_name + TABLE_INFO_FILE_SUFFIX
    table_info = ''
    
    for row in rows:
        table_info += '\t'.join(row)
        table_info += '\n'
    write_to_file(string = table_info,file_path = r'%s\%s' % (database_path ,table_name_append_suffix))
    write_to_file(string = '',file_path = r'%s\%s%s' % (database_path ,table_name,TABLE_DATA_FILE_SUFFIX))

    append_string_to_file(string = table_name + '\n', file_path = r'%s\%s' % (database_path,TABLES_NAME_FILE))
    print 'Table created successful!'
    return True

