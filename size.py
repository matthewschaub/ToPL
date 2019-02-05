from el import*

def size(e): #compute the size of an expression
	assert isinstance(e, Expr)

	if isinstance(e, BoolExpr):
		return 1

	if isinstance(e, NotExpr): 
		return 1 + size(e.expr)

	if isinstance(e, BinaryExpr): 
		return 1 + size(e.lhs) + size(e.rhs)

def height(e): #compute the height of an expression
	assert isinstance(e, Expr)

	if isinstance(e, BoolExpr):
		return 0;

	if isinstance(e, NotExpr):
		return 1 + height(e.expr)

	if isinstance(e,BinaryExpr):
		return 1 + height(e.lhs) + height(e.rhs)

def same(e1, e2): #Return true if two expressions are identical
	assert isinstance(e1, Expr)
	assert isinstance(e2, Expr)
	if isinstance(e1, BoolExpr) and isinstance(e2, BoolExpr):
		return e1 == e2
	elif isinstance(e1, NotExpr) and isinstance(e2, NotExpr):
		return e1 == e2
	elif isinstance(e1,BinaryExpr) and isinstance(e2,BinaryExpr):
		return e1 == e2
	return False; 

def value(e): #compute the value of an expression
	assert isinstance(e, Expr)

	if isinstance(e, BoolExpr):
		return e.value

	if isinstance(e, NotExpr):
		return not value(e.expr)

	if isinstance(e, AndExpr):
		return value(e.lhs) and value(e.rhs)

	if isinstance(e, OrExpr):
		return value(e.lhs) or value(e.rhs)

	

def step(e): #Return an expression representing a single step of evaluation
	pass


def reduce(e):#Calls step repeatedly until the expression is non-reducible
	pass