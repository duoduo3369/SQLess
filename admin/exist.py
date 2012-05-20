import os
from tools.tools import object_in_file_list

project_path = os.getcwd()
databases_file_path = project_path + r'\system\databases.txt'

def is_database_exist(dbname, databases_path = databases_file_path):
    if object_in_file_list(obj = dbname, file_path = databases_path):
        return True
    return False