
""" This module explains to find the operations of the pedestrians
like sped of the predefined pedestrians, giving movement to the 
pedestrians and reset of the experiment.
"""

import viz
import viztask
import vizact

from math import sqrt
import collections
import __builtin__

import file_check_write as of
import pedestrian_allocation as ped
import extractxml as xml

def velocity(index,id_temp):
    var = id_temp[index]
    j = index
    index = index - 1
    
    while var != id_temp[index]:
        index = index - 1
        if j - index == 100:
            break
    if j - index <= 50:
        walkspeed = sqrt((x[j] - x[index]) * ( x[j] - x[index])
                              + (y[j] - y[index]) * (y[j] - y[index])) * 16
    else:
        walkspeed = 1.3889
    return walkspeed

def endPedTrack(index, id_temp):     
    var = id_temp[index]
    j = index
    
    if j == len(id_temp) - 1:
        return j
    else:
        index = index + 1
        while var != id_temp[index]:
            if index - j  >  50:
                return j
                break
            elif index == len(id_temp) - 1:
                return j
                break
            index = index + 1

def visibileOn(avatar):
    avatar.visible(viz.ON)

def visibileOff(avatar):
    avatar.visible(viz.OFF)

def walkAvatars():
    frame_number = 0 
    once = 1
    next = 1
    i = 1
    m = n = 0 
    x_after = 2.1
    y_after = -12
    x_after1 = -2.1
    
    of.fileOpen(filename)
    yield viztask.waitKeyDown('m')

    for j in nn:
        opfile.write('FRAME')
        opfile.write(str(frame_number))
        opfile.write('\n')
        
        for k in range(1, j + 1):
            walkspeed = velocity(i, id_temp)
            walk = vizact.walkTo([x[i] , 0 , y[i]],
                                 turnInPlace = True, walkSpeed = walkspeed)
            id1[id_temp[i]].addAction(walk)
            index = endPedTrack(i, id_temp)
            of.trackRemainPedPos(i)
            s = of.startTrack(i)
            
            if (s == 2) or (once == 2):
                of.trackExpermentiee()
                once=1
                next=2
            if index == None:
                visibileOn(id1[id_temp[i]])
            else:
                if (x[i] > 1.5) and (x[i] < 2.6):
                    walk1 = vizact.walkTo([x_after, 0, y_after],
                                          turnInPlace = True, walkSpeed = 1.39)
                    id1[id_temp[i]].addAction(walk1)
                    if m == 4:
                        y_after = -12
                        x_after = x_after - 0.4
                        m = 0
                    else:
                        y_after = y_after+0.4
                    m = m + 1
                elif (x[i] > -2.2) and (x[i] < -1.5):
                    walk1 = vizact.walkTo([ x_after1,0,y_after],
                                          turnInPlace = True, walkSpeed = 1.39)
                    id1[id_temp[i]].addAction(walk1)
                    if n == 4:
                        y_after = -12
                        x_after1 = x_after1 + 0.4
                        n = 0
                    else:
                        y_after = y_after + 0.4
                    n= n + 1
            i = i + 1
        yield viztask.waitTime(0.1)#0.625
        frame_number = frame_number + 1
        if next == 2:
            once = 2
    opfile.close()
    
def resetExperiment():
    of.fileOpen(filename)
    opfile.close()
    
    p = ped.Ped()
    p.removePedestrians()
    __builtin__.pedestrians = []
    
    input_xml = viz.input('Enter the trajectory file name:: ')
    __builtin__.filename = viz.input(
        'Enter the file name to store the data of the experimentee\
        (with file extension.txt)::'
    )
    p = ped.Ped()
    __builtin__.pedestrians = p.pedestrainsDef()
    __builtin__.id_temp, __builtin__.x, __builtin__.y, __builtin__.nn = xml.trajectories(input_xml)
    __builtin__.id1 = collections.OrderedDict.fromkeys(id_temp)
    __builtin__.key_index = list(id1.keys())

    j = 0
    for i in id1:
        id1[i] = pedestrians[j]
        j = j + 1
    task = viztask.schedule(walkAvatars())


    
    
    
