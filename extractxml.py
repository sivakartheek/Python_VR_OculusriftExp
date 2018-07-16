""" This module analyses and extracts the data from xml file.
The sample data of different trajectory files used for experiments 
is shown in sample_trajectory_file.xml
(random data-format used shown in that file)
"""

from xml.etree import ElementTree as ET

def trajectories(input_xml):
    tree = ET.parse(input_xml)
    root = tree.getroot()

    pedestrians_data = [] 
    frame_id = [] 
    ped_id = [] 
    x_pos_ped = []   
    y_pos_ped = []  
    next_frame_id_number = []  

    for frame in root.iter('frame'):
        frame_id.append(frame.attrib)
    for agents in root.iter('agent'):
        pedestrians_data.append(agents.attrib)

    length = len(pedestrians_data)
    n = 0

    for i in range(1, length):
        n = n + 1
        if (int(pedestrians_data[i]['ID']) < int(pedestrians_data[i-1]['ID']) or
            int(pedestrians_data[i]['ID']) == int(pedestrians_data[i-1]['ID'])):
            next_frame_id_number.append(n)
            n = 0
    for i in range(length):
        ped_id.append(int(pedestrians_data[i]['ID']))
        x_pos_ped.append(float(pedestrians_data[i]['x']))
        y_pos_ped.append(float(pedestrians_data[i]['y']))
        
    return ped_id, x_pos_ped, y_pos_ped, next_frame_id_number
    



