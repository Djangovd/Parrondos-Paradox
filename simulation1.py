# -*- coding: utf-8 -*-
"""
Written by P. Motylinski
Illustration of Parrondo's paradox
"""
"""
Spyder Editor

This is a temporary script file.
"""

import random
import matplotlib.pyplot as plt

iter1 = 100000
iter2 = 100
eps= 0.005 * 1.
p1 = 1./2.  - eps
p2 = 1./10. - eps
p3 = 3./4.  - eps

rev1 = 0
rev1arr = []
rev2 = 0
rev2arr = []
######################
def toss(r,p,capital):
#    print "capital in = " + str(capital)
    if r < p:
        capital += 1
    else:
        capital -= 1
#    print "r, p, capital = " +str(r) + " " + str(p) + " " + str(capital)
#    print "capital out= " + str(capital)
    return capital
######################

def test(capital):
    return capital+1

#for l in range(0,iter2):
plt.figure(1)   
for i in range(0,iter1):
    r1 = random.random()
#    print "capital pre toss = " + str(rev1)
    rev1 = toss(r1, p1, rev1)       
#    print "capital post toss = " + str(rev1)
    if i%100==0: print "Capital game1 = " + str(rev1)
    rev1arr.append(float(rev1))
plt.subplot(311)
plt.plot(range(0,iter1),rev1arr)
print "~~~~~~~~~~"
for i in range(0,iter1):
    r1 = random.random()
    if rev2 % 3 == 0:
        rev2 = toss(r1,p2,rev2)
    else:
        rev2 = toss(r1,p3,rev2)
#    if i%100==0: print "Capital game2 = " + str(rev2)
    rev2arr.append(float(rev2))

plt.subplot(312)
plt.plot(range(0,iter1),rev2arr)
print "~~~~~~~~~~"   
rev1 = 0
rev1arr = []
for i in range(0,iter1):
    r1 = random.random()
    if r1 < 0.5 :
        rev1 = toss(r1,p1,rev1)
        print "game A"
    else:
        if rev1 % 3 == 0:
            rev1 = toss(r1,p2,rev1)
        else:
            rev1 = toss(r1,p3,rev1)
        print "game B"    
    rev1arr.append(float(rev1))

plt.subplot(313)
plt.plot(range(0,iter1),rev1arr)   
