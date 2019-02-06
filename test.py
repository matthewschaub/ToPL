from el import *
from size import *

e1 = NotExpr(NotExpr(BoolExpr(True)))

e2 = AndExpr(NotExpr(BoolExpr(True)), OrExpr(BoolExpr(True), BoolExpr(False)))
e3 = AndExpr(NotExpr(BoolExpr(True)), AndExpr(BoolExpr(False), BoolExpr(True)))


reduce(e2)