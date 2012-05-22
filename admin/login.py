#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from tools.tools import get_object_from_file_append_to_list
from tools.default_variable import SECRET_FILE_PATH
from tools.parse import  string_to_token


def secret_check(user,secret,secret_file = SECRET_FILE_PATH): 
    user = str(user)
    secret = str(secret)   

    records = get_object_from_file_append_to_list(secret_file)
    user_secret_dict = {}
    for record in records:
        user_secret_dict[record[0]] = record[1]
    
    try:
        if user_secret_dict[user] == secret:
            return True
        else:
            return False
    except:        
        return False
    
def login(user = 'root',password = None):
    if secret_check(user,password):
        print 'login sucessful!'
        return True
    else:
        print 'user name or password error'
        return False

def login_with_infomation(info = sys.argv):
    print 'Loading..'
    len_info = len(info)
    if len_info == 1:
        return login()
    elif len_info == 2:
        return login(info[1])
    elif len_info == 3:
        return login(info[1],info[2])
    else: 
        print 'User name or password error'
        return False
 
def input_login_infomation():
    print 'Please input you user name and password:'
    input_info = raw_input('>')
    info = ['SQLess']
    info.extend(string_to_token(input_info))
    return info
