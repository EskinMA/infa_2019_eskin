from graph import *
from math import *
import random

#элипс
def nangle(x1, x2, y1, y2, a, c):
    for x in range ( (x1-a), (x2+a) ):
        for y in range ( (y1-a), (y2+a) ):
            if sqrt((x-x1)**2 + (y-y1)**2) + \
            sqrt((x-x2)**2 + (y-y2)**2) < a:
                point(x, y, c)
#цвет черепахи (61, 9, 60)


#фон
brushColor(42, 135, 41)
rectangle(0, 0, 500, 300)

brushColor(110, 48, 74)
rectangle(0, 300, 500, 600 )

#деревья
brushColor(207, 207, 19)
rectangle(0, 0, 40, 400 )    
 
brushColor(207, 207, 19)
rectangle(70, 0, 200, 580 )

brushColor(207, 207, 19)
rectangle(340, 0, 370, 350 )

brushColor(207, 207, 19)
rectangle(450, 0, 490, 430 )


#тело
nangle(280, 410, 525, 525, 175, (61, 9, 60))
#голова
nangle(425, 470, 500, 500, 55, (61, 9, 60))
#нога ниж.пер.
nangle(405, 420, 575, 575, 25, (61, 9, 60))
#нога niz.zad.
nangle(290, 305, 575, 575, 25, (61, 9, 60))
#нога verh.zad
nangle(250, 267, 550, 550, 25, (61, 9, 60))
#нога verh.pered
nangle(420, 435, 550, 550, 25, (61, 9, 60))
#glaz praviy
nangle(455, 455, 490, 490, 5, (52, 255, 20))
#glaz leviy
#nangle(450, 450, 495, 495, 5, (52, 255, 20))
#nos
nangle(475, 475, 500, 500, 5, (255, 20, 20))



#treugol'niki (igla(mnogo) ili koluchki)
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

#igly
  #rog
nangle2(465, 487, 5, -40, (153, 150, 147))
#igly
for x in range (250, 400):
    for y in range (475, 575, 2):
        if sqrt((x-280)**2 + (y-525)**2) + \
           sqrt((x-410)**2 + (y-525)**2) < 175:
            if random.random() < 0.015:
                m = random.random()
                nangle2(x, y, 10, 20-m*40, (28, 28, 28))
#grib
def grib(x, y, k, a, c):
    brushColor(c)
    
    polygon([(x1, y1), (x2, y2), (x3, y3), (x1, y1)])

#apple
nangle(380, 380, 460, 460, 45, (255, 0, 0))
nangle(310, 310, 450, 447, 45, (181, 142, 0))
nangle(280, 285, 455, 480, 45, (181, 142, 0))


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

grib(335, 450, 0.4, 10)


#igly
for x in range (250, 400):
    for y in range (475, 575, 2):
        if sqrt((x-280)**2 + (y-525)**2) + \
           sqrt((x-410)**2 + (y-525)**2) < 175:
            if random.random() < 0.01:
                m = random.random()
                nangle2(x, y, 10, 20-m*40, (28, 28, 28))





run()