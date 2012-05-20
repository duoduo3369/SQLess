
RESTRICTION_TUPLE = (None,'primary key','union')
ROW_TUPLE = ('int','double','text','bolb','varchar','char')
class Base(object):
    def __init__(self,name):
        self.name = name                
        
    def clean_data(self):
        if type(self.name) != type(''):
            return False
        return True
        
class Row(Base):
    def __init__(self, name, row_type, restriction = None):      
        super(Row, self).__init__(name)
        self.row_type = row_type
        self.restriction = restriction
        
    def clean_data(self):
        if super(Row,self).clean_data() == False:
            return False
        if self.row_type.lower() not in ROW_TUPLE:
            return False
        if self.restriction != None:
            if self.restriction.lower() not in RESTRICTION_TUPLE:
                return False
        return True

class Table(Base):
    def __init__(self, name, rows = None):
        super(Table, self).__init__(name)         
        self.rows = rows
                
    def clean_data(self):
        if super(Table,self).clean_data() == False:
            return False
        if type(self.rows) != type([]):
            return False
        for row in self.rows:
            if type(row) != Row:
                return False
        return True
