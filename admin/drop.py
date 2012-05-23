import os
import shutil
from tools.tools import object_in_file_list,get_object_from_file_extend_to_list,write_to_file
from tools.tools import get_table_data_file_path,get_table_info_txt_path,get_database_path
from tools.tools import get_all_table_name_info_txt_path,get_object_from_file_append_to_list
from tools.default_variable import DATABASE_FILE_PATH
from exist import is_table_exist
from tools import default_variable

def drop_database(database_name):
    if not object_in_file_list(obj = database_name , file_path = DATABASE_FILE_PATH):
        print 'The database had not exists!'
        return False
    
    database_path = get_database_path(database_name)
    
    try:
        shutil.rmtree(database_path)
    except:
        #print 'Drop error!'
        return False
    
    databases = get_object_from_file_extend_to_list(DATABASE_FILE_PATH)
    after_drop_databases = [db for db in databases if db != database_name]
    databases = '\n'.join(after_drop_databases)
    write_to_file(string = databases,file_path = DATABASE_FILE_PATH)
    if default_variable.CURRENT_DB == database_name:
        default_variable.CURRENT_DB = None
    return True


def drop_table(database_name,table_name):
    if is_table_exist(database_name,table_name) == False:
        print 'The table has not exists!'
        return False
    
    table_info_path = get_table_info_txt_path(database_name,table_name)
    table_data_path = get_table_data_file_path(database_name,table_name)
    all_tables_info_path = get_all_table_name_info_txt_path(database_name)
    
    try:
        os.remove(table_info_path)
        os.remove(table_data_path)
    except:
        #print 'Drop error!'
        return False
        
    tables = get_object_from_file_extend_to_list(all_tables_info_path)
    after_drop_tables = [tb for tb in tables if tb != table_name]
    tables = '\n'.join(after_drop_tables)
    write_to_file(string = tables,file_path = all_tables_info_path)
    
    return True

from admin.exist import is_row_exist,is_db_and_tb_both_exist
from tools.parse import string_to_token

def drop_row(database_name, table_name, row_name):
    if is_db_and_tb_both_exist(database_name, table_name) == False:
        return False
    if is_row_exist(database_name, table_name, row_name ) == False:
        print 'The row named %s has not exists!' % (row_name)
        return False
    
    table_info_txt_path = get_table_info_txt_path(database_name, table_name)
    table_info_list = get_object_from_file_append_to_list(table_info_txt_path)
    
    after_drop_info = get_drop_row_string_from_infolist(table_info_list,row_name)
        
    write_to_file(after_drop_info, table_info_txt_path)
    
    return True

def get_drop_row_string_from_infolist(table_info_list,drop_row_name):
    after_drop_info = ''
    for row in table_info_list:
        #print 'in drop_row',type(row),len(row)
        try:
            token = string_to_token(row[0])
        except:
            return False            
        if token[0] != drop_row_name:
            for r in row:
                after_drop_info += r + '\t'            
            after_drop_info += '\n'
    return after_drop_info