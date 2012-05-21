#!/usr/bin/python
# -*- coding: utf8 -*-


import os
from tools.tools import get_object_from_file_append_to_list

secret_file_path = os.getcwd() + r'\system\user_secret.txt'

def secret_check(user,secret,secret_file = secret_file_path): 
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


