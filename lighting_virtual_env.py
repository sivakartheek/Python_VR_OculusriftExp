
""" This module sets the light condition to the virtual model in respective to
the x z y directions as similar to the real scenario in virtual environment.
"""

import viz

mylight = viz.addLight() 
mylight.position(-5, 5.9, 0) 
mylight.direction(0, 0, 1) 
mylight.spread(180) 
mylight.intensity(3) 
mylight.spotexponent(3) 
mylight.setPosition(0, 1, 0)

whitelight = viz.addLight()
whitelight.enable() 
whitelight.position(0, 0, 0)
whitelight.position(-5, 0, 0)
whitelight.position(5, 0, 0)
whitelight.position(-5, 0, 5.9)
whitelight.position(5, 0, 5.9)
whitelight.position(-5, 0, -4.1)
whitelight.position(5, 0, -4.1)
whitelight.position(10, 0, 5)
whitelight.position(15, 0, 5)
whitelight.spread(180)
whitelight.intensity(3)
whitelight.spotexponent(3)


