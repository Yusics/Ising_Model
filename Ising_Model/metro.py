from __future__ import division
import numpy as np
from PIL import Image
import scipy.misc as smp
import matplotlib.pyplot as plt
import sys


class Ising(object):
	def __init__(self):
		self.column  = int(sys.argv[1])
		self.row     = int(sys.argv[2])
		self.temp    = 0.01
		self.beta    = 1/self.temp
		self.J       = 1
		self.field_B = 0
		self.lattice = np.ones((self.column , self.row))

	def metro(self):
		flip = np.random.randint(self.column, size=2)
		self.flip_spin(flip[0], flip[1])
		change = self.eneryChange(flip[0], flip[1])
		self.a_prob(change, flip[0], flip[1])


	def flip_spin(self, idx_r, idx_c):
		self.lattice[idx_r][idx_c] *= -1

	def eneryChange(self, idx_r, idx_c):


		change = 2*self.lattice[idx_r][idx_c]*(-1)*self.J
		sum_spin = 0

		spin_list = []

		for i in xrange(-1,3,2):
			for j in xrange(-1,3,2):
				sp = []
				col = (idx_c+i)%self.column
				row = (idx_r+j)%self.row
				sp.append(col)
				sp.append(row)
				spin_list.append(sp)

	
		for i in range(4):
			sum_spin += self.lattice[spin_list[i][0]][spin_list[i][1]]


		change *= sum_spin


		return change + 2*self.field_B*self.lattice[idx_r][idx_c]*(-1)


	def a_prob(self, change, idx_r, idx_c):

		if change > 0:

			rand = np.random.rand()
		
			if rand >= np.exp(-self.beta*change):
				
				self.lattice[idx_r][idx_c] *= -1
		
	def energy(self):
		total_E = 0

		for i in range(self.row):
			for j in range(self.column):
				spin_list = []
				sum_spin = 0
				for r1 in xrange(-1,3,2):
					for r2 in xrange(-1,3,2):
						sp = []
						col = (i + r1)%self.column
						row = (j + r2)%self.row
						sp.append(col)
						sp.append(row)
						spin_list.append(sp)

				for r in range(4):	
					sum_spin += self.lattice[spin_list[r][0]][spin_list[r][1]]
					

				total_E -= sum_spin*self.lattice[i][j]

		return total_E

	def draw_image(self):
		im = np.zeros((self.column, self.row, 3))
		for i in range(self.column):
			for j in range(self.row):
				if self.lattice[i][j] != 1:
					im[i][j][0] = 255
					im[i][j][1] = 255
					im[i][j][2] = 255

		return im


ising = Ising()

mag = []
T   = []
time = []

for t in np.arange(1.5 , 3.5, 0.1):

	#print ising.lattice
	#exit()

	print t 
	T.append(t)
	ising.temp = t
	ising.beta = 1/t

	for i in range(2000000):
		
		ising.metro()
		
	mm = abs(np.sum(ising.lattice)/(ising.column*ising.row))
	mag.append(mm)



fig = plt.figure()
plt.plot(T, mag, 'ro')
plt.suptitle('m-T J=%d' % ising.J, fontsize=24)
plt.xlabel('Temp T(K)', fontsize=18)
plt.ylabel('magnetization m', fontsize=18)


plt.show()


print mag




