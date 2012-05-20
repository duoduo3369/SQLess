#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
sys.path.append(r'.')

from admin.login import run_script
from admin.create import create_database,create_table
from admin.drop import drop_database
def test_datebase_function(f):
    database_name = raw_input('please input the name of database> ')
    while not f(database_name):
        database_name = raw_input('please input the name of database >')
def test_create_table():
    database_name = '1'
    table_name = 'first_table'
    rows = [['a','int'],['b','varchar']]
    create_table(database_name,table_name,rows)
    
def main():
    #run_script()
    #test_datebase_function(create_database)
    test_create_table()

if __name__ == '__main__':
    main()

