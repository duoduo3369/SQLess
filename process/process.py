
from admin.login import login_with_infomation,input_login_infomation
from tools.parse import  string_to_token
from tools.tools import sql_input
from admin_choice import admin_choice


def run_script(LOGIN_FLAG = False):
    LOGIN_FLAG, login_times = login_with_infomation(), 1
    
    while not LOGIN_FLAG and login_times < 3:
        print 'Try %s times, you still have %s to login.' % (login_times, 3 - login_times)
        login_infomation = input_login_infomation()  
        LOGIN_FLAG = login_with_infomation(login_infomation)
        if LOGIN_FLAG == True: 
            return True
        login_times += 1
    
    if login_times >= 3:
        print 'Sorry, you may forgot your password, please try later.'
        raw_input('Hint any key to quit.')
        return False
    else:
        return True


def running():  
    RUNNING_FLAG = True
    while RUNNING_FLAG:
        input_string  = sql_input()
        input_string = input_string.lower()
        token = string_to_token(input_string)
        if len(token) == 0 :continue
        
        if token[0] == 'quit':
            RUNNING_FLAG = False
        else:
            if admin_choice(token):
                print 'Mission successed!'
            else:
                print 'Your input was wrong'
                print 'Mission failed!'

