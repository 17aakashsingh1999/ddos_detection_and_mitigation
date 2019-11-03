from priority_queue import PriorityQueue
from time import time,sleep
import threading
from random import random
from van_emde_sat import VanEmdeTreeSat

vhm = 3

start_time = time()


db = VanEmdeTreeSat(2**20)
db.init_sat()

low_priority_queue = PriorityQueue()
high_priority_queue = PriorityQueue()
def test_db(address):
	if db.member(address): 
		#print("ismem")
		q = db.get(address)
	else:
		q = []
	t = time() - start_time
	q.append(t)
	#print("listener1",q)
	if db.member(address): db.remove(address)
	db.put(address,q)
	#print(db.get(address))



def priority(t):
	return int(2**20 * t/10)

def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func


def listener(address):
	global high_priority_queue, low_priority_queue, db, vhm
	if db.member(address): q = db.get(address)
	else:
		q = []
	if len(q) < 3:
		t = time() - start_time
		q.append(t)
		#print("listener1",q)
		db.remove(address)
		db.put(address,q)
		#print(db.get(address))
		p = priority(vhm+random())
		#print("prio",p)
		high_priority_queue.insert(p,address)
	else:
		
		q.append(time() - start_time)
		#print("listener2",q)
		t1 = q[-1]
		t2 = q[-2]
		t3 = q[-3]

		diff = 2/(1/t2 + 1/t1) - 2/(1/t2 + 1/t3)
		#print(address,diff)
		db.remove(address)
		db.put(address,q)
		if diff > vhm:
			#print("low_priority_queue",address,diff)
			high_priority_queue.insert(priority(diff),address)
		else:
			#print("high_priority_queue",address,diff)
			low_priority_queue.insert(priority(diff),address)

def service(e):
	# this function can be used to handle requests
	# currently just printing the address to the console
	print("servicing",e)
	#pass

def service_request():
	while True:
		e = high_priority_queue.extract_max()

			
		if e == None: 
			print("Nothing to process")
			sleep(0.2)
			continue
		service(e)

def traffic_controller():
	while True:
		sleep(1)
		#print("hello traffic")
		e = low_priority_queue.extract_max()
		if e != None: high_priority_queue.insert(priority(random()),e)

def client(freq,address):
	t = 1/freq
	for i in range(10000000):
		sleep(random()/freq + t)
		listener(address)
		#print("client",address)










