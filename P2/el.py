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

class NotExpr(Expr):
	def __init__(self, e):
		assert isinstance(e, Expr)
		self.expr = e;
	def __str__(self):
		return "(Not " + str(self.expr) + ")"

class BinaryExpr(Expr):
	def __init__(self, e1, e2):
		assert isinstance(e1, Expr)
		assert isinstance(e2, Expr)
		self.lhs = e1
		self.rhs = e2

class AndExpr(BinaryExpr):
	def __str__(self):
		return "(" + str(self.lhs) + " And " + str(self.rhs) + ")"

class OrExpr(BinaryExpr):
	def __str__(self):
		return "(" + str(self.lhs) + " Or " + str(self.rhs) +")"

class IdExpr(Expr):
	def __init__(self, id):
		self.id = id
		self.ref = None

	def __str__(self):
		return self.id

class VarDecl:
	def __init__(self, id):
		self.id = id

	def __str__(self):
 		return self.id


class AbsExpr(Expr):
  def __init__(self, var, e1):
    if type(var) is str:
      self.var = VarDecl(var)
    else:
      self.var = var
    self.expr = e1

  def __str__(self):
    return f"\\{self.var}.{self.expr}"

class AppExpr(Expr):
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs

	def __str__(self):
		return f"({self.lhs} {self.rhs})"






