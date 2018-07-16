""" This module is used to check and write tracked data of 
the expermentiee into a file. 
"""

import viz
import __builtin__

def fileOpen(filename):
	if len(filename) == 0:
		print 'Filename Error::filename is not given'
		viz.quit()
	else:
		__builtin__.opfile = open(filename, 'w+')
		opfile.write(str('ID'))
		opfile.write('\t')
		opfile.write(str('X-Position'))
		opfile.write('\t')
		opfile.write(str('Y-Position'))
		opfile.write('\n')

def trackExpermentiee():
	ID = len(id1) + 1
	X, Z, Y = viz.MainView.getPosition()
	
	opfile.write(str(ID))
	opfile.write('\t')
	opfile.write(str(X))
	opfile.write('\t')
	opfile.write(str(Y))
	opfile.write('\n')

def trackRemainPedPos(i):
	id_ped = id_temp[i]
	X, Z, Y = id1[id_temp[i]].getPosition()
	
	opfile.write(str(id_ped))
	opfile.write('\t')
	opfile.write(str(X))
	opfile.write('\t')
	opfile.write(str(Y))
	opfile.write('\n')

"""checking for when to start the tracking of the experimentee
1:start to take position of avatar
2:not to take position of avatar
"""
check = 1 
started_Track = 1
def startTrack(i):
	global check
	global started_Track
	starter_index = key_index[-4]
	if check == 1:
		if id_temp[i] == starter_index:
			print 'Started tracking'
			check = 2
			return 2
