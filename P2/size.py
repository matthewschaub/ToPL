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
		return 1 + max(height(e.lhs), height(e.rhs))

def same(e1, e2): #Return true if two expressions are identical
	assert isinstance(e1, Expr)
	assert isinstance(e2, Expr)
	if isinstance(e1, BoolExpr) and isinstance(e2, BoolExpr):
		return e1 == e2
	elif isinstance(e1, NotExpr) and isinstance(e2, NotExpr):
		return same(e1.expr, e2.expr)
	elif isinstance(e1,BinaryExpr) and isinstance(e2,BinaryExpr):
		return same(e1.lhs, e2.lhs) and same(e1.rhs, e2.rhs)
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

def is_value(e):
	return type(e) is BoolExpr

def is_reducible(e):
	return not isinstance(e, BoolExpr)

def step_not(e):
	if isinstance(e.expr, BoolExpr): #if is_value(e.expr): (alternative)
		if e.expr.value == True:
			return BoolExpr(False)
		else: 
			return BoolExpr(True)
	return(e.expr)

def step_and(e):
	if isinstance(e.lhs, BoolExpr) and isinstance(e.rhs, BoolExpr):
		return BoolExpr(value(e.lhs) and value(e.rhs))
	if is_reducible(e.lhs):
		return AndExpr(step(e.lhs), e.rhs)
	if is_reducible(e.rhs):
		return AndExpr(e.lhs, step(e.rhs))

def step_or(e):
	if isinstance(e.lhs, BoolExpr) and isinstance(e.rhs, BoolExpr):
		return BoolExpr(value(e.lhs) or value(e.rhs))
	if is_reducible(e.lhs):
		return OrExpr(step(e.lhs), e.rhs)
	if is_reducible(e.rhs):
		return OrExpr(e.lhs, step(e.rhs))

def step(e): #Return an expression representing a single step of evaluation
	assert isinstance(e, Expr)
	assert is_reducible(e)
	if isinstance(e, NotExpr):
		return step_not(e)

	if isinstance(e, AndExpr):
		return step_and(e)

	if isinstance(e, OrExpr):
		return step_or(e)

	if isinstance(e, AppExpr):
		return step_app(expr)

def step_app(e):
	if is_reducible(e.lhs): # App-1
    return AppExpr(step(e.lhs), e.rhs)

  if type(e.lhs) is not AbsExpr:
    raise Exception("Non Lambda type")

  if is_reducible(e.rhs): # App-2
    return AppExpr(e.lhs, step(e.rhs))

  s = {
    e.lhs.var: e.rhs
  }
  return subst(e.lhs.expr, s);

  def resolve(e, scope = []):
  if type(e) is AppExpr:
    resolve(e.lhs, scope)
    resolve(e.rhs, scope)
    return

  if type(e) is AbsExpr:
    resolve(e.expr, scope + [e.var])
    return

  if type(e) is IdExpr:
    for var in reversed(scope):
      if e.id == var.id:
        e.ref = var 
    raise Exception("name lookup error")

  assert False



def subst(e,s):
	assert isinstance(e,Expr), "Expression type required"
	
	if e.is_a(IdExpr):
		if e.ref in s:
			return s[e.ref]
		else:
			return e

	if isinstance(e,AbsExpr):
		return AbsExpr(e.var,subst(e.expr,s))

	if isinstance(e,AppExpr):
		return AppExpr(subst(e.e1,s), subst(e.e2,s))


def reduce(e):#Calls step repeatedly until the expression is non-reducible
	print(e)
	while is_reducible(e):
		e = step(e)
		print(e)
	return e