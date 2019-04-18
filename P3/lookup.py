from lang import *

def lookup(id, stk):
  for scope in reversed(stk):
    if id in scope:
      return scope[id]
  return None

def resolve(e, stk = []):
  if type(e) is BoolExpr:
    return e

  if type(e) is AndExpr:
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e 

  if type(e) is OrExpr:
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e 

  if type(e) is NotExpr:
    resolve(e.expr, stk)
    return e

  if type(e) is IfExpr:
    resolve(e.cond, stk)
    resolve(e.true, stk)
    resolve(e.false, stk)
    return e

  if type(e) is IdExpr:
    decl = lookup(e.id, stk)
    if not decl:
      raise Exception("name lookup error")

    e.ref = decl
    return e

  if type(e) is AbsExpr:
    resolve(e.expr, stk + [{e.var.id : e.var}])
    return e

  if type(e) is AppExpr:
    resolve(e.lhs, stk)
    resolve(e.rhs, stk)
    return e

  if type(e) is LambdaExpr:
    resolve(e.expr, stk + [{var.id : var for var in e.vars}])
    return e

  if type(e) is CallExpr:
    resolve(e.fn, stk)
    for a in e.args:
      resolve(e.fn, stk)
    return e

  assert False
