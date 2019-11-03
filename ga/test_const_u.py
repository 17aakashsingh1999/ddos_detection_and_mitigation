from van_emde import VanEmdeTree
from random import randint
from time import time
u = 2 ** 20

def insertion_and_membership_test(cases, insert_mem_list):
	global u
	#print("------insertion and membership test------")

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

def deletion_test(cases, del_list):
	
	global u
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
	cases = [1000 * i for i in range(100)]
	del_list = []
	insert_mem_list = []
	for i in range(len(cases)) :
		print('case : ', i)
		insertion_and_membership_test(cases[i], insert_mem_list)
		deletion_test(cases[i], del_list)
		#successor_and_predecessor_test()
	return insert_mem_list, del_list
