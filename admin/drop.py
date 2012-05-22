import os
import shutil
from tools.tools import object_in_file_list,get_object_from_file_extend_to_list,write_to_file
from tools.tools import get_table_data_file_path,get_table_info_txt_path,get_database_path,get_all_table_name_info_txt_path
from tools.default_variable import DATABASE_FILE_PATH
from exist import is_table_exist
from tools import default_variable

def drop_database(database_name):
    if not object_in_file_list(obj = database_name , file_path = DATABASE_FILE_PATH):
        print 'The database had not exists!\nCheck you input'
        return False
    
    database_path = get_database_path(database_name)
    
    try:
        shutil.rmtree(database_path)
    except:
        print 'Drop error!'
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
        print 'The table has not exists!\nCheck you input'
        return False
    
    table_info_path = get_table_info_txt_path(database_name,table_name)
    table_data_path = get_table_data_file_path(database_name,table_name)
    all_tables_info_path = get_all_table_name_info_txt_path(database_name)
    
    try:
        os.remove(table_info_path)
        os.remove(table_data_path)
    except:
        print 'Drop error!'
        return False
        
    tables = get_object_from_file_extend_to_list(all_tables_info_path)
    after_drop_tables = [tb for tb in tables if tb != table_name]
    tables = '\n'.join(after_drop_tables)
    write_to_file(string = tables,file_path = all_tables_info_path)
    
    return True