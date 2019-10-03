from graph import *
from math import *
import random


#фон
brushColor(42, 135, 41)
rectangle(0, 0, 500, 300)

brushColor(110, 48, 74)
rectangle(0, 300, 500, 600 )



#элипс
def nangle(x1, x2, y1, y2, a, c):
    for x in range ( (x1-a), (x2+a) ):
        for y in range ( (y1-a), (y2+a) ):
            if sqrt((x-x1)**2 + (y-y1)**2) + \
            sqrt((x-x2)**2 + (y-y2)**2) < a:
                point(x, y, c)
#цвет черепахи (61, 9, 60)


def grib(x, y, k, AA):
    A = AA/180*pi
    k = k/2
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


def nangle2(x, y, k, a, c):
    brushColor(c)
    a = a/180*3.14
    x1 = x
    y1 = y
    x2 = x+k*1*cos(a)
    y2 = y-k*1*sin(a)
    x3 = x+k/2*cos(a)-k*5*sin(a)
    y3 = y-k/2*sin(a)-k*5*cos(a)
    polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])

#x=280
#y=525
def fullpls(x, y, k, AA):
    nangle(x, int(x+k*130), y, y, int(k*175), (61, 9, 60))
    nangle(int(x+k*145), int(x+k*190), int(y-k*25), int(y-k*25), int(k*55), (61, 9, 60))
    nangle(int(x+k*125), int(x+k*140), int(y+k*50), int(y+k*50), int(k*25), (61, 9, 60))
    nangle(int(x+k*10), int(x+k*25), int(y+k*50), int(y+k*50), int(k*25), (61, 9, 60))
    nangle(int(x-k*30), int(x-k*13), int(y+k*25), int(y+k*25), int(k*25), (61, 9, 60))
    nangle(int(x+k*140), int(x+k*155), int(y+k*25), int(y+k*25), int(k*25), (61, 9, 60))
    nangle(int(x+k*175), int(x+k*175), int(y-k*35), int(y-k*35), int(k*5), (52, 255, 20))
    nangle(int(x+k*195), int(x+k*195), int(y-k*25), int(y-k*25), int(k*5), (255, 20, 20))
    
    x0 = x
    y0 = y
    for x in range (int(x0-25*k), int(x0+130*k)):
        for y in range (int(y0-50*k), int(y0+50*k), int(2*k)):
            if sqrt((x-x0)**2 + (y-y0)**2) + \
               sqrt((x-x0-130*k)**2 + (y-y0)**2) < 175:
                if random.random() < 0.015:
                    m = random.random()
                    nangle2(x, y, int(k*10), 20-m*40, (28, 28, 28))
    
    grib(int(x-50*k), int(y-120*k), k, AA)
    nangle(x, x, int(y-115*k), int(y-115*k), int(45*k), (255, 0, 0))
    nangle(int(x-80*k), int(x-80*k), int(y-115*k), int(y-118*k), int(45*k), (181, 142, 0))
    nangle(int(x-110*k), int(x-105*k), int(y-110*k), int(y-110*k), int(45*k), (181, 142, 0))
    
    for x in range (int(x0-25*k), int(x0+130*k)):
        for y in range (int(y0-50*k), int(y0+50*k), int(2*k)):
            if sqrt((x-x0)**2 + (y-y0)**2) + \
               sqrt((x-x0-130*k)**2 + (y-y0)**2) < 175:
                if random.random() < 0.015:
                    m = random.random()
                    nangle2(x, y, int(k*10), 20-m*40, (28, 28, 28))
    




fullpls(280, 525, 1, 15)
fullpls(180, 350, 0.5, 10)
fullpls(430, 320, 0.55, 10)

#деревья
brushColor(207, 207, 19)
rectangle(0, 0, 40, 400 )    

brushColor(207, 207, 19)
rectangle(340, 0, 370, 350 )

brushColor(207, 207, 19)
rectangle(450, 0, 490, 430 )

brushColor(207, 207, 19)
rectangle(70, 0, 200, 580 )


for x in range (50, 250, 40):
    k = random.random()
    if k < 0.5:
        k = k + 0.5
    n = random.random()
    AA = -20 + 40*n
    grib(x, 550, k, AA)
    







run()
