from van_emde import *

class veb_Node(int):
	def set_sat(self,sat):
		self.sat = sat

	def get_sat(self):
		return self.sat

def Node(i,sat=None):
	a = veb_Node(i)
	a.set_sat(sat)
	return a

class VanEmdeTreeSat(VanEmdeTree):
	def __init__(self,u):  # perfect
		self.u = u2k(u)
		self.min = None
		self.max = None
		if self.u != 2:
			self.summary = VanEmdeTreeSat(u_root(self.u))
			self.cluster = [VanEmdeTreeSat(l_root(self.u)) for _ in range(u_root(self.u))]
	def low(self,x):
		if type(x) == veb_Node:
			return Node(x % l_root(self.u),x.get_sat())
		else:
			return x % l_root(self.u)

	def put(self,i,sat):
		super().insert(Node(i,sat))

	def get(self,x):
		if x == self.min:
			return self.min.get_sat()
		elif x == self.max:
			return self.max.get_sat()
		elif self.u > 2:
			return self.cluster[self.high(x)].get(self.low(x))
		else:
			return None