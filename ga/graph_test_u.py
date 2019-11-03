import numpy as np 
from matplotlib import pyplot as plt 
from test_const_n import *

def plot_van_emde_vs_priority_queue() :
	x = [2 ** i for i in range(1,24)]
	y, z = get_time()
	plt.title('')
	plt.xlabel('Universe Size')
	plt.ylabel('Time')
	plt.plot(x, y, label='Insert and Membership Test')
	plt.plot(x, z, label='Deletion Test')
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
	print(x,y)
	print(x,z)
	plt.show()


plot_van_emde_vs_priority_queue()