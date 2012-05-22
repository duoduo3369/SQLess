from tools.tools import append_string_to_file,get_table_info_txt_path
from admin.exist import is_database_exist,is_table_exist,is_row_exist
from whether_can_new import create_new_row_object

def add_row_to_table(database_name, table_name, row):
    if is_database_exist(database_name) == False:
        print 'The database named %s was not exists!' % (database_name)
        return False
    
    if is_table_exist(dbname = database_name,table_name = table_name) == True:
        print 'The table named %s has already exists!' % (table_name)
        return False
    try:
        row_name = row[0]
    except:
        return False
    
    if is_row_exist(database_name, table_name, row_name) == True:
        print 'The row named %s has already exists!' % (row_name)
        return False
    
    table_info_path = get_table_info_txt_path(database_name, table_name)
    row_obj = create_new_row_object(row)
    if row_obj is None:
        print 'Your input was wrong'
        return False
    else:
        row_info = ''
        for r in row:
            row_info += '\t'.join(r)
            row_info += '\n'
        append_string_to_file(row_info,table_info_path)
        return True
    
    return False

