from dhad_AST import VariableAssignment, IfStatement, BinOp, Identifier, Print

def dhad_parser(tokens):
    index = 0
    ast = []

    def parse_expression(index):
        token, value = tokens[index]
        if token == 'VAR':
            var_declaration_keyword = tokens[index][1]

            var_name_keyword = tokens[index+1][1]
            var_name = tokens[index+2][1]

            var_value_keyword = tokens[index+3][1]
            var_value = tokens[index+4][1]

            return index + 5, VariableAssignment(var_name, var_value)
        
        elif token == 'IF':
            if_declaration_keyword = tokens[index][1]

            if_comparison_first_side = tokens[index+1][1]

            if_comparator_token = tokens[index+2][0]

            arithmetic_comparator = ""
            if if_comparator_token == "EQ_COMPARE":
                arithmetic_comparator = "=="

            if_comparison_second_side = tokens[index+3][1]
            
            if_do_keyword = tokens[index+4][1]

            if_body_first_bracket = tokens[index+5][1]

            # Find the end of the IF body (matching 'RBRACE')
            if_body = []
            index += 6  # Move past 'LBRACE'
            
            while tokens[index][0] != "RBRACE":
                index, stmt = parse_expression(index)
                if_body.append(stmt)
            
            # Skip past 'RBRACE'
            index += 1

            return index, IfStatement(if_comparison_first_side, arithmetic_comparator, if_comparison_second_side, if_body)

        elif token == 'PREASSIGN':
            preassign_keyword = tokens[index][1]

            var_name = tokens[index + 1][1]

            postassign_keyword = tokens[index + 2][1]

            var_value = tokens[index + 3][1]

            return index + 4, VariableAssignment(var_name, var_value)

        elif token == 'PRINT':
            var_name = tokens[index + 1][1]
            return index + 2, Print(var_name)
        
        else:
            return index, Identifier(value)

    while index < len(tokens):
        index, expr = parse_expression(index)
        ast.append(expr)
    
    return ast