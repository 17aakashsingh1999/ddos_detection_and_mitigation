from van_emde_sat import *
import threading

def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func


class PriorityQueue:
	def __init__(self,u=2**20):
		self.u = u
		self.veb = VanEmdeTreeSat(u)
		self.veb.init_sat()

	@synchronized
	def insert(self,priority,data):
		if priority < 0 or priority >= self.u:
			pass
		else:
			self.veb.put(priority,data)

	@synchronized
	def extract_max(self):
		if self.veb.minimum() != None:
			m = int(self.veb.maximum())
			r = self.veb.get(m)
			self.veb.delete(m)
			return r
		else:
			return None

	@synchronized
	def extract_min(self):
		if self.veb.minimum() != None:
			m = int(self.veb.minimum())
			r = self.veb.get(m)
			self.veb.delete(m)
			return r
		else:
			return None

def main():
	a = PriorityQueue()
	a.insert(2,[2,3])
	a.insert(3,[3,4])
	print(a.extract_min())
	print(a.extract_min())
	a.insert(2,[2,3])
	a.insert(3,[3,4])
	print(a.extract_max())
	print(a.extract_max())

if __name__ == "__main__":
	main()