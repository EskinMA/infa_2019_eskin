from graph import *
from math import *
import random


#elips cherez vse
def elips(x1, y1, A, a, e, c):

    x1 = x1 - e*a*cos(A)
    y1 = y1 + e*a*sin(A)
    for x in range ( int(x1-(1+e)*a), int(x1+(1+e)*a) ):
        for y in range ( int(y1-(1+e)*a), int(y1+(1+e)*a) ):
            AA =pi/2 - A*pi/180 + atan2((x-x1), (y-y1))
            if sqrt((x-x1)**2 + (y-y1)**2) < (a*(1-e**(1/2))/(1-e*cos(AA))) :
                point(x, y, c)
x = 100 
y = 200
k = 1
A = 45
a = 50


#grib
elips (x, y, A+90, a, 0.9, (0, 255, 0))
elips (x, y, A, a, 0.9, (0, 0, 255))







run()