
import os


PROJECT_PATH = os.getcwd()
DATABASE_PATH = PROJECT_PATH + r'\databases'
DATABASE_FILE_PATH = PROJECT_PATH + r'\system\databases.txt'
SECRET_FILE_PATH = PROJECT_PATH  + r'\system\user_secret.txt'

TABLES_NAME_FILE = 'tables.txt'
TABLE_INFO_FILE_SUFFIX = r'_info.txt'

global CURRENT_DB
CURRENT_DB = None