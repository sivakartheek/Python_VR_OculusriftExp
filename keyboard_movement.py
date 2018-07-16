""" This module is used to define the movement around the virtual environment
by using keyboard.  In case if you are using occulusmodule.py with gamepad or
any other device then this module have to be disable in the main file
"""

import viz
import viztracker

key_tracker = viztracker.Keyboard6DOF(
    forward='w', backward='s', left='a',
    right='d', turnRight='e', turnLeft='q'
    )
key_link = viz.link(key_tracker, viz.MainView)
key_link.enable()
