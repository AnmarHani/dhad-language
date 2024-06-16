from dhad_AST import VariableAssignment, IfStatement, Print, BinOp

class DhadInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, ast):
        for statement in ast:
            if isinstance(statement, VariableAssignment):
                self.handle_variable_assignment(statement)
            elif isinstance(statement, IfStatement):
                self.handle_if_statement(statement)
            elif isinstance(statement, Print):
                self.handle_print_statement(statement)
            else:
                raise RuntimeError("Unknown statement type in AST")

    def handle_variable_assignment(self, assignment):
        var_name = assignment.var_name
        var_value = self.evaluate_expression(assignment.value)
        self.variables[var_name] = var_value


    def handle_if_statement(self, if_statement):
        first_side = self.evaluate_expression(if_statement.first_side)
        second_side = self.evaluate_expression(if_statement.second_side)
        comparator = if_statement.comparator

        if comparator == '==':
            condition = first_side == second_side
        else:
            raise RuntimeError(f"Unsupported comparator: {comparator}")

        if condition:
            for stmt in if_statement.body:
                self.interpret([stmt])  # Recursively interpret nested statements

    def handle_print_statement(self, print_statement):

        var_name = print_statement.var_name
        if var_name in self.variables:
            print(self.variables[var_name])
        else:
            raise RuntimeError(f"Variable '{var_name}' not found")

    def evaluate_expression(self, expr):
        if isinstance(expr, int) or isinstance(expr, float):
            return expr
        elif isinstance(expr, str):
            if expr in self.variables:
                return self.variables[expr]
            else:
                raise RuntimeError(f"Variable '{expr}' not found")
        elif isinstance(expr, BinOp):
            left_val = self.evaluate_expression(expr.left)
            right_val = self.evaluate_expression(expr.right)
            if expr.op == '+':
                return left_val + right_val
            elif expr.op == '-':
                return left_val - right_val
            elif expr.op == '*':
                return left_val * right_val
            elif expr.op == '/':
                return left_val / right_val
            else:
                raise RuntimeError(f"Unsupported operator: {expr.op}")
        else:
            raise RuntimeError("Invalid expression type")
