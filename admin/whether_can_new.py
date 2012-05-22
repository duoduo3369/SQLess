from models.tables import Row,Table

#def whether_can_new_table_object(table_name,rows):
#    row_list = []
#    for row in rows:
#        if len(row) == 2:
#            r = Row(row[0],row[1])            
#        elif len(row) == 3:
#            r = Row(row[0],row[1],row[2])            
#        else :
#            return False
#        if r.clean_data():
#            row_list.append(r)
#        else:
#            print 'You input near rows was wrong.'
#            return False
#        
#    table = Table(table_name,row_list)
#    if not table.clean_data():
#        print 'You input near table was wrong.'
#        return False
#    
#    return True
def create_new_row_object(row):
    if len(row) == 2:
        r = Row(row[0],row[1])            
    elif len(row) == 3:
        r = Row(row[0],row[1],row[2])            
    else :
        return None
    if r.clean_data():
        return r
    else :
        return None
    
def whether_can_new_table_object(table_name,rows):
    row_list = []
    for row in rows:
        r = create_new_row_object(row)
        if r is not None:
            row_list.append(r)
        else:
            print 'You input near rows was wrong.'
            return False
        
    table = Table(table_name,row_list)
    if not table.clean_data():
        print 'You input near table was wrong.'
        return False
    
    return True