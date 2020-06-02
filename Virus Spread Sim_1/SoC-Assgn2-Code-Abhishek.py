import random
from random import randint
from random import choice
import matplotlib.pyplot as plt
import numpy as np
for s in range(500):
  a=[[0 for i in range(120)] for j in range(125)]   
  p=[1]
  a[59][62]=1
  k=0
  while(k!=15000):
    for j in range(0,125):
      for i in range(0,120):
        if(a[j][i]==1):
          for x in range(i-1,i+2):
            for y in range(j-1,j+2):
              if((0<=y<125) and (0<=x<120) and (a[y][x]!=1) and (random.random()<0.25)):
                a[y][x]=2      
          y=j-2
          for x in [i-2,i-1,i,i+1,i+2]:
            if((0<=y<125) and (0<=x<120) and (a[y][x]!=1) and (random.random()<0.08)):
              a[y][x]=2      
          y=j+2  
          for x in [i-2,i-1,i,i+1,i+2]:
            if((0<=y<125) and (0<=x<120) and (a[y][x]!=1) and (random.random()<0.08)):
              a[y][x]=2
          x=i-1
          for y in [j-1,j,j+1]:
            if((0<=y<125) and (0<=x<120) and (a[y][x]!=1) and (random.random()<0.08)):
              a[y][x]=2
          x=i+1
          for y in [j-1,j,j+1]:
            if((0<=y<125) and (0<=x<120) and (a[y][x]!=1) and (random.random()<0.08)):
              a[y][x]=2    
    for i in range(8):
      y=randint(0,124)
      x=randint(0,119)
      z=randint(0,124)
      w=randint(0,119)
      t=[a[y][x],a[z][w]]
      a[y][x]=t[1]
      a[z][w]=t[0]  
    k=0  
    for j in range(125):
      for i in range(120):
        if((a[j][i]==1) or (a[j][i]==2)):
          a[j][i]=1
          k=k+1         
    p.append(k)
  plt.plot(p)
  plt.xlabel('Iteration')
  plt.ylabel('Number of ones')
  plt.show()
  print('iteration number: ',s+1)
  
  p1.append(len(p))
plt.plot(p1)
plt.xlabel('Number of runs')
plt.ylabel('Iterations')
plt.show()
b=np.array(p1)
print("Average number of iterations is: ",b.mean())
from scipy.signal import savgol_filter
p3=[]
for i in range(len(p)-1):
  p3.append(p[i+1]-p[i])
plt.plot(p3)
plt.xlabel('x')
plt.ylabel('dy/dx')
yhat=savgol_filter(p3,25,7)
plt.plot(yhat,c='red')
plt.show()    
print("Maximum of dy/dx is: ",max(yhat))