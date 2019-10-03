
from math import *
import random

i = 0
for n in range (100):
    for x in range (0, 10000, n):
        if 1/n < random.random():
        	i = i + 1
print(i)



run()