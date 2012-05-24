
All the functin、file struction、process description you can find in the /system/doc.txt ,
but only in Chinese, my english level、、、.

How to use it:

Please run main.py with username and password in the commandline,
like 'python main.py root 123456','main.py root 123456'
Or just double click the main.py. 

The user and password stored in /system/user_secret.txt,default root 123456.

The command you may use,not case sensitive.

USE dbname
SHOW DATABASES
SHOW TABLES (USE db first!)
DESC TALBE tb_name (USE db first!)
CREATE TABLE tb_name (); (USE db first!)
CREATE DATABASE db_name (USE db first!)
ALTER TABLE tb_name ADD () (USE db first!)
ALTER TABLE tb_name DROP tb_name (USE db first!)
ALTER TABLE tb_name MODIFY tb_name new_type (USE db first!)
DROP DATABASE db_name
DROP TABLE tb_name (USE db first!)
QUIT 