from el import *
from size import *

e1 = AndExpr(NotExpr(BoolExpr(True)), BoolExpr(False))

e2 = AndExpr(NotExpr(BoolExpr(True)), BoolExpr(True))
e3 = AndExpr(NotExpr(BoolExpr(True)), BoolExpr(False))

print(same(e2, e3))