#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
sys.path.append(r'.')

from process.process import running,run_script
        
def run():
    if run_script():
        running()
 
from test.test import  test_show_tables        
def main():
    run()
    
    

if __name__ == '__main__':
    main()
    