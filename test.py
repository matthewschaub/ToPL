from el import *
from size import size

e1 = AndExpr(NotExpr(BoolExpr(True)), 
	BoolExpr(False))

e2 = BoolExpr(True)

print(size(e1))