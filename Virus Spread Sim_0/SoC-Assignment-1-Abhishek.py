def swap(l):
 
  for i in range(5):
    from random import choice
    a=choice(list(range(0,10000)))
    b=choice(list(range(0,10000)))
    s=[l[a],l[b]]
    l[a]=s[1]
    l[b]=s[0]
p1=[]
for i in range(1000):  
  a=[]
  for i in range(10000):
    a.append(0)
  a[4999]=1

  prob=[0]*65
  for i in range(35):
    prob.append(1)

  p=[]
  import matplotlib.pyplot as plt
  from random import choice
  k=0
  while(k!=10000):
    i=0
    swap(a)
    while(i<9999):
      if(a[i]==1):
       if((choice(prob)==1) and (i<9999) and (a[i+1]!=1)):
          a[i+1]=1
          i=i+1
       if((choice(prob)==1) and (i<9999) and (a[i-1]!=1)):
         a[i-1]=1
      i=i+1 
    k=0
    for i in range(10000):
      if(a[i]==1):
        k=k+1   
    p.append(k)
  plt.plot(p)
  plt.xlabel('iteration')
  plt.ylabel('number of ones')
  plt.show()
  p1.append(len(p));
plt.plot(p1)
plt.xlabel('number of runs')
plt.ylabel('number of iterations')  
plt.show()
import numpy as np
b=np.array(p1)
print("average of number of iterations ",b.mean())
p2=[]
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
for i in range(0,len(p1)-1):
  p2.append(p1[i+1]-p1[i])
plt.plot(p2);
yhat=savgol_filter(p2,101,5)
plt.xlabel('x')
plt.ylabel('dy/dx')
plt.plot(yhat,c='red')
plt.show()
print("maximum of dy/dx: ",max(yhat))

