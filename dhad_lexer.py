import re
def dhad_lexer(code):
    tokens = []
    token_specification = [
        ('FLOAT',    r'\d+\.\d+'),            # Float number
        ('INT',   r'\d+'),                 # Integer number
        ('VAR',      r'متغير'),               # Variable keyword
        ('VAR_NAME',     r'يسمى'),            # Var Name keyword
        ('VAR_DEF',     r'وقيمته'),           # Var Definition with first assignment (with type) keyword
        ('PREASSIGN',   r'اجعل قيمة'),                   # PRe Assignment Keyword
        ('POSTASSIGN',   r'ب'),                   # Post Assignment Keyword
        ('EQ_COMPARE',       r'يساوي'),               # Comparison "==" Equals keyword
        ('IF',       r'اذا اصبح'),            # If keyword
        ('PRINT',    r'اطبع'),                # Print keyword
        ('DO',       r'فافعل'),               # Do keyword
        ('ID',       r'[ا-ي]+'),              # Identifiers
        ('LBRACE',   r'\{'),                  # Left brace
        ('RBRACE',   r'\}'),                  # Right brace
        ('NEWLINE',  r'\n'),                  # Line endings
        ('SKIP',     r'[ \t]'),               # Skip over spaces and tabs
        ('MISMATCH', r'.'),                   # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'FLOAT':
            value = float(value)
        elif kind == 'INT':
            value = int(value)
        elif kind == 'NEWLINE' or kind == 'SKIP':
            continue  # Ignore newlines and whitespace
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        
        tokens.append((kind, value))
    
    return tokens
