
""" This module defines the declaration, allocation  and deallocation
of the pedestrians in the virtual environment of the virtual model.
"""

import viz


class Ped:

    no_ped = viz.input('Enter the no of pedestrains(18 or 40)::')
    
    def __init__(self, n = no_ped):
        self.n = n

    def pedestrainsDef(self):
        ped_xdir = [
            -0.7, 0, 0.3, 0.6
            ]
        ped_ydir = [
            6.9, 7.3, 7.7, 8.1, 8.5,
            8.9, 9.3, 9.7, 10.1, 10.5
            ]
        pedestrian = []
        factor = int(self.n / 4)
        
        if factor == 4:
            factor = 5

        k = j = 0
        for i in range(factor):
            male = viz.addAvatar('vcc_male.cfg')
            male.setPosition([ped_xdir[k], 0, ped_ydir[i]])
            male.setEuler([180, 0, 0])
            male.state(1)
            pedestrian.append(male)

            male1 = viz.addAvatar('vcc_male2.cfg')
            male1.setPosition([ped_xdir[k+1], 0, ped_ydir[i]])
            male1.setEuler([180, 0, 0])
            male1.state(1)
            pedestrian.append(male1)

            female = viz.addAvatar('vcc_female.cfg')
            female.setPosition([ped_xdir[k+2], 0, ped_ydir[i]])
            female.setEuler([180, 0, 0])
            female.state(1)
            pedestrian.append(female)
               
            male2 = viz.addAvatar('vcc_male.cfg')
            male2.setPosition([ped_xdir[k+3], 0, ped_ydir[i]])
            male2.setEuler([180, 0, 0])
            male2.state(1)
            pedestrian.append(male2)

            k=0
        if self.no_ped == 18:
            pedestrian[-2].remove()
            pedestrian[-1].remove()
            del pedestrian[-2:]
            
        return pedestrian
    
    def removePedestrians(self):
        for i in range(1,len(id1)+1):
            id1[i].remove()
       


        

