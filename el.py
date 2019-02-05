class Expr:
	pass

class BoolExpr(Expr):
	def __init__(self, val):
		assert val == True or val == False
		self.value = val

class BinaryExpr(Expr):
	def __init__(self, e1, e2):
		assert isinstance(e1, Expr)
		assert isinstance(e2, Expr)
		self.lhs = e1
		self.rhs = e2

class NotExpr(Expr):
	def __init__(self, e):
		assert isinstance(e, Expr)
		self.expr = e; 

class AndExpr(BinaryExpr):
	pass

class OrExpr(BinaryExpr):
	pass
