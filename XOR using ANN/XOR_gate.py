import numpy as np
import random
import math
import matplotlib.pyplot as plt

def __init__(x,y,z,W_1):
    row=[]
    for i in range(y):
        for j in range(x+1):
            row.append(random.random())
        W_1.append(row)
        row=[]
    W_1=np.array(W_1)

def init_out(H,W_2):
    
    H.reshape(-1,1)
    for i in range(len(H)):
        W_2.append(random.random())    
    W_2=np.array(W_2)    
    return sigmoid(np.dot(W_2,H)),W_2,H

def train(I,H,O,W_1,W_2):
    I=I.reshape(-1,1)
    H=np.dot(W_1,I)
    for i in range(len(H)):
        H[i]=sigmoid(H[i])
    H=np.append(H,1)
    H.reshape(-1,1)    
    O=sigmoid(np.dot(W_2,H))
    return I,H,O,W_1,W_2
    
def backprop(O,y,c,W_1,W_2,I):
    c=math.pow(O-y,2)
    dc1=[]
    dc2=[]
    dc2=np.multiply(2*(O-y)*dsigmoid(O),H)
    dh=[]
    for i in range(len(H)-1):
        dh.append(dsigmoid(H[i]))
    dh=np.array(dh)
    dh=dh.reshape(-1,1)
    
    I=I.reshape(1,-1)
    dc1=(np.dot(dh,I))*2*(O-y)
    W_2=W_2-np.multiply(dc2,0.1)
    W_1=W_1-np.multiply(dc1,0.1)
    return O,y,c,W_1,W_2,I
#---------------------------------------------------
def sigmoid(x):
    return 1/(1+math.exp(-x))

def dsigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))
x1=float(input("x1= "))
x2=float(input("x2= "))
global W_1
W_1=[]
global W_2
W_2=[]
global I
I=np.array([x1,x2,1])
__init__(2,2,1,W_1)
global H
H=np.dot(W_1,I)
H=np.append(H,1)
for i in range(len(H)):
    H[i]=sigmoid(H[i])        
global O
O,W_2,H=init_out(H,W_2)
#----------------------------------------------------
if x1==1 and x2==0:
    y=1
if x1==0 and x2==1:
    y=1
if x1==1 and x2==1:
    y=0
if x1==0 and x2==0:
    y=0
#---------------------------------------------------
global c
cost=[]
output=[]
for i in range(1000):
    O,y,c,W_1,W_2,I=backprop(O,y,c,W_1,W_2,I)
    I,H,O,W_1,W_2=train(I,H,O,W_1,W_2)
    cost.append(c)
    output.append(O)
    
    
plt.plot(cost)
plt.xlabel("epoch")
plt.ylabel("Cost function")
plt.show()

plt.plot(output)
plt.xlabel("epoch")
plt.ylabel("Output")
plt.show()


        



        