from graph import *
from math import *
import random


def nangle(x1, x2, y1, y2, a, c):
    for x in range ( (x1-a), (x2+a) ):
        for y in range ( (y1-a), (y2+a) ):
            if sqrt((x-x1)**2 + (y-y1)**2) + \
            sqrt((x-x2)**2 + (y-y2)**2) < a:
                point(x, y, c)


def grib(x, y, k, AA):
    A = AA/180*pi
    nangle(x, int(x-120*k*sin(A)), y, int(y+120*k*cos(A)), int(k*150), 'white')
    nangle(int(x-75*k*cos(A)+40*k*sin(A)), int(x+90*k*cos(A)+20*k*sin(A)),
           int(y-40*k*cos(A)-75*k*sin(A)), int(y-20*k*cos(A)+90*k*sin(A)),
        int(k*180), 'red' )
    nangle(int(x-60*k*cos(A)+30*k*sin(A)), int(x-45*k*cos(A)+30*k*sin(A)),
           int(y-30*k*cos(A)-60*k*sin(A)), int(y-30*k*cos(A)-45*k*sin(A)),
        int(k*20), 'white' )
    nangle(int(x-30*k*cos(A)+50*k*sin(A)), int(x-14*k*cos(A)+50*k*sin(A)),
           int(y-50*k*cos(A)-30*k*sin(A)), int(y-50*k*cos(A)-14*k*sin(A)),
        int(k*20), 'white' )
    nangle(int(x+10*k*cos(A)+20*k*sin(A)), int(x+27*k*cos(A)+20*k*sin(A)),
           int(y-20*k*cos(A)+10*k*sin(A)), int(y-20*k*cos(A)+27*k*sin(A)),
        int(k*20), 'white' )
    nangle(int(x+20*k*cos(A)+40*k*sin(A)), int(x+37*k*cos(A)+40*k*sin(A)),
           int(y-40*k*cos(A)+20*k*sin(A)), int(y-40*k*cos(A)+37*k*sin(A)),
        int(k*20), 'white' )
    nangle(int(x+60*k*cos(A)+30*k*sin(A)), int(x+77*k*cos(A)+30*k*sin(A)),
           int(y-30*k*cos(A)+60*k*sin(A)), int(y-30*k*cos(A)+77*k*sin(A)),
        int(k*20), 'white')

grib(100, 200, 0.4, 170)





run()