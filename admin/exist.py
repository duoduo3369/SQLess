
from tools.tools import object_in_file_list,get_object_from_file_append_to_list,delete_blank_line_in_file
from tools.tools import get_table_info_txt_path, get_all_table_name_info_txt_path
from tools.default_variable import  DATABASE_FILE_PATH

def is_database_exist(dbname, databases_path = DATABASE_FILE_PATH):
    if object_in_file_list(obj = dbname, file_path = databases_path):
        return True
    return False

def is_table_exist(dbname,table_name):
    table_infomath_file_path = get_all_table_name_info_txt_path(dbname)
    if object_in_file_list(obj = table_name, file_path = table_infomath_file_path):
        return True
    return False

def is_row_exist(dbname,table_name,row_name):
    
    table_info_path = get_table_info_txt_path(dbname,table_name)
    
    delete_blank_line_in_file(table_info_path)
    
    rows_info = get_object_from_file_append_to_list(table_info_path)
    #print 'in is_row_exist rows_info',rows_info
    for r in rows_info:
        #print 'in is_row_exist  r',r
        if len(r) == 0:
            continue
        try:
            if r[0] == row_name:
                return True
        except:
            return False
    return False

def is_db_and_tb_both_exist(database_name,table_name):
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return False
    
    if is_table_exist(dbname = database_name,table_name = table_name) == False:
        print 'The table named %s was not exists!' % (table_name)
        return False