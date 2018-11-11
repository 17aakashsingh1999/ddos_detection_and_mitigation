from van_emde import *

class VanEmdeTreeSat(VanEmdeTree):
	def init_sat(self):
		self.satellite_data = [None] * self.u

	def put(self,i,sat):
		if not self.member(i):
			self.insert(i)
			self.satellite_data[i] = sat

	def get(self,x):
		return self.satellite_data[x]

	def remove(self,x):
		if self.member(x):
			self.delete(x)
			self.satellite_data[x] = None
