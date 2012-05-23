from tools.tools import append_string_to_file,get_table_info_txt_path
from tools.tools import get_object_from_file_append_to_list,write_to_file
from admin.exist import is_row_exist,is_db_and_tb_both_exist
from whether_can_new import create_new_row_object

def add_row_to_table(database_name, table_name, row):
    #row like ['a','int']
    if is_db_and_tb_both_exist(database_name, table_name) == False:
        return False
        
    table_info_path = get_table_info_txt_path(database_name, table_name)
    
    #print 'row',row
    row_obj = create_new_row_object(row)
    #print 'row_obj',row_obj
    if row_obj is None:
        #print 'Your input was wrong'
        return False
    else:
        row_name = row[0]
        if is_row_exist(database_name, table_name, row_name ) == True:
            print 'The row named %s has already exists!' % (row_name)
            return False
        
        row_info = ''
        for r in row:
            row_info += r + '\t'
            
        row_info += '\n'
        append_string_to_file(row_info,table_info_path)
        return True
    
    return False

from drop import drop_row
from tools.default_variable import ROW_TUPLE
def drop_row_from_table(database_name, table_name, row_name):
    return drop_row(database_name, table_name, row_name)

def modify_row_from_table(database_name, table_name, row_name,new_type):
    
    if new_type not in ROW_TUPLE:
        return False
    if is_db_and_tb_both_exist(database_name, table_name) == False:
        return False
    if is_row_exist(database_name, table_name, row_name ) == False:
        print 'The row named %s has not exists!' % (row_name)
        return False

    table_info_txt_path = get_table_info_txt_path(database_name, table_name)
    table_info_list = get_object_from_file_append_to_list(table_info_txt_path)
    
    after_modified_info = get_modified_row_string_from_infolist(table_info_list, row_name , new_type)
    
    write_to_file(after_modified_info, table_info_txt_path)
    
    return True

def get_modified_row_string_from_infolist(table_info_list, row_name, new_type):
    after_modified_info = ''
    for row in table_info_list:
        #print 'in drop_row',type(row),len(row),row
        try:
            r_name = row[0]
        except:
            return False                 
        if r_name == row_name:
            row[1] = new_type            
        
        for r in row:
            after_modified_info += r + '\t'   
       
        after_modified_info += '\n'
        
                
    return after_modified_info