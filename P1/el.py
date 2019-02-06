class Expr:
	pass


class BoolExpr(Expr):
	def __init__(self, val):
		assert val == True or val == False
		self.value = val
	def __eq__(self, other):
		if isinstance(other, BoolExpr):
			return self.value == other.value 
		return False
	def __str__(self):
		return str(self.value)

class BinaryExpr(Expr):
	def __init__(self, e1, e2):
		assert isinstance(e1, Expr)
		assert isinstance(e2, Expr)
		self.lhs = e1
		self.rhs = e2
	def __eq__(self, other):
		assert isinstance(other, BinaryExpr)
		if isinstance(self, AndExpr) and isinstance(other, AndExpr):
			return self.lhs == other.lhs and self.rhs == other.rhs
		elif isinstance(self, OrExpr) and isinstance(other, OrExpr):
			return self.lhs == other.lhs and self.rhs == other.rhs
		return False;

class NotExpr(Expr):
	def __init__(self, e):
		assert isinstance(e, Expr)
		self.expr = e;
	def __eq__(self, other):
		if isinstance(other, NotExpr):
			return self.expr == other.expr
		return False; 
	def __str__(self):
		return "(Not " + str(self.expr) + ")"

class AndExpr(BinaryExpr):
	def __str__(self):
		return "(" + str(self.lhs) + " And " + str(self.rhs) + ")"

class OrExpr(BinaryExpr):
	def __str__(self):
		return "(" + str(self.lhs) + " Or " + str(self.rhs) +")"
