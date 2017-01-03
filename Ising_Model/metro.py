from __future__ import division
import numpy as np
from PIL import Image
import scipy.misc as smp
import matplotlib.pyplot as plt
import sys


class Ising(object):
	def __init__(self):
		self.column  = sys.argv[1]
		self.row     = sys.argv[2]
		self.temp    = 0.01
		self.beta    = 1/self.temp
		self.J       = 1
		self.field_B = 0
		self.prob_v  = 0   
		self.prob_u  = 0 
		self.spin    = [-1,1]
		self.lattice = np.ones((self.column , self.row))

	def metro(self):
		#self.copy()
		#self.old_state = self.lattice
		flip = np.random.randint(self.column, size=2)
		self.flip_spin(flip[0], flip[1])
		change = self.eneryChange(flip[0], flip[1])
		#print change
		#exit()
		self.a_prob(change, flip[0], flip[1])

	def copy(self):
		self.old_state = np.zeros((self.column, self.row))
		for i in range(self.row):
			for j in range(self.column):
				self.old_state[i][j] = self.lattice[i][j]



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
				#print np.sum(self.lattice)
				#exit()
				self.lattice[idx_r][idx_c] *= -1
		
				
				#print "I'm in"
				#exit()
				#self.old_state = self.lattice
			#else:
				#print rand
				#print change
				#print np.exp(-self.beta*change)
				

				#print np.sum(self.old_state)
				
				#self.lattice[idx_r][idx_c] *= -1
		
			
			

	def energy(self):
		total_E = 0

		for i in range(self.row):
			for j in range(self.column):
				spin_list = []
				sum_spin = 0
				for r1 in xrange(1,3,1):
					for r2 in xrange(1,3,1):
						sp = []
						col = (i + r1)%self.column
						row = (j + r2)%self.row
						sp.append(col)
						sp.append(row)
						spin_list.append(sp)

				for r in range(4):	
					sum_spin += self.lattice[spin_list[r][0]][spin_list[r][1]]
					

				total_E -= sum_spin

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
	rand = np.random.randint(2, size=(ising.column, ising.row))
	for i in range(ising.column):
		for j in range(ising.row):
			if rand[i][j] == 1:

				ising.lattice[i][j] = 1
			else:
				ising.lattice[i][j] = 0
	#print ising.lattice
	#exit()

	print t 
	T.append(t)
	ising.temp = t
	ising.beta = 1/t

	for i in range(ising.column*ising.row*2000):
		
			#smp.imsave("result_%d.jpg" % i, ising.lattice)


		ising.metro()
		#if i%(2000*100*10) == 0:
		#	im = ising.draw_image()
		#	smp.imsave("result_%d.jpg" % i, im)
		#if i%10000 == 0:
		#	im = ising.draw_image()
		#	smp.imsave("result_%d.jpg" % i, im)
		#	print np.sum(ising.lattice)
		#if (i < 500000):

		#	if i % 50000  == 0:
		#		time.append(i)
		#		mag.append(np.sum(ising.lattice)/(ising.column*ising.row))
				#E.append(ising.energy())
		#else:
		#	if i % 5000 == 0:
		#		time.append(i)
		#		mag.append(np.sum(ising.lattice)/(ising.column*ising.row))


	

	#plt.plot(time, mag, 'ro')
	#plt.show()
	#exit()
	#im = ising.draw_image()
	#smp.imsave("result_%d.jpg" % t, im)

	
	mm = abs(np.sum(ising.lattice)/(ising.column*ising.row))
	mag.append(mm)



fig = plt.figure()
plt.plot(T, mag, 'ro')
plt.suptitle('m-T J=1', fontsize=24)
plt.xlabel('Temp T(K)', fontsize=18)
plt.ylabel('magnetization m', fontsize=18)
#fig.savefig("J_1_B_1.jpg")

plt.show()


print mag
















