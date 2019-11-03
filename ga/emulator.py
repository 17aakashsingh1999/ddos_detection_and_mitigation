from diff_demo import *
from threading import Thread

no_of_regular_users = 100
regular_user_freq = 0.1
no_of_attackers = 10
attacker_freq = 10

def emulator(vhm=0):

	set_vhm(vhm)
	setup_demo()

	regular_users = []
	for i in range(no_of_regular_users):
		regular_users.append(Thread(target=client,args=[regular_user_freq,i]))
	attackers = []
	for i in range(no_of_attackers):
		attackers.append(Thread(target=client,args=[attacker_freq,i+2000]))

	server = Thread(target=service_request,args=[])
	# traffic_ctrl = Thread(target=traffic_controller,args=[])

	for t in attackers:
		t.start()

	for t in regular_users:
		t.start()

	
	
	server.start()
	# traffic_ctrl.start()
	server.join()
	# traffic_ctrl.join()


	for t in regular_users:
		t.join()

	for t in attackers:
		t.join()
	data = get_data()
	print('emulator finished', vhm, data)
	return data


if __name__ == "__main__":
	emulator(0.5)



