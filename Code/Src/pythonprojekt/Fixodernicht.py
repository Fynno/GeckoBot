# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:47:15 2018

@author: Fynn
"""
from numpy import linalg as LA
import csv
import math
import numpy as np

b = [];

with open('S90F0_5.txt','r') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=' ')
        
        for line in csv_reader:
            a = [line[6],line[8],line[10]]
            b.append(a)
            
x = np.array(b)
y = x.astype(np.float)
            
       

def checkiffixed (startvec,endvec):
    
    g = [0,0,1]; "Calibrate by using by using the sensor output on a flat surface"
    delta = 90 - math.asin((np.dot(startvec,g))/(LA.norm(g)*LA.norm(startvec)))*57.2958
    
    if delta < 30:
        return 1
    
    safety = np.dot(startvec,endvec)/(LA.norm(startvec)*LA.norm(endvec))
        
    if safety <= 1 and safety >= -1:
        difangle = math.acos(safety)*57.2958
            
                    
    if difangle > (1.01*delta+24.5):
        return 0
    
    else:
        return 1


g = [0,0,1]; "Calibrate by using by using the sensor output on a flat surface"

"Check if testmove is necessary"
startvec = y[0]



else:
        if checkiffixed(y) == 1:
            print("continue")
        else:
            print("return to last pose")
    



