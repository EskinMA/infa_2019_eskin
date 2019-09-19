from graph import *
from math import *

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
for x in range (200, 500):
    for y in range (400, 600):
        if sqrt((x-280)**2 + (y-525)**2) + \
        sqrt((x-410)**2 + (y-525)**2) < 175:
           point(x, y, (61, 9, 60))
#голова
for x in range (400, 500):
    for y in range (400, 600):
        if sqrt((x-435)**2 + (y-525)**2) + \
        sqrt((x-450)**2 + (y-525)**2) < 25:
           point(x, y, (61, 9, 60))
#ноги



run()