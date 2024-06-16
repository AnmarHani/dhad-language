
class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Identifier(ASTNode):
    def __init__(self, id_name):
        self.id_name = id_name

class VariableAssignment(ASTNode):
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

class Print(ASTNode):
    def __init__(self, var_name):
        self.var_name = var_name

class IfStatement(ASTNode):
    def __init__(self, first_side, comparator, second_side, body):
        self.first_side = first_side
        self.comparator = comparator
        self.second_side = second_side
        self.body = body
