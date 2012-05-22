
from admin.create import create_table


def test_datebase_function(f):
    database_name = raw_input('please input the name of database> ')
    while not f(database_name):
        database_name = raw_input('please input the name of database >')
        
def test_create_table():
    database_name = '1'
    table_name = 'first_table'
    rows = [['a','int'],['b','varchar']]
    create_table(database_name,table_name,rows)
    
from admin.exist import is_table_exist
def test_is_table_exist():
    database_name = 'a'
    table_name = 'a'
    print is_table_exist(database_name,table_name)
    table_name = 'b'
    print is_table_exist(database_name,table_name)
    raw_input('>')

from admin.advance import show_tables
def test_show_tables():
    database_name = 'a'
    show_tables(database_name)
    database_name = 'b'
    show_tables(database_name)
    raw_input('>')