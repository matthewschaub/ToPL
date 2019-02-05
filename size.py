from el import*

def size(e):
	assert isinstance(e, Expr)

	if type(e) is BoolExpr:
		return 1
	if type(e) is NotExpr: 
		return 1 + size(e.expr)
	if isinstance(e, BinaryExpr): 
		return 1 + size(e.lhs) + size(e.rhs)