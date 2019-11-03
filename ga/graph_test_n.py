import numpy as np 
from matplotlib import pyplot as plt 
from test_const_u import *

def plot_van_emde_vs_priority_queue() :
	x = [1000 * i for i in range(100)]
	y, z = get_time()
	plt.title('')
	plt.xlabel('Cases')
	plt.ylabel('Time')
	plt.plot(x, y, label='Insert and Membership Test')
	plt.plot(x, z, label='Deletion Test')
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	plt.show()

plot_van_emde_vs_priority_queue()