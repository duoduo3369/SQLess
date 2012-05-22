from admin.exist import is_database_exist, is_table_exist

def use_database(database_name):
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return None
    else:
        print 'database changed!'
        return database_name
    
from tools.tools import  get_object_from_file_extend_to_list, \
get_object_from_file_append_to_list,\
get_all_table_name_info_txt_path,get_table_info_txt_path

from tools.default_variable import DATABASE_FILE_PATH 
def show_databases():
    databases = get_object_from_file_extend_to_list(DATABASE_FILE_PATH)
    print 'All databases:'
    for db in databases:
        print db
    print '' 
    
    return databases
    
def show_tables(database_name):
    if database_name is None:
        print 'Not database used, use a database fisrt!'
        return None
    
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return None
    
    table_infomath_file_path = get_all_table_name_info_txt_path(database_name)
    tables = get_object_from_file_extend_to_list(table_infomath_file_path)
    print 'All tables:'
    for tb in tables:
        print tb
    print '' 
    
    return tables

def desc_table(database_name,table_name):
    if database_name is None:
        print 'Not database used, use a database fisrt!'
        return None
    
    if table_name is None:
        print 'Please input the table you want to check out!'
        return None
    
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return None
    
    if is_table_exist(dbname = database_name,table_name = table_name) == False:
        print 'The table named %s was not exists!' % (table_name)
        return None
    info_path = get_table_info_txt_path(database_name,table_name)
    table_infomation = get_object_from_file_append_to_list(info_path)
    for info in table_infomation:
        print ' '.join(info)
        
    return table_infomation