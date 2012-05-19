
import os
import shutil
from tools.tools import object_in_file_list,get_object_from_file_extend_to_list,write_to_file

project_path = os.getcwd()
db_file_path = project_path + r'\databases'
db_sys_file_path = project_path + r'\system\databases.txt'

def drop_database(database_name,databases_systemfile_path = db_sys_file_path):
    if not object_in_file_list(obj = database_name , file_path = databases_systemfile_path):
        print 'The database had not exists!\nCheck you input'
        return False
    
    database_path = db_file_path + ( r'\%s' % database_name)
    
    try:
        shutil.rmtree(database_path)
    except:
        print 'Drop error!'
        return False
    
    databases = get_object_from_file_extend_to_list(databases_systemfile_path)
    after_drop_databases = [db for db in databases if db != database_name]
    databases = '\n'.join(after_drop_databases)
    write_to_file(string = databases,file_path = databases_systemfile_path)
    
    return True
    