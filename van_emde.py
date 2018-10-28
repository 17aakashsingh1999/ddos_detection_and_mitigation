from math import floor,ceil,log

def u2k(u):
	return 2 ** ceil(log(u,2))

def u_root(u):
	return 2 ** ceil(log(u,2)/2.0)

def l_root(u):
	return 2 ** floor(log(u,2)/2.0)

class VanEmdeTree:
	def __init__(self,u):  # perfect
		self.u = u2k(u)
		self.min = None
		self.max = None
		if self.u != 2:
			self.summary = VanEmdeTree(u_root(self.u))
			self.cluster = [VanEmdeTree(l_root(self.u)) for _ in range(u_root(self.u))]

	#def __str__(self):
	#	return f"u: {self.u}, min: {self.min}, max: {self.max}"

	def high(self,x):  #perfect
		return floor(x/l_root(self.u))

	def low(self,x):  #perfect
		return x % l_root(self.u)

	def index(self,x,y):  #perfect
		return x * l_root(self.u) + y

	def maximum(self):  #perfect
		return self.max

	def minimum(self):  #perfect
		return self.min

	def member(self,x):  #perfect
		#print(self)
		if x == self.min or x == self.max:
			return True
		elif self.u == 2:
			return False
		else:
			#print(f"{self.u} running else")
			return self.cluster[self.high(x)].member(self.low(x))

	def successor(self,x):  #perfect
		if self.u == 2:
			if x == 0 and self.max == 1:
				return 1
			else:
				return None
		elif self.min != None and x < self.min:
			return self.min
		else:
			max_low = self.cluster[self.high(x)].maximum()
			if max_low != None and self.low(x) < max_low:
				offset = self.cluster[self.high(x)].successor(self.low(x))
				return self.index(self.high(x),offset)
			else:
				successor_cluster = self.summary.successor(self.high(x))
				if successor_cluster == None:
					return None
				else:
					offset = self.cluster[successor_cluster].minimum()
					return self.index(successor_cluster,offset)

	def predecessor(self,x):  #perfect
		if self.u == 2:
			if x == 1 and self.min == 0:
				return 0
			else:
				return None
		elif self.max != None and x > self.max:
			return self.max
		else:
			min_low = self.cluster[self.high(x)].minimum()
			if min_low != None and self.low(x) > min_low:
				offset = self.cluster[self.high(x)].predecessor(self.low(x))
				return self.index(self.high(x),offset)
			else:
				predecessor_cluster = self.summary.predecessor(self.high(x))
				if predecessor_cluster == None:
					if self.min != None and x > self.min:
						return self.min
					else:
						return None
				else:
					offset = self.cluster[predecessor_cluster].maximum()
					return self.index(predecessor_cluster,offset)

	def empty_insert(self,x):  #perfect
		self.max = x
		self.min = x

	def insert(self,x):  #perfect
		if self.min == None:
			self.empty_insert(x)
		elif x < self.min:
			self.min, x = x, self.min
		if self.u > 2:
			if self.cluster[self.high(x)].minimum() == None:
				self.summary.insert(self.high(x))
				self.cluster[self.high(x)].empty_insert(self.low(x))
			else:
				self.cluster[self.high(x)].insert(self.low(x))
		if x > self.max:
			self.max = x

	def delete(self,x):
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
			else:
				self.max = self.index(self.high(x),self.cluster[self.high(x)].maximum())
