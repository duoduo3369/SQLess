
from tools.tools import object_in_file_list,get_all_table_name_info_txt_path
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