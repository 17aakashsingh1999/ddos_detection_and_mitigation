from van_emde import VanEmdeTree
from random import randint

def ins_and_mem_test():
	u = 2**10
	s = set()
	a = VanEmdeTree(u)
	for i in range(100000):
		s.add(randint(0,u-1))

	for i in s:
		a.insert(i)

	for i in range(1000000):
		r = randint(0,u-1)
		if r in s and a.member(r):
			pass
		else:
			print("fault")
			break

def ff():
	u = 2**10
	a = VanEmdeTree(u)
	print("made tree")
	s = set()
	b=set()
	for i in range(u):
		r = randint(0,100)
		if r in s and a.member(r):
			s.remove(r)
			a.delete(r)
		elif r not in s and not a.member(r):
			s.add(r)
			a.insert(r)
			b.add(r)
		else:
			print("fault",i,r,r in s,a.member(r),r in b)
			break
def ins():
	a = VanEmdeTree(2**4)
	a.insert(2)
	print("done insert")
	a.member(2)
	a.insert(3)
	print("done insert")
	a.member(3)
	
#ins()
ins_and_mem_test()
print("comp")
ff()
print("comp")