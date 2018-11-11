from listener import *
from threading import Thread

no_of_regular_users = 1000
regular_user_freq = 0.2
no_of_attackers = 10
attacker_freq = 1

def main():

	regular_users = []
	for i in range(no_of_regular_users):
		regular_users.append(Thread(target=client,args=[regular_user_freq,i]))
	attackers = []
	for i in range(no_of_attackers):
		attackers.append(Thread(target=client,args=[attacker_freq,i+2000]))

	server = Thread(target=service_request,args=[])
	traffic_ctrl = Thread(target=traffic_controller,args=[])

	

	for t in regular_users:
		t.start()

	for t in attackers:
		t.start()
	
	server.start()
	traffic_ctrl.start()
	server.join()
	traffic_ctrl.join()


	for t in regular_users:
		t.join()

	for t in attackers:
		t.join()


if __name__ == "__main__":
	main()



