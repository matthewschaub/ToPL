from el import *
from size import *

e1 = AndExpr(NotExpr(BoolExpr(True)), 
	BoolExpr(False))

e2 = OrExpr(BoolExpr(False), BoolExpr(False))
e3 = BoolExpr(True)

print(value(e2))