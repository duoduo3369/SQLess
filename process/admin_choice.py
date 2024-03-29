
from admin.advance import use_database,show_databases,show_tables,desc_table
from tools import default_variable #import CURRENT_DB

def admin_choice(token):
    len_token = len(token)
    if type(token) != type([]) or len_token < 2:
        #print 'Your input was wrong'
        return False

    admin_type = token[0]
    
    # only type 'use database_name'
    if len_token == 2:
        if admin_type == 'use':
            return admin_use_choice(token)
        
        if admin_type == 'show':
            return admin_show_choice(token)
    
    elif admin_type == 'create':
        return admin_create_choice(token)
    
    elif admin_type == 'drop':
        return admin_drop_choice(token)
    elif admin_type == 'desc':
        return admin_desc_choice(token)
    elif admin_type == 'alter':
        return admin_alter_choice(token)
    #print 'Your input was wrong.'
    return False

from admin.create import create_database,create_table
from tools.parse import  parsing_token_with_create_table_to_rows,parsing_token_with_alter_table_to_row
from admin.drop import drop_database,drop_table

def admin_use_choice(token):
    try:
        datebase_name = token[1]
    except:
        #print 'Your input was wrong, near use ...'
        return False        
    dbname = use_database(datebase_name)
    if dbname is None:
        return False
    else:
        default_variable.CURRENT_DB = dbname            
        return True
    
def admin_show_choice(token):
    try:
        choice_type = token[1]
    except:
        #print 'Your input was wrong, near show ...'
        return False
    if choice_type == 'databases':
        show_databases()
        return True
    elif choice_type == 'tables':
        tables = show_tables(default_variable.CURRENT_DB)
        if tables is None:
            return False
        else:
            return True
    else:
        return False

def admin_create_choice(token):
    try:
        choice_type,name = token[1],token[2]
    except:
        #print 'Your input was wrong, near create ...'
        return False
    if choice_type == 'database':
            return create_database(name)
        
    elif choice_type == 'table':
        if  default_variable.CURRENT_DB is None:
            print 'No database select ,please use a database first.'
            return False
        
        rows = parsing_token_with_create_table_to_rows(token)
        if rows is None or rows == []:
            #print 'Your input was wrong, near create ...'
            return False
        else:
            return create_table(database_name = default_variable.CURRENT_DB,table_name = name,rows = rows)
    else:
        #print 'Your input was wrong, near create ...'
        return False
    
from admin.alter import add_row_to_table,drop_row_from_table,modify_row_from_table
def admin_alter_choice(token):
    try:
        choice_type,name,alter_type = token[1],token[2],token[3]
    except:
        #print 'Your input was wrong, near alter ...'
        return False
    if choice_type == 'table':
        if alter_type == 'drop':
            
            try:
                row_name = token[4]
            except:
                return False
            
            return drop_row_from_table(database_name = default_variable.CURRENT_DB,table_name = name, row_name = row_name)
            
        elif alter_type == 'add':
            row = parsing_token_with_alter_table_to_row(token)
            #print rows
            if row is None or row == []:
            #print 'Your input was wrong, near alter ...'
                return False
            else:
                return add_row_to_table(database_name = default_variable.CURRENT_DB,table_name = name,row = row)
        elif alter_type == 'modify':
            #print 'admin_alter_choice: token',token
            try:
                row_name,new_type = token[4], token[5]
            except:
                return False
            return modify_row_from_table(database_name = default_variable.CURRENT_DB, table_name = name,row_name = row_name,new_type = new_type)      
            
    return False
def admin_drop_choice(token):
    try:
        choice_type,name = token[1],token[2]
    except:
        #print 'Your input was wrong, near drop ...'
        return False
    
    if choice_type == 'database':
            return drop_database(name)
    elif choice_type == 'table':        
        return drop_table(default_variable.CURRENT_DB,name)

    return False

def admin_desc_choice(token):
    try:
        choice_type,name = token[1],token[2]
    except:
        #print 'Your input was wrong, near desc ...'
        return False
    if choice_type == 'table':
        table_info = desc_table(database_name = default_variable.CURRENT_DB,table_name = name)
        if table_info is not None:
            return True
    return False