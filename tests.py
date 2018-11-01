from van_emde import VanEmdeTree
from random import randint
from time import time

u = 2 ** 24
cases = 2 ** 20

def insertion_and_membership_test():
	global u,cases
	print("------insertion and membership test------")

	s = set()
	t = time()
	a = VanEmdeTree(u)
	t = time() - t
	print("Tree made in {} seconds".format(t))
	t = time()
	for i in range(cases):
		r = randint(0,u-1)
		s.add(r)
		a.insert(r)

	for i in range(cases):
		r = randint(0,u-1)
		if (r in s and a.member(r)) or (r not in s and not a.member(r)):
			pass
		else:
			print("fault")
			return
	t = time() - t
	print("test for {} cases passed in {} seconds".format(cases,t))

def deletion_test():
	global u,cases
	
	print("---------deletion test----------")
	t = time()
	a = VanEmdeTree(u)
	t = time() - t
	print("Tree made in {} seconds".format(t))

	s = set()
	t = time()
	for i in range(cases):
		r = randint(0,u-1)
		if r in s and a.member(r):
			s.remove(r)
			a.delete(r)
		elif r not in s and not a.member(r):
			s.add(r)
			a.insert(r)
		else:
			print("fault")
			return
	t = time() - t
	print("test for {} cases passed in {} seconds".format(cases,t))

def __successor(l,r):  #very_slow
	l = list(l)
	l.sort()
	index = l.index(r)
	for i in range(index+1,len(l)):
		if l[i] != r:
			return l[i]
	return None

def __predecessor(l,r):  #very_slow
	l = list(l)
	l.sort()
	l.reverse()
	index = l.index(r)
	for i in range(index+1,len(l)):
		if l[i] != r:
			return l[i]
	return None

def successor_and_predecessor_test():
	global u,cases

	print("----------successor and predecessor test---------")
	t = time()
	a = VanEmdeTree(u)
	t = time() - t
	print("Tree made in {} seconds".format(t))
	
	s = set()
	t = time()
	for i in range(int(cases**0.5)):
		r = randint(0,u-1)
		if r in s and a.member(r):
			if a.successor(r) != __successor(s,r):
				print("succ fault")
			if a.predecessor(r) != __predecessor(s,r):
				print("pred fault")

		elif r not in s and not a.member(r):
			s.add(r)
			a.insert(r)
		else:
			print("fault")
	t = time() - t
	print("test for {} cases passed in {} seconds".format(int(cases**0.5),t))
	
def main():
	insertion_and_membership_test()
	deletion_test()
	successor_and_predecessor_test()


if __name__ == "__main__":
	main()