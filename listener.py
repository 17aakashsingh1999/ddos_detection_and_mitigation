from priority_queue import PriorityQueue
from time import time,sleep
import threading
from random import random
from van_emde_sat import VanEmdeTreeSat


session = None
packets = None
vhm = 0.07

start_time = time()

low_priority_queue = PriorityQueue()
high_priority_queue = PriorityQueue()

db = VanEmdeTreeSat(2**20)


def synchronized(func):
    func.__lock__ = threading.Lock()
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)
    return synced_func

def priority(t):
	return int(2**20 * t / 10)


@synchronized
def listener(address):
	global high_priority_queue, low_priority_queue, db, vhm
	q = db.get(address)
	if q == None:
		q = []
	if len(q) < 3:
		t = time() - start_time
		q.append(t)
		db.delete(address)
		db.put(address,q)
		high_priority_queue.insert(priority(vhm+random()),address)
	else:
		del q[0]
		q.append(time() - start_time)
		t1 = q[2]
		t2 = q[1]
		t3 = q[0]

		diff = 2/(1/t2 + 1/t1) - 2/(1/t2 + 1/t3)
		if diff < vhm:
			high_priority_queue.insert(priority(diff),p)
		else:
			low_priority_queue.insert(priority(diff),p)

def service(e):
	# this function can be used to handle requests
	# currently just printing the address to the console
	print(e.address)

def service_request():
	while True:
		e = high_priority_queue.extract_max()
		print("hello servicereq",e)
		if e == None: 
			sleep(0.2)
			continue
		service(e)

def traffic_controller():
	while True:
		sleep(1)
		print("hello traffic")
		e = low_priority_queue.extract_max()
		high_priority_queue.insert(priority(random()),e)

def client(freq,address):
	t = 1/freq
	while True:
		sleep(random() + t)
		listener(address)
		#print("call",address)










