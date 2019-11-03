from van_emde_sat import *
from random import randint
from time import time

u = 2 ** 20
cases = 2 ** 20

def satellite_data_test():
	global u,cases
	print("------satellite data test------")

	s = set()
	d = dict()
	t = time()
	a = VanEmdeTreeSat(u)
	t = time() - t
	print("Tree made in {} seconds".format(t))
	t = time()
	for i in range(cases):
		s.add(randint(0,u-1))
	for i in s:
		r = randint(0,u-1)
		d[i] = r
		a.put(i,r)

	for i in s:
		if a.get(i) != d[i]:
			print("fault")
			return
	t = time() - t
	print("test for {} cases passed in {} seconds".format(cases,t))

if __name__ == "__main__":
	satellite_data_test()