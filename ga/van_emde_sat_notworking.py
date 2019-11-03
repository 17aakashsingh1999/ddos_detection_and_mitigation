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
		#return Node(x % l_root(self.u),x.get_sat())

	def high(self,x):  #perfect
		if type(x) == veb_Node:
			return Node(floor(x/l_root(self.u)),x.get_sat())
		else:
			return floor(x/l_root(self.u))
		#return Node(floor(x/l_root(self.u)),x.get_sat())

	def index(self,x,y):  #perfect
		return x * l_root(self.u) + y

	def put(self,i,sat):
		self.insert(Node(i,sat))

	def insert(self,x):  #perfect
		if self.min == None:
			self.empty_insert(x)
		else:
			if x < self.min:
				self.min, x = x, self.min
			if self.u > 2:
				if self.cluster[self.high(x)].minimum() == None:
					self.cluster[self.high(x)].empty_insert(self.low(x))
					self.summary.insert(self.high(x))
				else:
					self.cluster[self.high(x)].insert(self.low(x))
		if x > self.max:
			self.max = x

	def get(self,x):
		if x == self.min:
			return self.min.get_sat()
		elif x == self.max:
			return self.max.get_sat()
		elif self.u > 2:
			return self.cluster[self.high(x)].get(self.low(x))
		else:
			return None

	def delete(self,x):  #perfect
		data = self.get(x)
		if self.min == self.max:
			self.min = None
			self.max = None
		elif self.u == 2:
			if x == 0:
				self.min = 1
			else:
				self.min = 0
			self.max = self.min
		else:
			if x == self.min:
				first_cluster = self.summary.minimum()
				x = self.index(first_cluster,self.cluster[first_cluster].minimum())
				x = Node(x,data)
				self.min = x
			self.cluster[self.high(x)].delete(self.low(x))
			if self.cluster[self.high(x)].minimum() == None:
				self.summary.delete(self.high(x))
				if x == self.max:
					summary_max = self.summary.maximum()
					if summary_max == None:
						self.max = self.min
					else:
						self.max = self.index(summary_max,self.cluster[summary_max].maximum())
						self.max = Node(self.max,self.get(self.max))
			else:
				if x == self.max:
					self.max = self.index(self.high(x),self.cluster[self.high(x)].maximum())
					self.max = Node(self.max,self.get(self.max))