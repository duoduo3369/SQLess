import shlex

def string_to_token(input_string,whitespace = ';',quotes = '|'):
    input_string = input_string.replace(',',' , ')
    lexer = shlex.shlex(input_string)
    lexer.whitespace += whitespace
    lexer.quotes += quotes
    token = [t for t in lexer]
    return token

def token_to_string(token):
    try:
        return ' '.join(token)
    except:
        #print 'Token is not a list'
        return None

def parsing_token_with_create_table_to_rows(token):
    try:
        if token[-2] == ',':
            #print 'The last comma should not input'
            return None
    except:
        #print 'Your input was wrong'
        return None
    
    format_string = token_to_string(token)
    format_string = format_string.replace('(', ' | ')
    format_string = format_string.replace(')', ' | ')
    format_string = format_string.replace(',', ' | | ')
    lexer = shlex.shlex(format_string)
    lexer.quotes = '|'
    format_token = [t for t in lexer]
    #token like ['create', 'table', 'a', '|  a int pk  |', '|  b varchr  |']
     
    if len(format_token) < 3:
        return None
    
    row_tokens = format_token[3:]
    #print 'row token',row_tokens
    rows = []
    for row in row_tokens:
        # row.split() like this ['|', 'a', 'int', 'pk', '|']
        rows.append(row.split()[1:-1])
    return rows

def parsing_token_with_alter_table_to_row(token):
    rows = parsing_token_with_create_table_to_rows(token)
    # rows like [[],[b,int]]
    if rows is not None:
        # rows[1:] like this [['a', 'int']]
        try:
            return rows[1:][0]
        except:
            return None
    return None