#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
sys.path.append(r'.')

from admin.login import run_script
from admin.create import create_database
from admin.drop import drop_database
def main():
    #run_script()
    new_database_name = raw_input('please input the name of database> ')
    while not drop_database(new_database_name):
        new_database_name = raw_input('please input the name of database >')

if __name__ == '__main__':
    main()

