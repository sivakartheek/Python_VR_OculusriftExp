
""" This script demonstrates the study of the exit choice behaviour of the
pedestrians by uisng VirtualReality and OcculusRift headset.
The banner uses a sequence helper to animate. Use the WASDQE keys to move
around. It has also need the extractml.py, lighting_virtual_env.py, 
pedestrian_allocation.py oculus_gamepad.py and find_methods.py files during compling.
Software requirements: python and Vizard(Virtual reality)for conducting ecperiments 
and for Analysis(R and python)
Thesis pdf file is available at:
http://www.asim.uni-wuppertal.de/fileadmin/bauing/asim/Thesen/Master_Dissertation_sreeram.pdf
If OcculusRift is not available still the experiment can be done by comment the occulus
module, occulus_gamepad.py and vizconnect.go('oculus_gamepad.py')          
"""

import viz
import vizact
import viztask
import vizinfo
import vizshape
import vizconnect
import oculus

import time
import collections
from math import sqrt
import __builtin__

import extractxml as xml                     
import lighting_virtual_env                             
import keyboard_movement                     
import pedestrian_allocation as ped
import file_check_write as of 
import find_methods as meth

viz.setMultiSample(4)                        
viz.go()
viz.MainWindow.fov(70)                       
viz.MainView.collision(viz.ON)              
viz.MainView.gravity (0)                     
viz.collision(viz.ON)
#vizconnect.go('oculus_gamepad.py')          
viz.MainView.move(0, 0, 15)
viz.MainView.setEuler(180, 0, 0)
viz.MainView.stepsize(2)

# Adds sky environment to the model 
sky = viz.add(viz.ENVIRONMENT_MAP, 'sky.jpg') 
skybox = viz.add('skydome.dlc')
skybox.texture(sky)

#The virtual model with two exit doors and entrance 
model = viz.addChild('Geometry_dim_RouteA.osgb') 

#Add vizinfo panel to display instructions
info = vizinfo.InfoPanel(
    'Use the WASDQE keys to move around the room \n\
     To Run the Experiment Press "m" \n\
     To Reset the Experiment Press "r" '
    )
input_xml = viz.input(
    'Enter the trajectory file name which contains data of the predefined pedestrians::'
    )
check_traj_file = viz.ask(
	'Is the name given in xml file and the no of pedestrians movemement used \
	in the xml file is correct or not?'
	)
if check_traj_file == 1:
    viz.go()
else:
    viz.quit()

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

task = viztask.schedule(meth.walkAvatars() )
vizact.onkeydown('r', task.kill)
vizact.onkeydown('r', meth.resetExperiment)


