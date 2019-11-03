def u22k(u):
	k = 0
	while True:
		v = 2 ** (2 ** k)
		if v >= u:
			return v
		k += 1

def sqrt(u):
	return int(u ** 0.5)

class ProtoVanEmdeTree:
	def __init__(self,u):
		self.u = u22k(u)
		if self.u != 2:
			self.summary = ProtoVanEmdeTree(sqrt(self.u))
			self.cluster = [ProtoVanEmdeTree(sqrt(self.u)) for i in range(sqrt(self.u))]
		if self.u == 2: self.A = [0,0]


	def high(self,x):
		return x // sqrt(self.u)

	def low(self,x):
		return x % sqrt(self.u)

	def index(self,x,y):
		return x * sqrt(self.u) + y

	def is_member(self,x):
		if self.u == 2:
			return self.A[x]
		return self.cluster[self.high(x)].is_member(self.low(x))

	def minimum(self):
		if self.u == 2:
			if self.A[0] == 1:
				return 0
			elif self.A[1] == 1:
				return 1
			else:
				return None
		else:
			min_cluster = self.summary.minimum()
			if min_cluster == None:
				return None
			else:
				offset = self.cluster[min_cluster].minimum()
				return self.index(min_cluster,offset)

	def maximum(self):
		if self.u == 2:
			if self.A[1] == 1:
				return 1
			elif self.A[0] == 1:
				return 0
			else:
				return None
		else:
			max_cluster = self.summary.maximum()
			if max_cluster == None:
				return None
			else:
				offset = self.cluster[max_cluster].maximum()
				return self.index(max_cluster,offset)

	def successor(self,x):
		if self.u == 2:
			if x == 0 and self.A[1] == 1:
				return 1
			else:
				return None
		else:
			offset = self.cluster[self.high(x)].successor(self.low(x))
			if offset != None:
				return self.index(self.high(x),offset)
			else:
				successor_cluster = self.summary.successor(self.high(x))
				if successor_cluster == None:
					return None
				else:
					offset = self.cluster[successor_cluster].minimum()
					return self.index(successor_cluster,offset)

	def predecessor(self,x):
		if self.u == 2:
			if x == 1 and self.A[0] == 1:
				return 0
			else:
				return None
		else:
			offset = self.cluster[self.high(x)].predecessor(self.low(x))
			if offset != None:
				return self.index(self.high(x),offset)
			else:
				predecessor_cluster = self.summary.predecessor(self.high(x))
				if predecessor_cluster == None:
					return None
				else:
					offset = self.cluster[predecessor_cluster].maximum()
					return self.index(predecessor_cluster,offset)

	def insert(self,x):
		if self.u == 2:
			self.A[x] = 1
		else:
			self.cluster[self.high(x)].insert(self.low(x))
			self.summary.insert(self.high(x))

	def delete(self,x):
		pass

def main():
	a = ProtoVanEmdeTree(16)
	a.insert(2)
	print(a.is_member(2))
	a.insert(4)
	print("predecessor",a.predecessor(15))
	print(a.is_member(4))
	print("min",a.minimum())
	print("max",a.maximum())
	print(a.u)

if __name__ == "__main__":
	main()






