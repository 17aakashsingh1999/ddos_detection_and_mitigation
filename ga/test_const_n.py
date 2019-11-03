from van_emde import VanEmdeTree
from random import randint
from time import time
cases = 200000

def insertion_and_membership_test(u, insert_mem_list):
	#print("------insertion and membership test------")
	global cases
	s = set()
	t = time()
	a = VanEmdeTree(u)
	t = time() - t
	#print("Tree made in {} seconds".format(t))
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
	#print("test for {} cases passed in {} seconds".format(cases,t))
	insert_mem_list.append(t)

def deletion_test(u, del_list):
	global cases	
	#print("---------deletion test----------")
	t = time()
	a = VanEmdeTree(u)
	t = time() - t
	#print("Tree made in {} seconds".format(t))

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
	#print("test for {} cases passed in {} seconds".format(cases,t))
	del_list.append(t)

#def __successor(l,r):  #very_slow
#	l = list(l)
#	l.sort()
#	index = l.index(r)
#	for i in range(index+1,len(l)):
#		if l[i] != r:
#			return l[i]
#	return None
#
#def __predecessor(l,r):  #very_slow
#	l = list(l)
#	l.sort()
#	l.reverse()
#	index = l.index(r)
#	for i in range(index+1,len(l)):
#		if l[i] != r:
#			return l[i]
#	return None
#
#def successor_and_predecessor_test():
#	global u,cases
#
#	print("----------successor and predecessor test---------")
#	t = time()
#	a = VanEmdeTree(u)
#	t = time() - t
#	print("Tree made in {} seconds".format(t))
#	
#	s = set()
#	t = time()
#	for i in range(int(cases**0.5)):
#		r = randint(0,u-1)
#		if r in s and a.member(r):
#			if a.successor(r) != __successor(s,r):
#				print("succ fault")
#			if a.predecessor(r) != __predecessor(s,r):
#				print("pred fault")
#
#		elif r not in s and not a.member(r):
#			s.add(r)
#			a.insert(r)
#		else:
#			print("fault")
#	t = time() - t
#	print("test for {} cases passed in {} seconds".format(int(cases**0.5),t))
	
def get_time():
	u = [2 ** i for i in range(1,24)]
	del_list = []
	insert_mem_list = []
	for i in range(len(u)) :
		print('for u : ', u[i])
		insertion_and_membership_test(u[i], insert_mem_list)
		deletion_test(u[i], del_list)
		#successor_and_predecessor_test()
	return insert_mem_list, del_list
