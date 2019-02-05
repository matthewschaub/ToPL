#jvm-like assemb;y languague for propositional calculus  (ie, basic logic)
#
# A program consists of a sequence of instructions
#
# An instruction is one of:
#
# i :: = push <v> (some value) true
#        push false
#        pop 
#        and 
#        or 
#        not
#
# A value is one of True or False

class Instr:
	pass

class Push(Instr)
  def __init__(self, val):
  	self.value = val

class Pop(Instr)
  pass

class And(Instr)
  pass

class Or(Instr)
  pass
  
class Not(Instr)
  pass
