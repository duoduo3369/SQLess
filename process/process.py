import sys
from admin.login import login

def run_script():
    print 'loading..'
    len_argv = len(sys.argv)
    if len_argv == 1:
        return login()
    elif len_argv == 2:
        return login(sys.argv[1])
    elif len_argv == 3:
        return login(sys.argv[1],sys.argv[2])
    else: 
        print 'user name or password error'
        return False


from tools.parse import string_to_token

CURRENT_DB = None
def running(RUNNING_FLAG = False):
    RUNNING_FLAG =run_script()
    while RUNNING_FLAG:
        input_string  = raw_input()
        input_string = input_string.lower()
        if input_string == 'quit':
            RUNNING_FLAG = False
        else:
            token = string_to_token(input_string)
            if admin_choice(token):
                print 'Mission successed!'
            else:
                print 'Mission failed!'

from admin.create import use_database
def admin_choice(token):
    len_token = len(token)
    if type(token) != type([]) or len_token < 2:
        print 'Your input was wrong'
        return False

    admin_type = token[0]
    
    # only type 'use database_name'
    if len_token == 2:
        if admin_type == 'use':
            flag = use_database(token[1].lower())
            if flag is None:
                return False
            else:
                global CURRENT_DB
                CURRENT_DB = flag             
                return True
    elif admin_type == 'create':
        return admin_create_choice(token)
    
    print 'Your input was wrong.'
    return False

from admin.create import create_database,create_table
from tools.parse import  parsing_token_with_create_table_to_rows

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
        if rows is None:
            return False
        else:
            return create_table(database_name = CURRENT_DB,table_name = name,rows = rows)
    else:
        print 'Your input was wrong, near create ...'
        return False