from priority_queue import PriorityQueue
from time import time,sleep
import threading
from random import random
from van_emde_sat import VanEmdeTreeSat
from sync import synchronized

vhm = 0
u = 2**13

start_time = time()

serviced_a_count = None
serviced_r_count = None
sample_count = None

a_count = None
r_count = None

@synchronized
def test_sample(address=-1):
	global serviced_a_count, serviced_r_count, sample_count
	if address == -1:
		if serviced_a_count + serviced_r_count < sample_count:
			return True
		else:
			return False
	
	if serviced_a_count + serviced_r_count < sample_count:
		if address < 2000:
			serviced_r_count += 1
			return True
		else:
			serviced_a_count += 1
			return True
	else:
		return False

def set_vhm(v):
	global vhm
	vhm = v

def get_data():
	global serviced_a_count, serviced_r_count, a_count, r_count
	return {
		'serviced'	: {
			'attacker'	: serviced_a_count,
			'regular'	: serviced_r_count
		},
		'total'		: {
			'attacker'	: a_count,
			'regular'	: r_count
		}
	}

@synchronized
def log_req_data(address):
	global a_count, r_count
	if address < 2000:
		r_count += 1
	else:
		a_count +=1


db = None
# db.init_sat()

low_priority_queue = None
high_priority_queue = None

def setup_demo():
	global u, start_time, serviced_a_count, serviced_r_count, sample_count, \
		a_count, r_count, db, low_priority_queue, high_priority_queue
	u = 2**13

	start_time = time()

	serviced_a_count = 0
	serviced_r_count = 0
	sample_count = 1000

	a_count = 0
	r_count = 0
	db = VanEmdeTreeSat(u)
	db.init_sat()

	low_priority_queue = PriorityQueue(u)
	high_priority_queue = PriorityQueue(u)
	

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
	return int(u * t/10)


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
		# print(address,diff)
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
	if test_sample(e):
		# print("servicing", e, serviced_a_count, serviced_r_count)
		pass

def service_request():
	while test_sample():
		e = high_priority_queue.extract_max()

			
		if e == None: 
			#print("Nothing to process")
			sleep(0.2)
			continue
		service(e)

def traffic_controller():
	while test_sample():
		sleep(1)
		#print("hello traffic")
		e = low_priority_queue.extract_max()
		if e != None: high_priority_queue.insert(priority(random()),e)

def client(freq,address):
	global a_count, r_count
	t = 1/freq
	while a_count + r_count < sample_count:
		sleep(random()/freq + t)
		if test_sample():
			log_req_data(address)
			listener(address)
		else:
			break










