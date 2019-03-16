from el import *
from size import *

e1 = AbsExpr("a", "a")

print(VarDecl("b"))
print(IdExpr("x"))
print(AppExpr(e1, IdExpr("a")))
print(e1)