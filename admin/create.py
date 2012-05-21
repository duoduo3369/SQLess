#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from tools.tools import append_string_to_file,get_data_base_path,write_to_file
from admin.exist import is_database_exist

project_path = os.getcwd()
databases_file_path = project_path + r'\system\databases.txt'
TABLES_NAME_FILE = 'tables.txt'

def create_database(database_name,sys_databases_file_path = databases_file_path):
    
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
    append_string_to_file(string = database_name + '\n', file_path = sys_databases_file_path)
        
    return True


from models.tables import Row,Table

def whether_can_new_table_object(table_name,rows):
    row_list = []
    for row in rows:
        if len(row) == 2:
            r = Row(row[0],row[1])            
        elif len(row) == 3:
            r = Row(row[0],row[1],row[2])            
        else :
            return False
        if r.clean_data():
            row_list.append(r)
        else:
            print 'You input near rows was wrong.'
            return False
        
    table = Table(table_name,row_list)
    if not table.clean_data():
        print 'You input near table was wrong.'
        return False
    
    return True

def create_table(database_name,table_name,rows): 
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return False
    
    if whether_can_new_table_object(table_name,rows) == False:
        print r' Your input was wrong.'
        return False
    
    database_path = get_data_base_path(database_name)
    table_name_append_suffix = table_name + r'_info.txt'
    table_info = ''
    
    for row in rows:
        table_info += '\t'.join(row)
        table_info += '\n'
    write_to_file(string = table_info,file_path = r'%s\%s' % (database_path ,table_name_append_suffix))
    append_string_to_file(string = table_name + '\n', file_path = r'%s\%s' % (database_path,TABLES_NAME_FILE))
    print 'Table created successful!'
    return True

def use_database(database_name):
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return None
    else:
        print 'database changed!'
        return database_name