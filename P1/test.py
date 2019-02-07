from el import *
from size import *

e1 = NotExpr(NotExpr(BoolExpr(True)))

e2 = AndExpr(NotExpr(BoolExpr(True)), AndExpr(BoolExpr(False), BoolExpr(True)))
e3 = AndExpr(NotExpr(BoolExpr(True)), AndExpr(BoolExpr(True), BoolExpr(True)))


print(same(e3, e2))