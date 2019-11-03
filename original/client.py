from random import random
from time import sleep

def client(freq,address):
	t = 1/freq
	while True:
		sleep(random() + t)
		listener(address)
		print("call",address)


