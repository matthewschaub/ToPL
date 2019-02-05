from el import *
from size import *

e1 = AndExpr(NotExpr(BoolExpr(True)), 
	BoolExpr(False))

e2 = BoolExpr(True)

print(height(e1))