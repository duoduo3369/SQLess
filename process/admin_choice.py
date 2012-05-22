
from admin.advance import use_database,show_databases,show_tables,desc_table
from tools import default_variable #import CURRENT_DB

def admin_choice(token):
    len_token = len(token)
    if type(token) != type([]) or len_token < 2:
        print 'Your input was wrong'
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
    
    print 'Your input was wrong.'
    return False

from admin.create import create_database,create_table
from tools.parse import  parsing_token_with_create_table_to_rows
from admin.drop import drop_database

def admin_use_choice(token):
    try:
        datebase_name = token[1]
    except:
        print 'Your input was wrong, near use ...'
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
        print 'Your input was wrong, near show ...'
        return False
    if choice_type == 'databases':
        show_databases()
        return True
    elif choice_type == 'tables':
        show_tables(default_variable.CURRENT_DB)
        return True
    else:
        return False

def admin_create_choice(token):
    try:
        choice_type,name = token[1],token[2]
    except:
        print 'Your input was wrong, near create ...'
        return False
    if choice_type == 'database':
            return create_database(name)
    elif choice_type == 'table':
        rows = parsing_token_with_create_table_to_rows(token)
        if rows is None or rows == []:
            print 'Your input was wrong, near create ...'
            return False
        else:
            return create_table(database_name = default_variable.CURRENT_DB,table_name = name,rows = rows)
    else:
        print 'Your input was wrong, near create ...'
        return False
    
def admin_drop_choice(token):
    try:
        choice_type,name = token[1],token[2]
    except:
        print 'Your input was wrong, near drop ...'
        return False
    
    if choice_type == 'database':
            return drop_database(name)
    elif choice_type == 'table':
        return False
    return False

def admin_desc_choice(token):
    try:
        choice_type,name = token[1],token[2]
    except:
        print 'Your input was wrong, near desc ...'
        return False
    if choice_type == 'table':
        table_info = desc_table(database_name = default_variable.CURRENT_DB,table_name = name)
        if table_info is not None:
            return True
    return False